import cv2
import numpy as np
def zlicz_monety():
    img = cv2.imread("monety.jpg")
    img_blur = cv2.medianBlur(img, 5)
    gray_img = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray_img, 
                               cv2.HOUGH_GRADIENT, 
                               dp=1, 
                               minDist=150, 
                               param1=30,
                               param2=30,
                                minRadius=40,
                                maxRadius=100
                               )
    circles = np.uint16(np.around(circles))
    counter = 0
    print(f"Na zdjeciu jest {len(circles[0, :])} okregow")
    for i in circles[0, :]:
        x, y, r = i[0], i[1], i[2]
        cv2.circle(gray_img, (x,y), r, (0, 0 ,255), 3)
        
    cv2.imshow("monety", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
zlicz_monety()
