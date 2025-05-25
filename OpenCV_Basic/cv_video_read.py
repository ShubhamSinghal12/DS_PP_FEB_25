import cv2

cap = cv2.VideoCapture(0)


while True:
    ret,frame = cap.read()
    
    if ret == False:
        continue
    
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video Capture',frame)
    cv2.imshow('Gray Video Capture',gray_frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()














# import cv2

# cap = cv2.VideoCapture(0)

# while True:

#     ret,frame = cap.read()
#     gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     if ret == False:
#         continue

#     cv2.imshow("Video Capture",frame)
#     cv2.imshow("Gray Video",gray_frame)

#     key_pressed = cv2.waitKey(1)
#     if key_pressed == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()