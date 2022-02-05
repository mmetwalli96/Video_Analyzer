# Import dependencies
import datetime 
import cv2 as cv


# Video stream source 
capture = cv.VideoCapture("https://10.0.0.104:8080/video")

while(True):
    # Capture the frame
    streamStatus, frame = capture.read()

    # Assign the font type which will be displayed on the video and its properties
    font = cv.FONT_HERSHEY_SCRIPT_COMPLEX   # Font Type
    fontColor = (255, 255, 255)             # Color of the font
    fontThickness = 3                       # Thickness of the font
    fontLocation = (100, 1000)              # Position of the text on the stream
    fontScale = 7                           # Scale of the font
    line = cv.LINE_8                        # Font shape adjustment

    # Obtain th current date and time
    dateTime = str(datetime.datetime.now())

    # Attach the date and time in the stream
    frame = cv.putText(frame, dateTime, fontLocation, font, fontThickness, fontColor, fontScale, line)

    # Show the stream
    cv.imshow('stream', frame)
    
    # Stop the video stream
    if cv.waitKey(1) == ord('q'):
        break
        
capture.release()
cv.destroyAllWindows()