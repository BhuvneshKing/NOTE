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
