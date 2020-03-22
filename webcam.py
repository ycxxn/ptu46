import cv2

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    cv2.imshow("wabcam",frame)

    cv2.waitKey(30)

cap.release()
cv2.destroyAllWindows()