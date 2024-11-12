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

    # Obliczenie pochodnych cząstkowych za pomocą maski Prewitta
    prewitt_grad_x = cv2.filter2D(image, -1, prewitt_x) / 3
    prewitt_grad_y = cv2.filter2D(image, -1, prewitt_y) / 3

    # Obliczenie modułu gradientu
    prewitt_magnitude = np.sqrt(prewitt_grad_x**2 + prewitt_grad_y**2)

    # Przeskalowanie modułu gradientu do zakresu 0-255
    prewitt_magnitude = prewitt_magnitude / np.amax(prewitt_magnitude) * 255
    prewitt_magnitude = prewitt_magnitude.astype(np.uint8)

    # Wyświetlenie wyników
    plt.figure(figsize=(8, 4))

    plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title("Oryginalny obraz")
    plt.axis('off')

    plt.subplot(122), plt.imshow(prewitt_magnitude, cmap='gray'), plt.title("Moduł gradientu (Prewitt)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
