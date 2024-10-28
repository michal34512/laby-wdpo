import cv2
import numpy as np

points = []
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(original_img, (x, y), 2, (0, 0, 255), -1) # thickess -1 sprawia, że nie koło jest całe w jednym kolorze
        cv2.imshow('Select Points', original_img)
        
        if len(points) == 4:
            transform_perspective()

def transform_perspective():
    src_points = np.array(points, dtype=np.float32)
    print(src_points)
    dst_points = np.array([[0, 0], [img_width, 0], [img_width, img_height], [0, img_height]], dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    print(matrix)
    transformed_img = cv2.warpPerspective(img_copy, matrix, (img_width, img_height))
    cv2.imshow('Transformed Image', transformed_img)

original_img = cv2.imread('road.jpg')  
original_height, original_width = original_img.shape[:2] 
width = int(original_width * 0.5)
height = int(original_height * 0.5)
original_img = cv2.resize(original_img, (width, height), interpolation=cv2.INTER_AREA)
img_height, img_width = original_img.shape[:2] 
img_copy = original_img.copy()

cv2.imshow('Select Points', original_img)
cv2.setMouseCallback('Select Points', select_points)

cv2.waitKey(0)
cv2.destroyAllWindows()
