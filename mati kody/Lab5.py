import numpy as np
import cv2

def empty_callback(value):
    pass

def zad1():

    img = cv2.imread("budynek.jpg",cv2.IMREAD_GRAYSCALE)
    img = img / 255
    Mxkernel = np.matrix([[1,0,-1],[2,0,-2],[1,0,-1]])
    Mykernel = Mxkernel.T
    img_mx = cv2.filter2D(img,-1,Mxkernel)/4
    img_my = cv2.filter2D(img,-1,Mykernel)/4
    gradient = np.sqrt(img_mx**2 + img_my**2)

    while True:
        cv2.imshow('okno',img)
        cv2.imshow('Mxkernel',np.abs(img_mx))
        cv2.imshow('Mykernel', np.abs(img_my))
        cv2.imshow('Gradient',gradient)

        cv2.waitKey(20)

def zad2():
    img = img = cv2.imread("samolot.jpg")
    cv2.namedWindow('okno')
    cv2.createTrackbar('UT','okno',100,255,empty_callback)
    cv2.createTrackbar('LT', 'okno', 200, 255, empty_callback)

    while True:
        ut = cv2.getTrackbarPos('UT','okno')
        lt = cv2.getTrackbarPos('LT', 'okno')
        img_canny = cv2.Canny(img,lt,ut,L2gradient=True)
        cv2.imshow('okno',img_canny)
        cv2.waitKey(20)

def zad3():
    img = cv2.imread('shapes.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 150, 200, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    while True:
        cv2.imshow('okno',img)
        key = cv2.waitKey(20)
        if key == 27:
            break

def zaddod1():
    img = img = cv2.imread("drone_ship.jpg")
    cv2.namedWindow('okno')

    while True:
        img_canny = cv2.Canny(img, 412, 891, L2gradient=True)
        cv2.imshow('okno', img_canny)
        key = cv2.waitKey(20)
        if key == 27:
            break

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Jeśli lewy przycisk myszy został naciśnięty
        pixel = param[y, x]  # Pobieramy wartość piksela w miejscu kliknięcia
        print(f"Kliknięto piksel na współrzędnych ({x}, {y}), wartość: {pixel}")


def zaddod2():
    # Wczytanie obrazu
    img = cv2.imread("fruit.jpg")
    img_blur = cv2.medianBlur(img, 5)  # Zastosowanie medianowego rozmycia, aby wygładzić obraz
    gray_img = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    # Wykrywanie okręgów za pomocą HoughCircles
    circles = cv2.HoughCircles(
        gray_img,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=20,
        param2=40,
        minRadius=120,
        maxRadius=200
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            x, y, r = i[0], i[1], i[2]

            # Wytnij fragment obrazu w obrębie okręgu
            circle_roi = img[y - r:y + r, x - r:x + r]
            if circle_roi.size == 0:  # Sprawdź, czy fragment nie jest pusty
                continue

            # Konwersja do HSV dla analizy koloru
            circle_hsv = cv2.cvtColor(circle_roi, cv2.COLOR_BGR2HSV)

            # Oblicz średni kolor w okręgu
            avg_color = cv2.mean(circle_hsv)[:3]  # (Hue, Saturation, Value)

            # Sprawdzenie zakresów kolorów dla pomarańczy i jabłek
            if 10 < avg_color[0] < 25:  # Pomarańczowe (Hue w zakresie pomarańczowym)
                cv2.circle(img, (x, y), r, (255, 0, 0), 3)  # Pomarańczowa obwódka
            elif 35 < avg_color[0] < 85:  # Zielone (Hue w zakresie zielonym)
                cv2.circle(img, (x, y), r, (0, 0, 255), 3)  # Zielona obwódka

    # Wyświetlenie obrazu z oznaczeniami
    cv2.imshow("Fruits Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zaddod3():
    img = cv2.imread("coins.jpg")
    img_blur = cv2.medianBlur(img, 5)
    gray_img = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(
        gray_img,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=30,
        param2=50,
        minRadius=40,
        maxRadius=100
    )

    circles = np.uint16(np.around(circles))
    counter = 0
    for i in circles[0, :]:
        x, y, r = i[0], i[1], i[2]
        cv2.circle(gray_img,(x,y),r,(0,0,255),3)
        if 40<r<60:
            counter=counter+0.1
        elif 80<r<110:
            counter=counter+1


    print(f'Na zdjeciu znajduje sie {counter:.1f}0 zlotych')
    cv2.imshow("coins", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

zaddod1()