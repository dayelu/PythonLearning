from PIL import Image
import pytesseract

img_obj = Image.open('test.jpg')
#lang = 'eng+chi_sim'
text = pytesseract.image_to_string(img_obj,lang='eng')

print(text)
