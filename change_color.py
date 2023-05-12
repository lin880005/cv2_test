import cv2

def changePicColor(num,img):
    if num == 1: #變黑白照
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        return img
    elif num == 2:#維持原樣
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        return img 
    elif num == 3:#B R對調
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        return img
    
def resualt(img,num):
    out = changePicColor(num,img)
    try:
        cv2.imwrite("reasult_pic/change_color.jpg",out)
        cv2.imshow("win",out)
        cv2.waitKey(0)
    except:
        print("輸入錯誤，請再輸入一次!!")
        num = eval(input("請輸入1,2,3其中一個數字:"))
        resualt(img,num)

img = cv2.imread("cv.jpg")
num = eval(input("請輸入1,2,3其中一個數字:"))

resualt(img,num)