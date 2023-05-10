import cv2
import random

a = [[123,34,57,62,"cat"],[12,85,145,32,"dog"]]

img = cv2.imread("cv.jpg")

def show_result(img,a):
    for i in a:
        color_random = random.randint(0,255)
        img = cv2.imread("cv.jpg")
        point1 = (i[0],i[1])
        point2 = (i[2],i[3])
        color = (color_random,color_random,color_random)
        thickness = 2

        cv2.rectangle(img,point1,point2,color,thickness)
        cv2.imshow("win",img)
        cv2.waitKey(0)

show_result(img,a)