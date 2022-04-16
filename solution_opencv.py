import cv2

image = cv2.imread('./image.png', cv2.IMREAD_GRAYSCALE)
image_enhanced = cv2.equalizeHist(image)

cv2.imshow('input image', image)
cv2.imshow('output image', image_enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()