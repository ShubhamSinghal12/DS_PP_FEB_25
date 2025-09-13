from keras.models import load_model
import cv2

model = load_model('mnist.h5')

def predictDigit(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img,(28,28))
    img = (img/255.0).reshape((1,28,28,1))
    pred = model.predict(img).argmax(axis = 1)
    return str(pred[0])


if __name__ == "__main__":
    print(predictDigit('digit.png'))