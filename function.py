import cv2
def print_1():
    print("1")

def show_image():
    img = cv2.imread("cv.jpg")
    cv2.imshow("win",img)
    cv2.waitKey(0)

def show_hello():
    print("hello")

def error():
    print("error")


def way_1():
    num = eval(input("請輸入數字:"))
    selectionList = []
    for i in range(10):
        selectionList.append(error)
    
    selectionList[1] = print_1
    selectionList[3] = show_image
    selectionList[5] = show_hello

    selectionList[num]()

try:
    way_1()
except Exception:
    print("error")