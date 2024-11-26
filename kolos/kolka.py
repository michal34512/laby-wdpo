import cv2
import numpy as np

def process_circles(image_path):
    img = cv2.imread(image_path)
    blur_img = cv2.medianBlur(img, 11)

    # Konwersja do przestrzeni kolorów HSV
    hsv = cv2.cvtColor(blur_img, cv2.COLOR_BGR2HSV)
    
    # Zakresy kolorów dla czerwonego i niebieskiego
    red_lower1 = np.array([0, 100, 100])    # Pierwszy zakres czerwonego (odcienie dookoła 0)
    red_upper1 = np.array([10, 255, 255])
    red_lower2 = np.array([160, 100, 100])  # Drugi zakres czerwonego (odcienie dookoła 180)
    red_upper2 = np.array([179, 255, 255])
    blue_lower = np.array([100, 150, 50])   # Zakres niebieskiego
    blue_upper = np.array([140, 255, 255])
    
    # Maski dla kolorów
    red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)  # Łączymy dwa zakresy czerwonego
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    
    # Detekcja konturów dla czerwonych kółek
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Liczba kółek
    red_count = 0
    blue_count = 0
    
    # Procesowanie konturów czerwonych
    for contour in red_contours:
        if cv2.contourArea(contour) > 50:  # Filtrujemy małe szumy
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            if radius > 5:  # Upewniamy się, że to kółko
                red_count += 1
                # Rysujemy niebieską obwódkę wokół czerwonego kółka
                cv2.circle(img, center, radius, (255, 0, 0), 3)  # Niebieska obwódka

    # Procesowanie konturów niebieskich
    for contour in blue_contours:
        if cv2.contourArea(contour) > 50:  # Filtrujemy małe szumy
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            if radius > 5:  # Upewniamy się, że to kółko
                blue_count += 1
                # Rysujemy czerwoną obwódkę wokół niebieskiego kółka
                cv2.circle(img, center, radius, (0, 0, 255), 3)  # Czerwona obwódka

    # Wypisanie wyników
    print(f"Liczba czerwonych kółek: {red_count}")
    print(f"Liczba niebieskich kółek: {blue_count}")

    # Wyświetlenie obrazu
    cv2.imshow("Processed Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Przykład użycia
# Podaj ścieżkę do obrazu
process_circles("circles.png")
