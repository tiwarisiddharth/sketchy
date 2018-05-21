import cv2
import numpy
cap=cv2.VideoCapture(0)
while(True):
    res,cam=cap.read()
    cam=cv2.resize(cam,(0,0),fx=1,fy=1)
    gry=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
    blur=cv2.bilateralFilter(gry,10,10,10)
    can=cv2.Canny(blur,20,10)
    i,can=cv2.threshold(can,150,255,cv2.THRESH_TRUNC)
    cv2.imshow('w',can)
    ch=cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
