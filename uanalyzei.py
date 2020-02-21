import cv2
import numpy as np
import pafy # pip3 install youtube-dl
import base64
from flask import Flask, render_template, redirect, url_for, request, make_response
app = Flask(__name__)

url = "https://www.youtube.com/watch?v=KVyMIEwI7uw"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

#captura = cv2.VideoCapture('drone.mp4')                 # Video File
#captura = cv2.VideoCapture(0)                           # Webcam 1,2,3
#captura = cv2.VideoCapture('http://192.168.1.68:8081/') # IPCamara

captura = cv2.VideoCapture() #Youtube
captura.open(best.url)

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/send")
def send():
    while 1:
        ret, img = captura.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    #return render_template('index.html', message='asd')
#captura.release()
#v2.destroyAllWindows()

if __name__ == "__main__":
    app.run(debug = True)