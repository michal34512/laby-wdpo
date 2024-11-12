import cv2
import numpy as np

# Wczytanie obrazu
image_path = 'einstein2.png'  # Podaj ścieżkę do pliku graficznego
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,None ,  fx=0.5, fy=0.5)

if image is None:
    print("Nie udało się wczytać obrazu. Sprawdź ścieżkę.")
else:
    # Funkcja aktualizująca wynik na podstawie wartości progów z suwaków
    def update_canny(threshold1, threshold2):
        # Wykrywanie krawędzi metodą Canny’ego
        edges = cv2.Canny(image, threshold1, threshold2)
        # Wyświetlenie obrazu z krawędziami
        cv2.imshow("Krawędzie Canny", edges)

    # Inicjalizacja okna i suwaków
    cv2.namedWindow("Krawędzie Canny")
    cv2.createTrackbar("Próg dolny", "Krawędzie Canny", 50, 255, lambda v: update_canny(v, cv2.getTrackbarPos("Próg górny", "Krawędzie Canny")))
    cv2.createTrackbar("Próg górny", "Krawędzie Canny", 150, 255, lambda v: update_canny(cv2.getTrackbarPos("Próg dolny", "Krawędzie Canny"), v))

    # Pierwsze wywołanie z domyślnymi wartościami progów
    update_canny(50, 150)

    # Oczekiwanie na zamknięcie okna przez użytkownika
    cv2.waitKey(0)
    cv2.destroyAllWindows()
