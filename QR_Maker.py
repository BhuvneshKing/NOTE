import pyqrcode
x="https://github.dev/BhuvneshKing/entire_life"
url = pyqrcode.create(x)
# the QR code will be save in the form of "QRcode.svg"
url.svg("QRcode.svg",scale=8)