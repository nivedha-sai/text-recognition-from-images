import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
image = cv2.imread("Screenshot 2024-06-12 145753.png")
img_RGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_RGB))

cv2.imshow("Input", image)
cv2.waitKey(0)