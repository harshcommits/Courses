// this extension allows node to use ECMAScript directly; therefore we use 'import' instead of 'require'

import { createServer } from 'http';

const server = createServer((req, res) => {
    res.end("Hello from ECMA");
});

server.listen(4343, () => {
    console.log("Server is running from ECMA syntax")
})