import cv2
import numpy as np

def empty(a):
    pass

def getContours(imgarg):
    #Gets all the contours in the given contour img
    contours, hierarchy = cv2.findContours(imgarg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #Iterating through each contour
    for cnt in contours:
        #Calculation of various parameters
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        corn = cv2.approxPolyDP(cnt, 0.01 * peri, True)#positions of corners as a list
        #Length of that list gives us number of corners
        lcorn = len(corn)

        if peri !=0:
            circ = area/float(peri*peri) #Calculation of circularity
        #Limit by area and number of corners
        if 150 < area < 3000 and lcorn > 4 and circ >0.02:
            cv2.drawContours(testing,cnt,-1, (255, 0, 0), 4)#Draws the contour around the pothole detected


#Rename bolt.mp4 to virat.mp4 in the below line to test the other video
potvid = cv2.VideoCapture("Resources/bolt.mp4")

#Trackbars to edit various parameters
cv2.namedWindow('Trackbars')
cv2.resizeWindow("Trackbars", 700, 500)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 200, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Canny Min", "Trackbars", 50, 100, empty)
cv2.createTrackbar("Canny Max", "Trackbars", 50, 100, empty)

while True :
    success,testing = potvid.read()  #Reads each frame of the video

    testHSV = cv2.cvtColor(testing, cv2.COLOR_BGR2HSV) #Converts colour scheme to Hue-Saturation-Value

    #Assigns values from the trackbars to the variables
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    c_min = cv2.getTrackbarPos("Canny Min", "Trackbars")
    c_max = cv2.getTrackbarPos("Canny Max", "Trackbars")

    #Masked image
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(testHSV, lower, upper)

    #Canny image
    imgcanny = cv2.Canny(mask,c_min,c_max)

    #Contours from Canny image
    imgcont = imgcanny.copy()
    getContours(imgcont)

    #Displaying all images generated
    cv2.imshow("Mask", mask)
    cv2.imshow("Canny", imgcanny)
    cv2.imshow("Contours", imgcont)
    cv2.imshow("Image", testing)

    cv2.waitKey(1)#Holds the code for 1ms

