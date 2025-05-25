import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

face_data = []
name = input("Enter the name of the Person: ")
count = 0

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
    if len(faces) == 0:
        continue
    
    face = sorted(faces,key = lambda f: f[2]*f[3])[-1]
    x,y,w,h = face
    offset = 10
    face_img = frame[y-offset:y+h+offset, x-offset:x+w+offset]
    face_img = cv2.resize(face_img,(100,100))
    cv2.imshow('Face Image',face_img)
    
    if count%10 == 0:
        face_data.append(face_img)
    count += 1
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

face_data = np.array(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

# Save this data into file system
np.save('./data/'+name+'.npy',face_data)
print("Data Successfully saved")


cap.release()
cv2.destroyAllWindows()














