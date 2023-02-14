import qrcode
from PIL import Image

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add data to the QR code
data = "https://www.example.com"
qr.add_data(data)

# Make the QR code image
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image as a PNG file
img.save("qr_code.png")


from tkinter import *
from PIL import ImageTk, Image
import os

with Image.open("qr_code.png") as img:
    width, height = img.size
    global Width,Height
    Width=(width)
    Height=(height)

root = Tk()

def delete_file_on_close():
    os.remove("qr_code.png")
    root.destroy()

img = Image.open("qr_code.png")
photo = ImageTk.PhotoImage(img)
label = Label(root, image=photo, width=Width, height=Height)
label.pack()
root.protocol("WM_DELETE_WINDOW", delete_file_on_close)
root.mainloop()
