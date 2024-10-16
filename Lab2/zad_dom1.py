import cv2
import numpy as np
import time

def empty_callback(value):
    pass

def main():
    # Wczytanie obrazu
    img = cv2.imread('qr.jpg')

    if img is None:
        print("Nie udało się wczytać obrazu.")
        return

    scale_factor = 2.75
    new_width = int(img.shape[1] * scale_factor)
    new_height = int(img.shape[0] * scale_factor)

    # Pomiar czasu dla różnych metod interpolacji
    start_time = time.perf_counter()
    resized_linear = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    linear_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    resized_nearest = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
    nearest_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    resized_area = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    area_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    resized_lanczos = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
    lanczos_time = time.perf_counter() - start_time

    # Wyświetlenie przeskalowanych obrazów
    cv2.imshow('Original', img)
    cv2.imshow('Resized - LINEAR', resized_linear)
    cv2.imshow('Resized - NEAREST', resized_nearest)
    cv2.imshow('Resized - AREA', resized_area)
    cv2.imshow('Resized - LANCZOS4', resized_lanczos)

    # Wyświetlenie czasów
    print(f"Czas przeskalowania - INTER_LINEAR: {linear_time:.6f} sekund")
    print(f"Czas przeskalowania - INTER_NEAREST: {nearest_time:.6f} sekund")
    print(f"Czas przeskalowania - INTER_AREA: {area_time:.6f} sekund")
    print(f"Czas przeskalowania - INTER_LANCZOS4: {lanczos_time:.6f} sekund")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
