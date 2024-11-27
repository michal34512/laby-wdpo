import cv2
import numpy as np

def mozaika(image_path, block_size=5):
    img = cv2.imread(image_path)
    
    height, width, depth = img.shape
    
    processed_img = img.copy()
    
    # Iteracja przez bloki
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = img[y:y+block_size, x:x+block_size]
            mean = block.mean(axis=(0, 1))
            processed_img[y:y+block_size, x:x+block_size] = mean 
    cv2.imshow("Original Image", img)
    cv2.imshow("Processed Image", processed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

mozaika("sheep.jpg", 20)
