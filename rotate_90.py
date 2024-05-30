import sys
import cv2 as cv

def rotate_90(img):

    img_rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    cv.imshow('Imagem girada a 90 graus', img_rotated)
    cv.waitKey(0)


def main():

    if len(sys.argv) < 2:
        print('Argumentos insuficientes')
        sys.exit()

    img_path = sys.argv[1]
    img = cv.imread(img_path)

    cv.imshow('Imagem Original', img)

    rotate_90(img)

main()