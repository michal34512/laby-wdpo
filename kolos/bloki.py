import cv2
import numpy as np

def process_image_with_blocks(image_path, block_size=5):
    gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    height, width = gray_img.shape
    
    processed_img = gray_img.copy()
    
    # Iteracja przez bloki
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = gray_img[y:y+block_size, x:x+block_size]
            
            max_val = np.max(block)
            min_val = np.min(block)
            
            diff = max_val - min_val
            
            processed_img[y:y+block_size, x:x+block_size] = diff
    
    cv2.imshow("Original Image", gray_img)
    cv2.imshow("Processed Image", processed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

process_image_with_blocks("sheep.jpg")
