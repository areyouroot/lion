from tkinter import Frame
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import threading
from .models import *
from django.core.mail import EmailMessage

@gzip.gzip_page

def index(request):
    context = []
    return render(request, "lion/home.html", {'title': "index"})

#def facerec(request):
#    return render(request, "lion/facerec.html", {'title': "face"})

def facerec(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam),content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    id = request.GET['id']
    return render(request, "lion/facerec.html", {'title': "face",'id':id})

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()  
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Create your views here.
