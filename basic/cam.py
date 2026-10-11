import cv2
cam=cv2.VideoCapture(2)
while True:
 _,frame   =cam.read()
 cv2.imshow("frame",frame)
 if cv2.waitKey(1) & 0xFF==ord("q"):
  break