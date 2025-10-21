import cv2 

## Reading images

# img = cv2.imread("resources/lena.png")
# print(img)  # prints the dimensions of the image (height, width, channels)
# cv2.imshow("Output", img)
# cv2.waitKey(0)


## Reading videos

# cap = cv2.VideoCapture("resources/elon.mp4")

# while True:
#    success, img = cap.read()
#    cv2.imshow("Output", img)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#       break



## Reading from webcam
cap = cv2.VideoCapture(0)

cap.set(3, 640)  # Width
cap.set(4, 480)  # Height


while True:
   success, img = cap.read()
   cv2.imshow("Output", img)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

