import cv2
import numpy as np

# Globalne zmienne
points = []
target_img = cv2.imread("gallery.png")  # Obraz docelowy
source_img = cv2.imread("pug.png")  # Obraz do wklejenia

def select_points(event, x, y, flags, param):
    global points, target_img, source_img
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 4:
            # Po zaznaczeniu czterech punktów wykonaj dopasowanie i wklejanie
            warp_and_paste()

def warp_and_paste():
    global points, target_img, source_img

    # Punkty obrazu źródłowego
    h, w, _ = source_img.shape
    src_points = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)

    # Punkty obrazu docelowego (wybrane przez użytkownika)
    dst_points = np.array(points, dtype=np.float32)

    # Obliczenie macierzy perspektywy
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Przekształcenie obrazu źródłowego
    warped_img = cv2.warpPerspective(source_img, matrix, (target_img.shape[1], target_img.shape[0]))

    # Maska do wklejania
    mask = np.zeros_like(target_img, dtype=np.uint8)
    cv2.fillPoly(mask, [np.int32(dst_points)], (255, 255, 255))
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # Nałożenie obrazu z maską
    inverted_mask = cv2.bitwise_not(mask)
    target_img_bg = cv2.bitwise_and(target_img, target_img, mask=inverted_mask)
    warped_img_fg = cv2.bitwise_and(warped_img, warped_img, mask=mask)
    combined_img = cv2.add(target_img_bg, warped_img_fg)

    # Wyświetlenie wynikowego obrazu
    cv2.imshow("Result", combined_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    global target_img, source_img

    # Wczytanie obrazów


    if target_img is None or source_img is None:
        print("Nie udało się wczytać obrazów.")
        return

    # Wyświetlenie obrazu docelowego i przypisanie funkcji obsługi myszy
    cv2.imshow("Select Points", target_img)
    cv2.setMouseCallback("Select Points", select_points)

    # Czekanie na zamknięcie okna
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()