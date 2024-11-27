import cv2
import numpy as np

img=cv2.imread("zad3.png",cv2.IMREAD_GRAYSCALE)

result = np.empty_like(img)
h,w = img.shape
print(img.shape)
for y in range(h):
    for x in range (w):
        result[y,x]=(img[y,x]%2)*255
cv2.imshow('okno',img)
cv2.imshow('wynik',result)
cv2.waitKey(0)