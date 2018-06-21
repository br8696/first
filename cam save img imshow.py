import cv2
from time import sleep as a
while True:
    cam=cv2.VideoCapture(0)
    img=cam.read()[1]
    cv2.imshow("name.jpeg",img)
    if cv2.waitKey(10)==ord('q'):
        break
    cam.release()
    a(.02)
