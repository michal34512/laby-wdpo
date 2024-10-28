import cv2
import numpy as np

# Zmienna do przechowywania współrzędnych punktów zaznaczenia
points = []

# Funkcja do obsługi kliknięć myszy
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        # Dodanie punktu po kliknięciu
        points.append((x, y))
        # Wyświetlenie zaznaczonego punktu
        cv2.circle(image, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow("Image", image)

        # Sprawdzenie, czy wybrano dwa punkty
        if len(points) == 2:
            apply_threshold()

# Funkcja do progowania wybranego obszaru na kanale zielonym
def apply_threshold():
    global image, points

    # Ustalenie wybranego obszaru
    x1, y1 = points[0]
    x2, y2 = points[1]
    roi = image[y1:y2, x1:x2]

    # Wyciągnięcie kanału G (zielonego) i zastosowanie progowania
    green_channel = roi[:, :, 1]
    _, thresholded = cv2.threshold(green_channel, 127, 255, cv2.THRESH_BINARY)

    # Wstawienie progowanego kanału z powrotem do obrazu
    roi[:, :, 1] = thresholded
    image[y1:y2, x1:x2] = roi

    # Wyświetlenie obrazu z progowaniem
    cv2.imshow("Thresholded Image", image)

# Wczytanie przykładowego obrazu
image = cv2.imread('road.jpg')  
original_height, original_width = image.shape[:2] 
width = int(original_width * 0.5)
height = int(original_height * 0.5)
image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Kopia obrazu do zaznaczenia punktów
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", select_points)

cv2.waitKey(0)
cv2.destroyAllWindows()
