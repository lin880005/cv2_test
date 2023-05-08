import cv2


"""
img = cv2.imread("cv.jpg")
cv2.imshow("win",img)

center = (180,160)
radius = 10
color = (0,0,0)

newImg = cv2.circle(img,center,radius,color,10)

cv2.imshow("win",newImg)
cv2.waitKey(0)
"""

def show_circle(center,color,):
    circle1 = cv2.imread("1-0.jpg")
    circle2 = circle1.copy()
    radius = 10
    thickness = 2
    
    circle1 = cv2.circle(circle1,center,radius,color,thickness)
    cv2.imshow("win",circle1)
    cv2.imshow("win2",circle2)
    cv2.waitKey(0)

center = (200,150)
color = (70,10,10)
show_circle(center,color)
show_circle((300,300),(99,6,7))








    



