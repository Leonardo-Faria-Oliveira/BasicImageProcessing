import sys
import cv2 as cv

def rgb_to_gray(img):

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Imagem cinza', img_gray)
    cv.waitKey(0)
    

def main():

    if len(sys.argv) < 2:
        print('Argumentos insuficientes')
        sys.exit()

    img_path = sys.argv[1]
    img = cv.imread(img_path)

    cv.imshow('Imagem Original', img)

    rgb_to_gray(img)


main()