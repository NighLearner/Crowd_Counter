import cv2 as cv
from ultralytics import YOLO
import math

# Initialize the YOLOv8 model
model = YOLO("yolov8n.pt")

cap = cv.VideoCapture('D:\Crowd_counter\Pedestrian.mp4')
# Load the image

frameRate = cap.get(5) #frame rate

count = 0

while (cap.isOpened()):
    ret, frame = cap.read()
    frameId = cap.get(1) #current frame number
    
    cv.imshow("Object Detection", frame)

    if (ret != True):
        break
    
    if (frameId % math.floor(frameRate) == 0):
        
        # Detect objects in the image
        results = model.predict(frame)

        # Get the list of detected objects
        objects = results[0].boxes.data.tolist()

        
        for obj in objects:
            if obj[5] == 0:
                count = count + 1
            
        # print the number of bodies detected
        print("Number of bodies detected: " + str(count))
    
    count = 0
    
    if cv.waitKey(1) == ord('q'):
        break
    
# Release the video capture and close all windows
cap.release()
cv.destroyAllWindows()