import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

# Open the web cam
cap = cv2.VideoCapture(0)
# Set the video frame. 3 is for width and 4 is for height
cap.set(3, 640)
cap.set(4, 480)
# Increase the frame rate
cap.set(cv2.CAP_PROP_FPS, 100)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
# adding the images from file
# imBg = cv2.imread("images/1.jpg")

listImg = os.listdir("images")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 1

# Display
while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)


    # Stack the images side by side)
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    # Displaying the frame rate
    _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))
    print(indexImg)
    cv2.imshow("image", imgStacked)
    key = cv2.waitKey(0)
    if key == ord('a'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('d'):
        if indexImg <len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        break

