import cv2
import numpy as np



def mouseCallback(event, x, y, flags,  points):

    if event == cv2.EVENT_LBUTTONDOWN:

        points.append([x,y])
        print(x, y, points)

    pass

source_points = []
destination_points = np.asarray([[0,0],[800,0],[800,800],[0,800]],np.float32)


obraz=cv2.imread('budynek.jpg')
obraz = cv2.resize(obraz,None,fx=0.5,fy=0.5)
cv2.namedWindow('okienko')
cv2.namedWindow('result')
cv2.setMouseCallback('okienko',mouseCallback,source_points)

while True:
    key = cv2.waitKey(10)
    if key == 27:
        break

    cv2.imshow('okienko', obraz)
    if len(source_points) == 4:
        source_points = np.asarray(source_points,dtype=np.float32)
        M = cv2.getPerspectiveTransform(source_points,destination_points)
        result = cv2.warpPerspective(obraz,M,(800,800))
        cv2.imshow('result', result)


cv2.destroyAllWindows()