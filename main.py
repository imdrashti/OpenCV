import cv2
import pytesseract
import os
from os import listdir
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = ""
folder_dir = "D:\Python\extractingText"

dict = {
    "File name": '',
    "Total bill":'',
}

imgList = []
invoiceList = []

for images in os.listdir(folder_dir):

    if (images.endswith(".jpg")):
        # print(images)
        imgList.append(images)

        for iImage in imgList:
            img = cv2.imread(iImage)
            # img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # print(img.shape)
            ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

            rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(18, 18))

            dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

            contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            img2 = img.copy()
                # rect = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # cropped = img2[y:y + h, x:x + w]
            rect = cv2.rectangle(img2, (254, 1307), (380, 1355), (255, 0, 0), 3)
            cropped = img2[1307:1355, 254:380]

            # print(pytesseract.image_to_string(cropped))

            text = pytesseract.image_to_string(cropped)
        invoiceList.append(text)


dict["File name"] = imgList
dict["Total bill"] = invoiceList

df = pd.DataFrame(dict)

df.to_excel("New_Invoice_Details.xlsx")

print(df)




