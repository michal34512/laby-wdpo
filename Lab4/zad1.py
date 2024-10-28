import cv2
import numpy as np

# Funkcja obsługująca zdarzenia myszy
def draw_shape(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Lewy przycisk myszy
        # Rysowanie kwadratu o boku 50 pikseli
        cv2.rectangle(img, (x - 25, y - 25), (x + 25, y + 25), (255, 0, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:  # Prawy przycisk myszy
        # Rysowanie okręgu o promieniu 25 pikseli
        cv2.circle(img, (x, y), 25, (0, 255, 0), -1)

# Tworzymy białe tło obrazu
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Nazwa okna i przypisanie funkcji zdarzeń myszy
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_shape)

while True:
    # Wyświetlanie obrazu
    cv2.imshow('Image', img)
    
    # Naciśnięcie klawisza 'q' kończy działanie programu
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Zamykanie okien
cv2.destroyAllWindows()
