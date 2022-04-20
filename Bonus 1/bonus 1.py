import cv2
import numpy as np

def empty(a):
    pass

def getContours(imgarg):
    #Gets all the contours in the given contour img
    contours, hierarchy = cv2.findContours(imgarg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # for i in range(0,360):
    #     line_mask = cv2.drawContours()
    # k = numpy.logical_and(contours, line_mask)



givimg=cv2.imread("Resources/TJunc.png")

testHSV = cv2.cvtColor(givimg, cv2.COLOR_BGR2HSV) #Converts colour scheme to Hue-Saturation-Value

#Masked image
lower = np.array([0, 0, 0])
upper = np.array([179, 179, 179])
mask = cv2.inRange(testHSV, lower, upper)

#Canny image
imgcanny = cv2.Canny(mask,50,50)

#Contours from Canny image
imgcont = imgcanny.copy()
getContours(imgcont)

#Displaying all images generated
cv2.imshow("Mask", mask)
cv2.imshow("Canny", imgcanny)
cv2.imshow("Contours", imgcont)
cv2.imshow("Image", givimg)

cv2.waitKey(5000)#Holds the code for 5s

