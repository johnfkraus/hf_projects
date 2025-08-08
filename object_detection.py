import cv2
 
stream = cv2.VideoCapture(0)

while(True):
    (grabbed, frame) = stream.read()
    
    cv2.imshow("Image", frame)

    key = cv2.waitKey(1) & 0xFF    
    if key == ord("q"):
        break

stream.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
show the frame
