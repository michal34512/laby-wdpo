import cv2
import numpy as np
import time

def empty_callback(value):
    pass

def main():
    img = cv2.imread('PUTVISION_LOGO.png')

    if img is None:
        print("Nie udało się wczytać obrazu.")
        return
    neg = 255 - img
    cv2.imshow('Negatyw', neg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
