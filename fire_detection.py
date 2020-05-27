import cv2
import numpy as np
import datetime
import socket
import time
#video_file = "video_1.mp4"
#video_file = "../fire.mp4"
video = cv2.VideoCapture(1)
framecount = 0
while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break
 
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
    lower = [18, 150, 150]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)
    
    
 
 
    output = cv2.bitwise_and(frame, hsv, mask=mask)
    output = output * 0.5
    no_red = cv2.countNonZero(mask)
    cv2.imshow("output", output)
    cv2.imshow("origin", frame)
    #print("output:", frame)
    info = None 
    # if int(no_red) > 29000:
    if (framecount % 100) == 0:
        info = ('FireSuspect', (int(no_red) > 900), str(datetime.datetime.now()))
        string = str(info)
        print(string)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 60000))
        s.sendall(string.encode())
        s.close()
    framecount += 1
    # time.sleep(1)
    #print(int(no_red))
   #print("output:".format(mask))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
 
cv2.destroyAllWindows()
video.release()
