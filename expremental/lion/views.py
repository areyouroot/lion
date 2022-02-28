from tkinter import Frame
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import threading
from .models import *
from django.core.mail import EmailMessage
import sqlite3
from sre_constants import SUCCESS
from tabnanny import check
import cv2
import numpy as np
import face_recognition as fc
import os

@gzip.gzip_page

def index(request):
    context = []
    return render(request, "lion/home.html", {'title': "index"})

#def facerec(request):
#    return render(request, "lion/facerec.html", {'title': "face"})

def facerec(request):

        id = request.GET['id']
        con = sqlite3.connect('face.db')
        c = con.cursor()
        print(id)
        c.execute("SELECT pic FROM face WHERE id = '%s'" % (id))
        img = (c.fetchall()[0][0])

        with open("check.jpg","wb") as file:
            file.write(img)

        cwd = os.getcwd()
        img = cv2.imread(f'{cwd}/check.jpg')
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        facescurframe = fc.face_locations(img)
        encode = fc.face_encodings(img,facescurframe)
        print(encode)

        cap = cv2.VideoCapture(0)
        while True:
            SUCESS,img = cap.read()
            imgs = cv2.resize(img,(0,0),None,0.25,0.25)
            imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

            facescurframe = fc.face_locations(img)
            encode2=fc.face_encodings(img,facescurframe)
            for encodeface,faceloc in zip(encode2,facescurframe):
                match = fc.compare_faces(encode,encodeface)
                if match[0] == True:
                    print("hehehe")
                    return render(request, "lion/facerec.html", {'title': "face",'id':id})



    #try:
    #    cam = VideoCamera()
    #    return StreamingHttpResponse(gen(cam),content_type="multipart/x-mixed-replace;boundary=frame")
    #except:
    #    pass


#class VideoCamera(object):
#    def __init__(self):
#        self.video = cv2.VideoCapture(0)
#        (self.grabbed, self.frame) = self.video.read()
#        threading.Thread(target=self.update, args=()).start()
#
#    def __del__(self):
#        self.video.release()
#
#    def get_frame(self):
#        image = self.frame
#        _, jpeg = cv2.imencode('.jpg', image)
#        return jpeg.tobytes()
#
#    def update(self):
#        while True:
#            (self.grabbed, self.frame) = self.video.read()
#
#def gen(camera):
#    while True:
#        frame = camera.get_frame()  
#        yield(b'--frame\r\n'
#        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
## Create your views here.
#