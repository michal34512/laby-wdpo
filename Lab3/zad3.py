import time
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
    new_image = np.zeros(img.shape, dtype=np.uint8)
    for x in range(1, img.shape[0] - 2):
        for y in range(1, img.shape[1]  - 2):
            sum = 0. 
            for kerx in range(-1, 2):
                for kery in range(-1, 2):
                    sum += img[x + kerx, y + kery]
            new_image[x, y] = sum / 9.
    return new_image
def blurred_img():
    img = cv2.imread('obraz.jpeg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow("normal", img)
    img = myBlur(img)
    cv2.imshow("blur", img)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()
def compare_durations():
    img = cv2.imread('obraz.jpeg', cv2.IMREAD_GRAYSCALE)
    start_time = time.perf_counter()
    cvblur = cv2.blur(img, (3,3))
    cvtime = time.perf_counter() - start_time
    start_time = time.perf_counter()
    myblur = myBlur(img)
    mytime = time.perf_counter() - start_time
    print(f"Cv: {cvtime} My: {mytime}")
def filter2D():
    img = cv2.imread('obraz.jpeg', cv2.IMREAD_GRAYSCALE)
    start_time = time.perf_counter()
    blurred_filter2D = cv2.filter2D(img, -1, (3,3))
    cvfiltertime = time.perf_counter() - start_time
    print(f"Cvfilter: {cvfiltertime}")
    
def main():
    filter2D()
    
if __name__ == "__main__":
    main()
