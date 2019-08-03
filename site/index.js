const express = require('express');
const app = express();

const views = __dirname+'/public/views/';
const controller = __dirname+'/public/app/controllers/'

app.use(express.static('public'));
app.listen(3000, () => console.log('Listening on 3000, visit "http://localhost:3000/"'));

app.get('/', (req, res) => {
    res.sendFile(views+'/html/index.html');
});



