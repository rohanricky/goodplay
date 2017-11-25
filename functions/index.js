//Dependencies
var express = require('express');
var bodyParser = require('body-parser');
const routes = require('./router/api');
const functions = require('firebase-functions');
var firebase = require("firebase-admin");


// routes
var app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));

app.use('/static',express.static('static'));
app.get('/check',(req,res,next)=>{
    res.send("Express Working");
});

app.use('/api',routes);

//server port
app.set('port',(process.env.PORT || 6000));
exports.app = functions.https.onRequest(app);
