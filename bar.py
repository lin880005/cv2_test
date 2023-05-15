import cv2

circleRadius = 1
def update(x):
    global circleRadius
    circleRadius = x
    print(x)

img = cv2.imread("cv.jpg")
cv2.namedWindow("win")
cv2.createTrackbar("bar","win",0,100,update)
center = (100,100)
color = (255,0,0)
thickness = 1


"""
    while cv2.waitKey(100) != 27:
        continue
"""

while True:
    x = cv2.waitKey(100)
    img2 = img.copy()
    cv2.circle(img2,center,circleRadius,color,thickness)
    cv2.imshow("win",img2)
    if x == 27:
        break 