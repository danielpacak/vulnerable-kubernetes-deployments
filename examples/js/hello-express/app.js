const {exec} = require("child_process")
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/process/exec', (req, res) => {req
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
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
