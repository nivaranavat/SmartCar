import picamera
import time
import cv2
import os
import numpy as np
#create object
camera = picamera.PiCamera()

#take a picture

#camera.capture('example.jpg')

#record a video
camera.start_recording('examplevid.h264')
time.sleep(5)
camera.stop_recording()

#take a live
#camera.start_preview(fullscreen = False, window= (500,500,1500,1500))

image_name=[]
allimages=[]
camera.resolution=(1024,1024)
camera.start_preview(fullscreen=False, window=(300,300,1500,1500))
time.sleep(5)
for i in range(0,2,1):
	name="image"+str(i)+".jpg"
	camera.capture("image"+str(i)+".jpg")
	time.sleep(1)
	picture=cv2.imread("image"+str(i)+".jpg")
	print("image shape", picture.shape)
	allimages.append(picture)
	image_name.append(name)
print(allimages)
print(len(image_name))
print(image_name)

for i  in  range(len(image_name)-1):
	while len(image_name)>5:
		print(image_name[i])
		os.remove(image_name[i])
		image_name.remove(image_name[i])
		print(image_name)
print(image_name)
