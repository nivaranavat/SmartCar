import cv2
from face import face_detection
ai=face_detection((1024,1024),"haarcascade_frontalface_default.xml")
#ai.detection("image0.jpg")
#testing=face_detection()
try:
	video_capture=cv2.VideoCapture(-1)
except:
	print( "Cam 2 is invalid")

ai.live(video_capture)
