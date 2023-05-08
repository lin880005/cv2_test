
import cv2



#num = eval(input("請輸入1,2,3:"))
'''
if num == 1:
    cv2.imshow("image",img[0])
    cv2.waitKey(0)
elif num ==2:
    cv2.imshow("image",img[1])
    cv2.waitKey(0)
else:
    print("請再輸入一次")
'''
img = [cv2.imread("hi/cv.jpg"),cv2.imread("hi/dog.jpg"),cv2.imread("hi/dog1.jpg"),cv2.imread("hi/dog2.jpg"),cv2.imread("C:\\Users\\Patrick\\Desktop\\python0508\\hi\\hi2\\dog3.jpg")]
i=0
while i < len(img):
    
    cv2.imshow("image",img[i])
    cv2.waitKey(1000)
    i+=1
    
    

