import cv2


img = cv2.imread("./dog.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Dog Image',img)
cv2.imshow('Gray Image',gray)

cv2.waitKey(0) # Program will stop when any key is pressed
cv2.destroyAllWindows()