# Python program to convert a image into a pdf
# using img2pdf library
# importing necessary libraries
import img2pdf 
from PIL import Image
import os
# storing image path
img_path = "pic.png"
 # storing pdf path
pdf_path = "pic.pdf"
# opening image 
image = Image.open(img_path)
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
# opening or creating pdf file
with open(pdf_path, "wb") as f:
# writing pdf files with chunks
    f.write(pdf_bytes)
# closing image file
image.close()
# output
print("Successfully made pdf file")