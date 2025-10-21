import cv2  


### 1. convert color image to grayscale

# img = cv2.imread("resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# print(img.shape)        # prints the dimensions of the color image (height, width, channels)
# print(img_gray.shape)  # prints the dimensions of the grayscale image (height, width)

# cv2.imshow("Original Image", img)
# cv2.imshow("Grayscale Image", img_gray)
# cv2.waitKey(0)


### 2. Convert to blur image


# img = cv2.imread("resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)

# print(img.shape)        # prints the dimensions of the color image (height, width, channels)
# print(img_gray.shape)  # prints the dimensions of the grayscale image (height, width)
# print(img_blur.shape)  # prints the dimensions of the blurred image (height, width)

# cv2.imshow("Original Image", img)
# cv2.imshow("Grayscale Image", img_gray)
# cv2.imshow("Blurred Image", img_blur)
# cv2.waitKey(0)



### 3. Convert to canny image


img = cv2.imread("resources/lena.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
img_canny = cv2.Canny(img_blur, 100, 100)

print(img.shape)        # prints the dimensions of the color image (height, width, channels)
print(img_gray.shape)  # prints the dimensions of the grayscale image (height, width)
print(img_blur.shape)  # prints the dimensions of the blurred image (height, width)
print(img_canny.shape)  # prints the dimensions of the canny image (height, width)

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", img_gray)
cv2.imshow("Blurred Image", img_blur)
cv2.imshow("Canny Image", img_canny)
cv2.waitKey(0)
