import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    
    ret, frame = cap.read()
    if ret == False:
        continue

    # gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # cv2.imshow('Gray Image',gray_img)

    faces = face_cascade.detectMultiScale(frame,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],2)

    cv2.imshow('Image',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()














