import cv2
cap=cv2.VideoCapture(2)

while cap.isOpened():
    _, frame=cap.read()
    cv2.imshow('camera',frame)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()