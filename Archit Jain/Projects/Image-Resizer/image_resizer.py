import cv2

image = cv2.imread('old_image.png')

cv2.imshow("old_image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

length = int(input("Enter the length of new image: "))
width = int(input("Enter the width of new image: "))

new_image = cv2.resize(image, (width, length))
cv2.imshow("Resized Image", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('resized_image.png', new_image)