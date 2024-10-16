import cv2
import numpy as np

def empty_callback(value):
    pass

def main():
    img1 = cv2.imread('qr.jpg')
    img2 = cv2.imread('PUTVISION_LOGO.png')

    assert img1 is not None, "file could not be read, check with os.path.exists()"
    assert img2 is not None, "file could not be read, check with os.path.exists()"
    height, width = img2.shape[:2]
    resized_img1 = cv2.resize(img1, (width, height), interpolation=cv2.INTER_LANCZOS4)
    cv2.namedWindow('image')
    cv2.createTrackbar('alpha', 'image', 50, 100, empty_callback)
    cv2.createTrackbar('beta', 'image', 50, 100, empty_callback)

    while True:
        alpha = cv2.getTrackbarPos('alpha', 'image') * 0.01
        beta = cv2.getTrackbarPos('beta', 'image') * 0.01
        dst = cv2.addWeighted(resized_img1, alpha, img2, beta, 0)

        cv2.imshow('image', dst)

        key_code = cv2.waitKey(10)
        if key_code == 27:  # Naciśnij Esc, aby zakończyć
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
