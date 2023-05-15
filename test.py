import cv2
import numpy as np

x_pt = 0
y_pt =0
circleRadius = 1
z=0
color2 = [0,0,0]

def update_x(x):
    global x_pt
    x_pt = x
    

def update_y(y):
    global y_pt
    y_pt = y
    

def update(x):
    global circleRadius
    circleRadius = x
    
def rgb(index,z):
    color2[index] = z

img = cv2.imread("cv.jpg")
cv2.namedWindow("win")
cv2.createTrackbar("x","win",0,300,update_x)
cv2.createTrackbar("y","win",0,300,update_y)
cv2.createTrackbar("radius","win",0,100,update)
cv2.createTrackbar("B","win",0,255,lambda z : rgb(0,z))
cv2.createTrackbar("G","win",0,255,lambda z : rgb(1,z))
cv2.createTrackbar("R","win",0,255,lambda z : rgb(2,z))

thickness = 2


while True:
    img2 = img.copy()
    cv2.circle(img2,(x_pt,y_pt),circleRadius,color2,thickness)
    cv2.imshow("win",img2)
    x = cv2.waitKey(100)
    if x == 27:
        break