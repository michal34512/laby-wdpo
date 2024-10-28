import cv2
import numpy as np

points = []
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(gallery_img, (x, y), 2, (0, 0, 255), -1)
        cv2.imshow('Select Points', gallery_img)
        
        if len(points) == 4:
            paste_pub()

def paste_pub():
    src_points = np.array([[0, 0], [mops_width, 0], [mops_width, mops_height], [0, mops_height]], dtype=np.float32)
    dst_points = np.array(points, dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    transformed_img = cv2.warpPerspective(mops_img, matrix, (gallery_width, gallery_height))
    transformed_gray = cv2.cvtColor(transformed_img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(transformed_gray, 1, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(gallery_img, gallery_img, mask=mask_inv)
    img2_fg = cv2.bitwise_and(transformed_img, transformed_img, mask=mask)
    result = cv2.add(img1_bg, img2_fg)
    cv2.imshow('Final Image', result)

gallery_img = cv2.imread('gallery.png')
gallery_height, gallery_width = gallery_img.shape[:2] 
mops_img = cv2.imread('pug.png')
mops_height, mops_width = mops_img.shape[:2]

cv2.imshow('Select Points', gallery_img)
cv2.setMouseCallback('Select Points', select_points)

cv2.waitKey(0)
cv2.destroyAllWindows()
