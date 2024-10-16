import cv2
import numpy as np

def empty_callback(value):
    pass

def main():
    img = cv2.imread('qr.jpg')

    if img is None:
        print("Nie udało się wczytać obrazu.")
        return

    scale_factor = 2.75
    new_width = int(img.shape[1] * scale_factor)
    new_height = int(img.shape[0] * scale_factor)

    resized_linear = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    resized_nearest = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
    resized_area = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    resized_lanczos = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow('Original', img)
    cv2.imshow('Resized - LINEAR', resized_linear)
    cv2.imshow('Resized - NEAREST', resized_nearest)
    cv2.imshow('Resized - AREA', resized_area)
    cv2.imshow('Resized - LANCZOS4', resized_lanczos)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
