# import the opencv library
import cv2
import numpy as np
from matplotlib import pyplot as plt

# define a video capture object
vid = cv2.VideoCapture(0)

low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])

hsv_low = np.array([103,198,28], np.uint8)
hsv_high = np.array([118, 255, 130], np.uint8)

while(True):
    ret, frame = vid.read()
    #frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, hsv_low, hsv_high)
    blue = cv2.bitwise_and(frame, frame, mask=mask)
    
    contours, hierachy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        #print(area)
        if area > 400:
            #cv2.drawContours(frame, contour, -1, (0,255,0), 3)
            M = cv2.moments(contour)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(frame, (cx, cy), 3, (0, 255, 0), -1)
                print(cx, cy)  

    cv2.imshow('frame', frame)
    cv2.imshow('blue', blue)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
