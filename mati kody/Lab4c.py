import cv2
import numpy as np

points = []
img_original = None

def select_points(event, x, y, flags, param):
    global points, img_original
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 2:
            # Po zaznaczeniu dwóch punktów wykonaj progowanie
            process_region()

def process_region():
    global points, img_original
    if len(points) == 2:
        # Skopiowanie obrazu, aby zachować oryginał
        img = img_original.copy()

        # Pobranie współrzędnych obszaru
        x1, y1 = points[0]
        x2, y2 = points[1]

        # Wycięcie obszaru i progowanie na kanale G (zielonym)
        region = img[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
        green_channel = region[:, :, 1]
        _, thresh = cv2.threshold(green_channel, 128, 255, cv2.THRESH_BINARY)

        # Nałożenie progowania na obszar
        region[:, :, 1] = thresh

        # Wyświetlenie wyniku
        cv2.imshow("Processed Image", img)

        # Resetowanie punktów
        points = []

def main():
    global img_original

    # Wczytanie obrazu
    img_original = cv2.imread("budynek.jpg")
    if img_original is None:
        print("Nie udało się wczytać obrazu.")
        return

    # Wyświetlenie obrazu i przypisanie funkcji obsługi myszy
    cv2.imshow("Select Region", img_original)
    cv2.setMouseCallback("Select Region", select_points)

    # Czekanie na zamknięcie okna
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()