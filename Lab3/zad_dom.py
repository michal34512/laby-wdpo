import time
import cv2
import numpy as np
from pykuwahara import kuwahara


def kuwahara_filter(image, r=2):
    # Rozmiar okna
    size = 2 * r + 1
    
    # Wymiary obrazu
    h, w, channels = image.shape
    
    # Inicjalizacja obrazu wyjściowego
    output = np.zeros_like(image)
    
    # Przetwarzanie piksel po pikselu
    for y in range(r, h - r):
        for x in range(r, w - r):
            for c in range(0, channels):
                # Wyodrębnienie okna o wymiarach (size x size)
                window = image[y - r:y + r + 1, x - r:x + r + 1, c]
                
                # Podział na 4 kwadranty
                q1 = window[:r + 1, :r + 1]  # Lewy górny
                q2 = window[:r + 1, r:]      # Prawy górny
                q3 = window[r:, :r + 1]      # Lewy dolny
                q4 = window[r:, r:]          # Prawy dolny
                
                # Obliczanie średnich i wariancji dla każdego kwadrantu
                regions = [q1, q2, q3, q4]
                stats = []
                
                for region in regions:
                    mean, stddev = cv2.meanStdDev(region)
                    stats.append((mean[0][0], stddev[0][0]))  # Dodajemy średnią i odchylenie
                
                # Wybieramy region o najmniejszym odchyleniu standardowym
                best_region = min(stats, key=lambda x: x[1])
                
                # Przypisanie średniej wartości z wybranego regionu do wyjściowego piksela
                output[y, x, c] = best_region[0]
    
    return output
def kuwahara_filter_lib(img):
    return  kuwahara(img, method='mean', radius=2)
def zad_dom():
    img = cv2.imread('obraz.jpeg')
    newimg = kuwahara_filter(img)
    cv2.imshow("image", img)
    cv2.imshow("new image", newimg)
    newimglib = kuwahara_filter_lib(img)
    cv2.imshow("new image lib", newimglib)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()
    
def main():
    zad_dom()
    
if __name__ == "__main__":
    main()





