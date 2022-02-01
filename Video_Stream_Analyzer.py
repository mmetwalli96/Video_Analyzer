# Import dependencies
import cv2 as cv

# Video stream source 
capture = cv.VideoCapture("https://10.0.0.115:8080/video")
while(True):
    stream_status, frame = capture.read()
    cv.imshow('stream', frame)
    
    # Stop the video stream
    if cv.waitKey(1) == ord('q'):
        break
        
capture.release()
cv.destroyAllWindows()