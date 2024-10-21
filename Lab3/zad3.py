import cv2
import numpy as np

def make_every_third_pixel_white():
    img = cv2.imread('obraz.jpeg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow("obraz", img)
    iterator = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            iterator  = (iterator + 1 ) % 3
            if(iterator == 0):
                img[i,j] = 255
    cv2.imshow("obraz 2", img)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()

def myBlur(img):
    for x in range(1, img.shape[0] - 2):
        for y in range(1, img.shape[1]  - 2):
            sum = 0. 
            for kerx in range(-1, 2):
                for kery in range(-1, 2):
                    sum += img[x + kerx, y + kery]
            img[x, y] = sum / 9.
def blurred_img():
    img = cv2.imread('obraz.jpeg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow("normal", img)
    myBlur(img)
    cv2.imshow("blur", img)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()
def main():
    blurred_img()
    
if __name__ == "__main__":
    main()
