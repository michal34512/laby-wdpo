import cv2
import numpy as np

def replace_colors_by_click(image_path, tolerance):
    # Globalne zmienne
    points = []
    colors = []

    def mouse_callback(event, x, y, flags, param):
        nonlocal points, colors, image

        if event == cv2.EVENT_LBUTTONDOWN:
            # Zapisz współrzędne klikniętego punktu
            points.append((x, y))
            # Pobierz kolor klikniętego piksela
            color = image[y, x]
            colors.append(color.tolist())
            print(f"Wybrano punkt: {x, y} o kolorze: {color}")

            # Rysowanie punktu na obrazie
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("Image", image)

            # Jeśli zaznaczono dwa punkty, rozpocznij zamianę kolorów
            if len(points) == 2:
                replace_colors()

    def replace_colors():
        nonlocal new_img, colors
        print(f"{colors[0]}")
        color_1 = np.array(colors[0], dtype=np.uint8)
        color_2 = np.array(colors[1], dtype=np.uint8)
        print(f"Zamieniam kolor {color_1} na {color_2}...")

        # Tworzenie maski dla koloru punktu 1
        # Tworzenie zakresów dla koloru 1 z tolerancją
        lower_bound = np.clip(color_1 - tolerance, 0, 255)
        upper_bound = np.clip(color_1 + tolerance, 0, 255)

        mask = cv2.inRange(new_img, lower_bound, upper_bound)
        new_img[mask == 255] = color_2

        # Wyświetlenie przetworzonego obrazu
        cv2.imshow("Processed Image", new_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Wczytaj obraz
    image = cv2.imread(image_path)
    new_img = np.copy(image)

    # Wyświetl obraz i czekaj na kliknięcia użytkownika
    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mouse_callback)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
replace_colors_by_click("zamiana_kolorow.jpg", 10)