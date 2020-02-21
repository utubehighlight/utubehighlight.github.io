import cv2
import numpy as np
import pafy # pip3 install youtube-dl
from flask import Flask, render_template, request, jsonify, redirect, make_response, url_for

app = Flask(__name__)


#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
url = ""



@app.route('/')
def index():
    print('new user')
    return render_template('index.html')
    
@app.route('/process', methods=['POST'])
def process():
    #print('processinfaddi')
    global url
    url = request.form['title']
    print("This is the url: " + url)
    try:# url == "https://www.youtube.com/watch?v=KVyMIEwI7uw":
        video = pafy.new(url)
        best = video.getbest(preftype="mp4")
        title = video.title
        rating = video.rating
        views = video.viewcount
        author = video.author
        length = video.length
        duration = video.duration
        captura = cv2.VideoCapture() #Youtube
        captura.open(best.url)
        #likes = video.likes
        #dislikes = video.dislikes
        #description = video.
        #send()
        return render_template('index.html', title=title)
        #send()
    except:
        title = 'Please enter a valid URL'
    print("THIS IS THE TITLE: " + title)
    return render_template('index.html', title=title)
    #return render_template('index.html')#jsonify({'title' : title})


#@app.route('/send', methods=['GET', 'POST'])
#def send():
#    if request.method == 'POST':
 #       url = request.form['url']
 #       try:# url == "https://www.youtube.com/watch?v=KVyMIEwI7uw":
 #           video = pafy.new(url)
  #      #best = video.getbest(preftype="mp4")
  #          title = video.title
  #          rating = video.rating
  #          views = video.viewcount
   #         author = video.author
   #         length = video.length
   #         duration = video.duration
   #         likes = video.likes
   #         dislikes = video.dislikes
   #         description = video.description
   #         print("in try")
   ##     except:
     ##       title = "Please enter a valid URL"
       #     print("in except")
        #rating = video.rating
        #views = video.viewcount
        #author = video.author
        #length = video.length
        #duration = video.duration
        #likes = video.likes
        #dislikes = video.dislikes

        
        #print(title)
        #stuff = description
        #stuff=f"Processing {title} by {author} for {length} with {likes} likes and {dislikes}."
        #print(f"Processing {title} by {author} for {length} with {likes} likes and {dislikes}.")
        #while True:
        #    ret, frame = captura.read()
        #    edges = cv2.Canny(frame, 50, 50)
            
            #cv2.imshow('Xtrack',edges)
        #    k = cv2.waitKey(24)&0xFF ##FRAME RATE
        #    if k == 27:
        #        break
        #    return edges
     #   return render_template('index.html', url=title)
    #return render_template('index.html')
@app.route("/send")
def send():
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    title = video.title
    rating = video.rating
    views = video.viewcount
    author = video.author
    length = video.length
    duration = video.duration
    captura = cv2.VideoCapture() #Youtube
    captura.open(best.url)
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

#captura = cv2.VideoCapture('drone.mp4')                 # Video File
#captura = cv2.VideoCapture(0)                           # Webcam 1,2,3
#captura = cv2.VideoCapture('http://192.168.1.68:8081/') # IPCamara

        # captura = cv2.VideoCapture() #Youtube
        # captura.open(best.url)
        # ret, img = captura.read()
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # for (x,y,w,h) in faces:
        #     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #     roi_gray = gray[y:y+h, x:x+w]
        #     roi_color = img[y:y+h, x:x+w]
        
        #     eyes = eye_cascade.detectMultiScale(roi_gray)
        #     for (ex,ey,ew,eh) in eyes:
        #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # cv2.imshow('img',img)
        # k = cv2.waitKey(30) & 0xff
        # if k == 27:
        #     break
        #yield render_template('index.html', title=title)
        #continue
    #return render_template('index.html', message='asd')
#captura.release()
#v2.destroyAllWindows()

if __name__ == "__main__":
    app.run(debug = True)