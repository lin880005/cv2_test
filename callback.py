import cv2

def to_gray(img):
    print("to_gray")
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",img2)

def to_rgb(img):
    print("to_rgb")
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("rgb",img2)


def template(algorithm):
    print('hello')
    img = cv2.imread("cv.jpg")
    algorithm(img)
    cv2.waitKey(0)


def template1():
    print("hello")
    img = cv2.imread("cv.jpg")
    cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",img)
    cv2.waitKey(0)

def template2():
    print("hello")
    img = cv2.imread("cv.jpg")
    cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("rgb",img)
    cv2.waitKey(0)


template(to_rgb)