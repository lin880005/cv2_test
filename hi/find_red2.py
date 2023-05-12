import cv2
import numpy as np


img = cv2.imread("02.png")
cv2.imshow("before",img)
img = cv2.medianBlur(img,5)
cv2.imshow("after",img)
hueImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lowRange = np.array([0, 123, 100])
highRange = np.array([6, 255, 255])
# 網路上的人認為是紅色的區域

mask = cv2.inRange(hueImage, lowRange, highRange)

mask = cv2.medianBlur(mask,3)

#RETR_EXTERNAL 只取最外層的輪廓
#RETR_LIST     取所有的輪廓
#CHAIN_APPROX_SIMPLE  儲存所有輪廓點
#CHAIN_APPROX_SIMPLE  每一個方向只取一的點，四邊形只有四個點
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 獲得contours, 以及輪廓在第幾層(hierarchy, 通常不用)
count = 0
for cnt in contours:
   
    (x,y,w,h) = cv2.boundingRect(cnt) #輪廓的四個點
    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
    catch = int(x+w/2),int(y+h/2)
    cv2.circle(img,catch,2,(255,100,0),-1)
    print(cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2))
    count +=1
cv2.imshow('result', img)
cv2.waitKey(0)

print(count)