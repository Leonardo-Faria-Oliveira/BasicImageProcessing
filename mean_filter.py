import sys
import cv2 as cv
import numpy as np

def rgb_to_gray(img):

    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    

def mean_filter(img):

    img_gray = rgb_to_gray(img)
    x = img_gray.shape[0]
    y = img_gray.shape[1]

    for i in range(1, x - 1):
        for j in range(1, y - 1):
            img_gray[i, j] = np.mean(img_gray[i-1:i+2, j-1:j+2])

    img_mean = img_gray
    cv.imshow('Imagem com filtro da media aplicado', img_mean)
    cv.waitKey(0)
    

def main():

    if len(sys.argv) < 2:
        print('Argumentos insuficientes')
        sys.exit()

    img_path = sys.argv[1]
    img = cv.imread(img_path)

    cv.imshow('Imagem Original', img)

    mean_filter(img)

main()