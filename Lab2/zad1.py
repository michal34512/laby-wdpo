import cv2
import numpy as np

def empty_callback(value):
    pass

def main():
    img = cv2.imread('obraz.jpeg')
    cv2.namedWindow('image')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.createTrackbar('Thresholding', 'image', 127, 255, empty_callback)
    cv2.createTrackbar('0 : Simple \n1 : Adaptive : 2\n Adaptive + gauss', 'image', 0, 2, empty_callback)
    cv2.createTrackbar('Adaptive -C', 'image', 0, 100, empty_callback)
    while True:
        threshold_value = cv2.getTrackbarPos('Thresholding', 'image')
        adaptive_switch = cv2.getTrackbarPos('0 : Simple \n1 : Adaptive : 2\n Adaptive + gauss', 'image')
        adaptive_C = cv2.getTrackbarPos('Adaptive -C', 'image')

        if adaptive_switch == 0:
            _, thresh_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)
        elif adaptive_switch == 1:
            thresh_img = cv2.adaptiveThreshold(gray_img, 255,
                                               cv2.ADAPTIVE_THRESH_MEAN_C,
                                               cv2.THRESH_BINARY, 11, adaptive_C)
        else:
            thresh_img = cv2.adaptiveThreshold(gray_img, 255,
                                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                               cv2.THRESH_BINARY, 11, adaptive_C)
        cv2.imshow('image', thresh_img)

        key_code = cv2.waitKey(10)
        if key_code == 27:  # Naciśnij Esc, aby zakończyć
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
