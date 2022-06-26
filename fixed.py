import cv2

print("Printing A lovebirds...")

filePath = 'Parakeeets.jpg'
img = cv2.imread(filePath, 1)
cv2.imshow("Parakeets", img)
cv2.waitKey(0)
cv2.destroyAllWindows()