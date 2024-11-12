import cv2
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie obrazu w skali szarości
image_path = 'einstein.png'  # Podaj ścieżkę do pliku graficznego
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")
else:
    # Ustawienie obrazu jako typ float32 do precyzyjnych obliczeń
    image = np.float32(image)

    # Definicja masek Prewitta
    prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
    prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)

    # Definicja masek Sobela
    sobel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], dtype=np.float32)
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)

    # Obliczenie pochodnych cząstkowych za pomocą maski Prewitta
    prewitt_grad_x = cv2.filter2D(image, -1, prewitt_x) / 3
    prewitt_grad_y = cv2.filter2D(image, -1, prewitt_y) / 3

    # Obliczenie pochodnych cząstkowych za pomocą maski Sobela
    sobel_grad_x = cv2.filter2D(image, -1, sobel_x) / 4
    sobel_grad_y = cv2.filter2D(image, -1, sobel_y) / 4

    # Obliczenie wartości bezwzględnej gradientu dla Prewitta i Sobela
    prewitt_magnitude = cv2.magnitude(prewitt_grad_x, prewitt_grad_y)
    sobel_magnitude = cv2.magnitude(sobel_grad_x, sobel_grad_y)

    # Wyświetlenie wyników
    plt.figure(figsize=(12, 8))

    plt.subplot(332), plt.imshow(image, cmap='gray'), plt.title("Oryginalny obraz")
    plt.axis('off')

    plt.subplot(334), plt.imshow(prewitt_grad_x, cmap='gray'), plt.title("Prewitt - gradient X")
    plt.axis('off')

    plt.subplot(335), plt.imshow(prewitt_grad_y, cmap='gray'), plt.title("Prewitt - gradient Y")
    plt.axis('off')

    plt.subplot(336), plt.imshow(prewitt_magnitude, cmap='gray'), plt.title("Prewitt - Magnituda")
    plt.axis('off')

    plt.subplot(337), plt.imshow(sobel_grad_x, cmap='gray'), plt.title("Sobel - gradient X")
    plt.axis('off')

    plt.subplot(338), plt.imshow(sobel_grad_y, cmap='gray'), plt.title("Sobel - gradient Y")
    plt.axis('off')

    plt.subplot(339), plt.imshow(sobel_magnitude, cmap='gray'), plt.title("Sobel - Magnituda")
    plt.axis('off')


    plt.tight_layout()
    plt.show()
