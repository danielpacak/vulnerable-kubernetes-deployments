const Pyroscope = require('@pyroscope/nodejs');
const {exec} = require("child_process")
const express = require('express')
const app = express()
const port = 3000

Pyroscope.init({
    serverAddress: 'http://localhost:4040',
    appName: 'hello-express',
    // Enable CPU time collection for wall profiles
    // This is required for CPU profiling functionality
    wall: {
      collectCpuTime: true
    },
    flushIntervalMs: 5000
});

Pyroscope.start()

app.get('/', (req, res) => {
    res.send('Hello World!')
})

const decodeReplyFromBusboy = (req, res) => {
    exec("uname -r", (error, stdout, stderr) => {
        if (error) {
            res.send({"error": error.message})
            return
        }
        if (stderr) {
            res.send({"stderr": stderr})
            return
        }
        res.send({"stdout": stdout})
    })
}

app.get('/process/exec', decodeReplyFromBusboy)

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
