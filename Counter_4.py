import cv2 as cv
from ultralytics import YOLO
import math
import time
import datetime

# Initialize the YOLOv8 model
model = YOLO("yolov8n.pt")

cap = cv.VideoCapture(0)
# Load the image

#frameRate = cap.get(5) #frame rate

start_time = time.time()
count = 0

while (cap.isOpened()):
    ret, frame = cap.read()
    if (ret != True):
        break
    
    #frameId = cap.get(1) #current frame number
    
    # frameRate = cap.get(cv.CAP_PROP_FPS)
    # print(frameRate)
    cv.imshow("Object Detection", frame)
    current_time = time.time()
    
    if int(current_time - start_time) >= 5:
        
        # Detect objects in the image
        results = model.predict(frame)

        # Get the list of detected objects
        objects = results[0].boxes.data.tolist()

        
        for obj in objects:
            if obj[5] == 0:
                count = count + 1
            
        # print the number of bodies detected
        print("Number of bodies detected: " + str(count) + " at " + str(int(current_time)))
        start_time = current_time
    
    count = 0
    
    if cv.waitKey(1) == ord('q'):
        break
    
# Release the video capture and close all windows
cap.release()
cv.destroyAllWindows()