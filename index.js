const cv = require('opencv4nodejs');
const path = require('path');
const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);
//const youtubedl = require('youtube-dl')
//const video = youtubedl('https://www.youtube.com/watch?v=bjzkmHRLTaI')
const FPS = 30;

const wCap = new cv.VideoCapture(0);
var frame = wCap.read();

//let frame = new cv.Mat(500,500, cv.CV_8UC4);
//let fgmask = new cv.Mat(500, 500, cv.CV_8UC1);
//let fgbg = new cv.BackgroundSubtractorMOG2(500, 16, true);
//cap.read(frame);
//fgbg.apply(frame, fgmask);


app.get('/', (req, res) => {
    $.ajax({
        type:"POST", url:"/send", data: {image: image}
    }).done(function (o){
        //do something
        frame = data.image;
        console.log('requested sucess');
    });
    res.sendFile(path.join(__dirname, 'index.html'));
});
function postdata(input) {
    $.ajax({
        type:"POST", url:"/send", data: {image: image}
    }).done(function (o){
        //do something
        frame = data.image;
        console.log('requested sucess');
    });
    console.log("iafasdn");
    print("kfjaofi");
}

// setInterval(() => {
//     interva();, 100/FPS
// }, 1000 / FPS)

// server.listen(3000);

setInterval(() => {
    //console.log("jadfkodijiosa");
    //alert("kajfl");
    interva;
    //console.log('adfa');
    const image = cv.imencode('.jpg', frame).toString('base64');
    io.emit('image', image);
}, 1000 / FPS);

function interva()
{
    //print("innnda");
    //alert("HELLO");
    console.log("Hellowordl");
    // $.ajax({
    //     type:"POST", url:"/send", data: {image: image}
    // }).done(function (o){
    //     //do something
    //     frame = data.image;
    //     console.log('requested sucess');
    // });
}

server.listen(3000);