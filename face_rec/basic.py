import cv2
import numpy as np
import face_recognition as fc
from numpy.lib.index_tricks import ogrid

imgget = fc.load_image_file('./elone.jpg')
imgget = cv2.cvtColor(imgget,cv2.COLOR_BGR2RGB)
imgtest = fc.load_image_file('./elonetest1.jpg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

faceloc = fc.face_locations(imgget)[0] #prints the face location usefull to draw rectangle in image
encodeelone = fc.face_encodings(imgget)[0]
cv2.rectangle(imgget,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(0,0,255),2) #draws the rectangel in the face

faceloct = fc.face_locations(imgtest)[0] #prints the face location usefull to draw rectangle in image
encodeelonet = fc.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceloct[3],faceloct[0]),(faceloct[1],faceloct[2]),(0,0,255),2) #draws the rectangel in the face

results = fc.compare_faces([encodeelone],encodeelonet)
print (results)
print ("the encodings are :")
print(encodeelone)
print ('the data type is')
print (type(encodeelone))


cv2.imshow('elone',imgget)
cv2.imshow('elonetest',imgtest)
cv2.waitKey(0)
