import cv2

img = cv2.imread("hi/dog2.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

h,w = img.shape

#print(f"w is : {w} h is : {h} c is : {c}")
image = cv2.imread("01.jpg")
image2 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(image2[0][0])