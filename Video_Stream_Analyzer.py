# Import dependencies
import datetime 
import cv2 as cv


# Video stream source 
capture = cv.VideoCapture("https://10.0.0.104:8080/video")
while(True):
    # Capture the frame
    stream_status, frame = capture.read()

    # Assign the font type which will be displayed on the video
    font = cv.FONT_HERSHEY_SCRIPT_COMPLEX

    # Obtain th current date and time
    dateTime = str(datetime.datetime.now())

    # Attach the date and time in the stream
    frame = cv.putText(frame, dateTime, (10, 100), font, 1, (210, 155, 155), 4, cv.LINE_8)

    # Show the stream
    cv.imshow('stream', frame)
    
    # Stop the video stream
    if cv.waitKey(1) == ord('q'):
        break
        
capture.release()
cv.destroyAllWindows()