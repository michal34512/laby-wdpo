import cv2
import numpy as np

def select_and_process_image(image_path):
    img = cv2.imread(image_path)
    
    points = []
    def select_points(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN: 
            points.append((x, y))
            cv2.circle(temp_img, (x, y), 2, (0, 0, 255), -1)
            cv2.imshow("Select Points", temp_img)

            if(len(points) == 2):
                cv2.destroyAllWindows()

    temp_img = img.copy()
    
    cv2.imshow("Select Points", temp_img)
    cv2.setMouseCallback("Select Points", select_points)
    
    cv2.waitKey(0)
    

    x1, y1 = points[0]
    x2, y2 = points[1]
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    
    cropped = img[y_min:y_max, x_min:x_max]
    
    enlarged = cv2.resize(cropped, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
    sharpen_kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
    
    sharpened = cv2.filter2D(enlarged, -1, sharpen_kernel)
    
    sharpened = np.clip(sharpened, 0, 255)


    cv2.imshow("Processed Fragment", sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Przykład użycia
select_and_process_image("sheep.jpg")
