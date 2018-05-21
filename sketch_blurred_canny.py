import cv2
import numpy
cap=cv2.VideoCapture(0)
while(True):
    res,cam=cap.read()
    cam=cv2.resize(cam,(0,0),fx=1,fy=1)
    gry=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gry,(21,21),0)
    blur=cv2.bilateralFilter(blur,10,20,20)
    blur=cv2.medianBlur(blur,3)
    can=cv2.Canny(blur,15,10)
    i,can=cv2.threshold(can,150,255,cv2.THRESH_TRUNC)
    cv2.imshow('w',can)
    ch=cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
