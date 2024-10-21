import cv2
import numpy as np

def trackbar_value_changed(value, winName, img):
    value = value*2 + 1
    match winName:
        case "blur":
            img_blur = cv2.blur(img, (value, value))
            cv2.imshow(winName, img_blur)
        case "gauss":
            img_blur = cv2.GaussianBlur(img, (value, value), 0)
            cv2.imshow(winName, img_blur)
        case "median":
            img_blur = cv2.medianBlur(img, value)
            cv2.imshow(winName, img_blur)

def main():
    #img = cv2.imread('lenna_noise.bmp')
    img = cv2.imread('lenna_salt_and_pepper.bmp')

    cv2.imshow('image', img)
    img_blur = cv2.blur(img,(10, 10))
    img_gauss = cv2.GaussianBlur(img, (5,5), 0,) # sigma = 0 -> calculated from kernel size
    img_median = cv2.medianBlur(img, 5)

    cv2.imshow('blur', img_blur)
    cv2.imshow('gauss', img_gauss)
    cv2.imshow('median', img_median)
    cv2.createTrackbar('kernel (2n+1)', 'blur', 10, 100, lambda value: trackbar_value_changed(value, "blur", img))
    cv2.createTrackbar('kernel (2n+1)', 'gauss', 10, 100, lambda value: trackbar_value_changed(value, "gauss", img))
    cv2.createTrackbar('kernel (2n+1)', 'median', 10, 100, lambda value: trackbar_value_changed(value, "median", img))
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
