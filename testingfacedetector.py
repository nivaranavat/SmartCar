import cv2
from face import face_detection
from camera import Camera
from servo import Servo
from pca import PCA
import time
cascade_file = "haarcascade_frontalface_default.xml"
cam = Camera(camera_index = -1)
cam.start(face_detect = True, cascade_file = cascade_file)
pca = PCA().getPCA()
servo = Servo(pca, 9)
servo.reset()
time.sleep(5)
servo.move(120)
time.sleep(5)
while True:
	faces, stop = cam.run(face_detect = True)
	if stop:
		break
	else:
		print("faces", faces)	
		#if len(faces)> 0:
			#servo.moveToLocation(faces[0][0], faces[0][1])
"""
ai=face_detection((1024,1024),"haarcascade_frontalface_default.xml")
#ai.detection("image0.jpg")
#testing=face_detection()
try:
	video_capture=cv2.VideoCapture(-1)
except:
	print( "Cam 2 is invalid")

ai.live(video_capture)
"""
