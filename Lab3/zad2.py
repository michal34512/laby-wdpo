import cv2
import numpy as np

def trackbar_value_changed(value, winName, img):
    match winName:
        case "erode":
            img_blur = cv2.blur(img, (value, value))
            cv2.imshow(winName, img_blur)
        case "dilate":
            img_blur = cv2.GaussianBlur(img, (value, value), 0)
            cv2.imshow(winName, img_blur)

def main():
    img = cv2.imread('obraz.jpeg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)
    _, thresh_img = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
    cv2.erode
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
