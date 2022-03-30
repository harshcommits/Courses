import express from 'express';

const app = express();
const port = 4000;

app.get('/', (req, res) => 
    res.send(`Node and express server running on port ${port}`)
);

app.listen(port, () => 
    console.log(`Your server is running on port ${port}`)
);