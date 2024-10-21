import cv2
import numpy as np

def trackbar_value_changed(value, winName, img):
    value = value*2 + 1
    kernel = np.ones((value, value), np.uint8)
    match winName:
        case "eroded":
            new_img = cv2.erode(img, kernel, iterations=1)
            cv2.imshow(winName, new_img)
        case "dilated":
            new_img = cv2.dilate(img, kernel, iterations=1)
            cv2.imshow(winName, new_img)

def main():
    img = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (400, 400))
    _, thresh_img = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow('image', thresh_img )
    kernel = np.ones((15, 15), np.uint8)
    eroded = cv2.erode(thresh_img, kernel, iterations=1)
    dilated  = cv2.dilate(thresh_img, kernel, iterations=1)
    cv2.imshow('eroded', eroded)
    cv2.imshow('dilated', dilated)
    cv2.createTrackbar('kernel (2n+1)', 'eroded', 2, 100, lambda value: trackbar_value_changed(value, "eroded", thresh_img))
    cv2.createTrackbar('kernel (2n+1)', 'dilated', 2, 100, lambda value: trackbar_value_changed(value, "dilated", thresh_img))
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
