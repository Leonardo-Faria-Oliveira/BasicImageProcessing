import sys
import cv2 as cv

def invert(img):

    img_inverted = cv.flip(img, 1)
    cv.imshow('Imagem invertida', img_inverted)
    cv.waitKey(0)


def main():

    if len(sys.argv) < 2:
        print('Argumentos insuficientes')
        sys.exit()

    img_path = sys.argv[1]
    img = cv.imread(img_path)

    cv.imshow('Imagem Original', img)

    invert(img)

main()