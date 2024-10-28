import cv2
import numpy as np
from matplotlib import pyplot as plt

# Generowanie przykładowego obrazu (losowy obraz 256x256 z wartościami 0-255)
image = cv2.imread('road.jpg')  

# Konwersja obrazu na skalę szarości
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 1. Wyświetlenie histogramu dla obrazu kolorowego

# Ustawienia wykresu
colors = ('b', 'g', 'r')
plt.figure(figsize=(12, 6))
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.title("Histogram dla obrazu kolorowego")
plt.xlabel("Wartość pikseli")
plt.ylabel("Liczba pikseli")
plt.show()

# 2. Histogram dla obrazu w skali szarości
hist_gray = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
plt.figure(figsize=(6, 6))
plt.plot(hist_gray, color='black')
plt.title("Histogram dla obrazu w skali szarości")
plt.xlabel("Wartość pikseli")
plt.ylabel("Liczba pikseli")
plt.show()

# 3. Wyrównanie histogramu za pomocą CLAHE

# Tworzenie obiektu CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Zastosowanie CLAHE na obrazie w skali szarości
clahe_gray = clahe.apply(gray_image)

# Wyświetlenie wynikowego obrazu i jego histogramu po CLAHE
hist_clahe_gray = cv2.calcHist([clahe_gray], [0], None, [256], [0, 256])

# Wyświetlenie histogramów i obrazu po CLAHE
plt.figure(figsize=(12, 6))

# Histogram po wyrównaniu CLAHE
plt.subplot(1, 2, 1)
plt.plot(hist_clahe_gray, color='black')
plt.title("Histogram dla obrazu w skali szarości po CLAHE")
plt.xlabel("Wartość pikseli")
plt.ylabel("Liczba pikseli")

# Wyświetlenie obrazu po wyrównaniu histogramu
plt.subplot(1, 2, 2)
plt.imshow(clahe_gray, cmap='gray')
plt.title("Obraz po wyrównaniu histogramu (CLAHE)")
plt.axis('off')

plt.show()
