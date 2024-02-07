import cv2 as cv
from ultralytics import YOLO
import csv
from datetime import datetime
import time

# Initialize the YOLOv8 model
model = YOLO("yolov8n.pt")

# Open the CSV file and write the header
with open("Counter.csv", mode='w') as csv_file:
    fieldnames = ['Time', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

def write_csv(time , count):
    with open("Counter.csv", mode='a') as csv_file:
        fieldnames = ['Time', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Time': time, 'Count': count})

# Open the video capture
cap = cv.VideoCapture('D:\Crowd_counter\Pedestrian.mp4')

start_time = time.time()
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    if round(current_time - start_time) >= 5:
        # Detect objects in the image
        results = model.predict(frame)

        # Get the list of detected objects
        objects = results[0].boxes.data.tolist()

        for detected_object in objects:
            if detected_object[5] == 0:
                count += 1

        print("Number of bodies detected: " + str(count))
        write_csv(datetime.now(), count)

        start_time = current_time
        count = 0

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()