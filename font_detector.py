import pytesseract
from PIL import Image

#This is the path to the Tesseract executables
pytesseract.pytesseract.tesseract_cmd = r'usr/bin/tessercact'

#load the image from the file
image = Image.open('Images/receipt1.jpg')

#Perform OCR to ectract text
text = pytesseract.image_to_string(image)

font_names = ["Arial", "Times New Roman", "Verdana", "Helvetica", "Courier"]

detected_font = None
for font_name in font_names:
    if font_name.lower() in text.lower():
        detected_font = font_name
        break

if detected_font:
    print(f"Detected font family: {detected_font}")
else:
    print("Font detection failed")

