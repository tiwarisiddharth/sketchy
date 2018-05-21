import cv2
import numpy
cap=cv2.VideoCapture(0)
while(True):
    res,cam=cap.read()
    cam=cv2.resize(cam,(0,0),fx=1,fy=1)
    gry=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
#    blur=cv2.GaussianBlur(gry,(21,21),0)
#    blur[2]=cv2.bilateralFilter(gry,10,20,20)
    blur=cv2.medianBlur(gry,3)
    #blur=('cv2.GaussianBlur(gry,(21,21),0)','cv2.bilateralFilter(gry,10,20,20)','cv2.medianBlur(gry,3)')

#    blur=cv2.bilateralFilter(gry,10,10,10)
#    x=input('Well,i know 3 methods of blurring :- 1)Gaussian  2)bilateralFilater 3)medianBlur')
#   for i in x:
#    blur=cv2.bilateralFilter(gry,30,50,60)


#    print('Well,i know 2 methods of edge detecction :- 1)Canny 2)Laplacian')



    can=cv2.Laplacian(blur,cv2.CV_64F)
#    can=cv2.Canny(blur,20,10)
    i,can=cv2.threshold(can,150,255,cv2.THRESH_TRUNC)
    cv2.imshow('w',can)
    ch=cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
