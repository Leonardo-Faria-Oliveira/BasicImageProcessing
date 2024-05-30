import sys
import cv2 as cv


def rgb_to_gray(img):

    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    

def gray_to_binary(img):

    img_gray = rgb_to_gray(img)

    _, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
    cv.imshow('Imagem preto e branco', img_binary)
    cv.waitKey(0)


def change_to_binary(img):

    img_gray = rgb_to_gray(img)

    x = img_gray.shape[0]
    y = img_gray.shape[1]

    for i in range(x):
        for j in range(y):
            if img_gray[i, j] > 127:
                img_gray[i, j] = 255
            else:
                img_gray[i, j] = 0

    img_binary = img_gray
    cv.imshow('Imagem preto e branco', img_binary)
    cv.waitKey(0)
    

def main():

    if len(sys.argv) < 2:
        print('Argumentos insuficientes')
        sys.exit()

    img_path = sys.argv[1]
    img = cv.imread(img_path)

    cv.imshow('Imagem Original', img)

    gray_to_binary(img)

main()