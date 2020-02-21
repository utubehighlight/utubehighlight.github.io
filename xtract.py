import cv2
import numpy as np
import pafy # pip3 install youtube-dl

#url = "https://www.youtube.com/watch?v=KVyMIEwI7uw" #INPUT
#shaqtin url = "https://www.youtube.com/watch?v=ZpJIDYphWTI" #INPUT
url = "https://www.youtube.com/watch?v=ymf1dNSRl0k" #Input
video = pafy.new(url)
best = video.getbest(preftype="mp4")
title = video.title
rating = video.rating
views = video.viewcount
author = video.author
length = video.length
duration = video.duration
likes = video.likes
dislikes = video.dislikes
#description = video.description

#captura = cv2.VideoCapture('drone.mp4')                 # Video File
#captura = cv2.VideoCapture(0)                           # Webcam 1,2,3
#captura = cv2.VideoCapture('http://192.168.1.68:8081/') # IPCamara

captura = cv2.VideoCapture() #Youtube
captura.open(best.url)
#print(title)
#stuff = description
#stuff=f"Processing {title} by {author} for {length} with {likes} likes and {dislikes}."
print(f"Processing {title} by {author} for {length} with {likes} likes and {dislikes} dislikes.")
while True:
    ret, frame = captura.read()
    edges = cv2.Canny(frame, 50, 50)
    
    cv2.imshow('Xtrack',edges)
    k = cv2.waitKey(24)&0xFF ##FRAME RATE
    if k == 27:
        break
    
captura.release()
cv2.destroyAllWindows()