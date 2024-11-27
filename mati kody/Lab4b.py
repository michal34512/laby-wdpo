import cv2
import numpy as np



def mouseCallback(event, x, y, flags,  userdata):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(obraz,(x,y),30,(0,0,255),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(obraz,(x-15,y-15),(x+15,y+15),(255,0,0),-1)
    pass

obraz = np.zeros((800,800,3),np.uint8)
cv2.namedWindow('okienko')
cv2.setMouseCallback('okienko',mouseCallback)

while True:
    key = cv2.waitKey(10)
    if key == 27:
        break
    cv2.imshow('okienko',obraz)

cv2.destroyAllWindows()