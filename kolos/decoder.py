import cv2
import numpy as np

def decode_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    decoded_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] % 2 == 1:
                decoded_image[i, j] = 255
            else:
                decoded_image[i, j] = 0

    cv2.imshow("Original Image", image)
    cv2.imshow("Decoded Image", decoded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

decode_image("decoder.png")
