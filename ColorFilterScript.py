import cv2
import numpy as np


## webcam Initialisation
cap = cv2.VideoCapture(0)

lower_purple = np.array([105, 0, 0])
upper_purple = np.array([135, 255, 255])


## looping conditions
while True:
     ret, frame = cap.read()


     ## converting it in HSV for easy filtering
     hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


     ## using the inrange function to capture the values
     ##only b/w upper and lower bound
     mask = cv2.inRange(hsv_img, lower_purple, upper_purple)

     ## now bitwise and with our orignal frame and the masked frame
     res = cv2.bitwise_and(frame, frame, mask = mask)

     cv2.imshow("original", frame)
     cv2.imshow("only filtered colour", res)
     if cv2.waitKey(1) == 32 :  ## 13 to be entered for the break
         break

cap.release()
cv2.destroyAllWindows()
