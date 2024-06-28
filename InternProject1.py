import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
image = cv2.imread("Screenshot 2024-06-12 145753.png")
img_RGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img_RGB))

results = pytesseract.image_to_boxes(img_RGB)
ih, iw, ic = image.shape
for box in results.splitlines():
    box = box.split(' ')
    print(box)

    x, y, w, z = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(image, (x,ih-y), (w,ih-z),(0,255,0),2)
    cv2.putText(image,box[0], (x, ih-z), cv2.FONT_HERSHEY_COMPLEX, 1 ,(255,0,0),1)

cv2.imshow("Input", image)
cv2.waitKey(0)