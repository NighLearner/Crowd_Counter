import cv2 as cv

#importing cascade
cascade = cv.CascadeClassifier('haar_upper_body.xml')

# Initialize the video capture
cap = cv.VideoCapture('pedestrian.mp4')

while True:
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Detect the human body
    bodies = cascade.detectMultiScale(gray, 1.1, 2)
    
    # Draw the rectangle around each body
    for (x, y, w, h) in bodies:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
    # print the number of bodies detected
    print("Number of bodies detected: " + str(len(bodies)))
    
    cv.imshow("Object Detection", frame)

    if cv.waitKey(1) == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv.destroyAllWindows()

