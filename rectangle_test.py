import cv2
import random

a = [[200,200,280,240,"cat"],[200,240,280,285,"dog"]]

img = cv2.imread("cv.jpg")

def draw_rectangle(i,img):
    color_random = random.randint(0,255)
    point1 = (i[0],i[1])
    point2 = (i[2],i[3])
    color = (color_random,color_random,color_random)
    thickness = 2
    cv2.rectangle(img,point1,point2,color,thickness)

def draw_text(name,num,img):
    size = 1
    color_random1 = random.randint(0,255)
    color_text =(color_random1,0,0)
    lineWidth = 1
    position = (200,190 + 40*num)
    cv2.putText(img,f"{num}.{name}",position,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,size,color_text,lineWidth)

def show_result(img,a):
    num=0
    for i in a:
        num+=1
        draw_rectangle(i,img)
        draw_text(i[4],num,img)    
    cv2.imshow("win",img)
    cv2.waitKey(0)
        
show_result(img,a)