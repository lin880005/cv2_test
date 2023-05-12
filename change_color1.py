import cv2



def bgr_to_rgb(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
    cv2.imshow("win",img)
    cv2.waitKey(0)

def bgr_to_gray(img):
     img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
     cv2.imshow("win",img)
     cv2.waitKey(0)

def show_origin(img):
    cv2.imshow("win",img)
    cv2.waitKey(0)
def null(img):
    return

def way_2():
    img = cv2.imread("cv.jpg")
    num = eval(input("請輸入1,2,3其中一個數字:"))
    if num == 1:
        bgr_to_rgb(img)
    elif num == 2:
        bgr_to_gray(img)
    elif num == 3:
        show_origin(img)
    else:
        print("error")

def way_3():
    img = cv2.imread("cv.jpg")
    num = eval(input("請輸入1,2,3其中一個數字:"))
    #selectionList = [bgr_to_rgb,bgr_to_gray,show_origin]
    selectionList = []
    for i in range(10):
        selectionList.append(null)
    
    selectionList[1] = bgr_to_rgb
    selectionList[2] = bgr_to_gray
    selectionList[3] = show_origin
    """
    selectionList.append(null)
    selectionList.append(bgr_to_rgb)
    selectionList.append(bgr_to_gray)
    selectionList.append(show_origin)
    """
    
    selectionList[num](img)

way_3()