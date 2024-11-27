import cv2
import numpy as np

# Globalne zmienne
points = []
img_original = cv2.imread("zad2.jpg")
tolerance = 100  # Tolerancja koloru

def select_points(event, x, y, flags, param):
    global points, img_original
    if event == cv2.EVENT_LBUTTONDOWN:
        # Dodaj współrzędne kliknięcia do listy punktów
        points.append((x, y))
        if len(points) == 2:
            # Po zaznaczeniu dwóch punktów wykonaj zamianę kolorów
            replace_colors()

def replace_colors():
    global points, img_original, tolerance

    # Skopiowanie obrazu, aby zachować oryginał
    img = img_original.copy()

    # Pobranie kolorów pikseli dla punktów 1 i 2
    color1 = img[points[0][1], points[0][0]]  # Kolor w punkcie 1 (y, x)
    color2 = img[points[1][1], points[1][0]]  # Kolor w punkcie 2 (y, x)

    # Tworzenie maski dla pikseli podobnych do color1
    lower_bound = np.clip(color1 - tolerance, 0, 255)
    upper_bound = np.clip(color1 + tolerance, 0, 255)

    # Znalezienie pikseli w zakresie tolerancji
    mask = cv2.inRange(img, lower_bound, upper_bound)

    # Zamiana kolorów w masce
    img[mask > 0] = color2

    # Wyświetlenie wynikowego obrazu
    cv2.imshow("Result", img)

    # Resetowanie punktów
    points.clear()

def main():
    global img_original

    # Wczytanie obrazu

    if img_original is None:
        print("Nie udało się wczytać obrazu.")
        return

    # Wyświetlenie obrazu i przypisanie funkcji obsługi myszy
    cv2.imshow("Select Points", img_original)
    cv2.setMouseCallback("Select Points", select_points)

    # Czekanie na zamknięcie okna
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
