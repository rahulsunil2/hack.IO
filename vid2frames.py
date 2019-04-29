import cv2 
import os

count = 0
pathList = os.listdir()
pathList = [i for i in pathList if i[-5:] == ".h264"]
for path in pathList:
    print(path)
    vidObj = cv2.VideoCapture(path) 
    success = 1
    while success:
        success, image = vidObj.read() 
        cv2.imwrite("frame%d.jpg" % count, image)
        count += 1