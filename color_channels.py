import sys
import cv2 as cv

def color_channels(img):

    b, g, r = cv.split(img)
    cv.imshow('Canal Vermelho', r)
    cv.imshow('Canal Verde', g)
    cv.imshow('Canal Azul', b)
    cv.waitKey(0)


def main():

    if len(sys.argv) < 2:
        print('Argumentos insuficientes')
        sys.exit()

    img_path = sys.argv[1]
    img = cv.imread(img_path)

    cv.imshow('Imagem Original', img)

    color_channels(img)


main()