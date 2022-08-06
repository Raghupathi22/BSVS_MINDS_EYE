# this file has all the fuctions which can be used to generate and decode QR codes.

import pyqrcode
from pyqrcode import QRCode 
from pyzbar.pyzbar import decode
from PIL import Image

# to generate QR codes use the below fuction

def qr_gen(text, file_name, scale):
    qr = pyqrcode.create(text)
    qr.png(file_name+".png", scale)

# to decode the QR code use the below function

def qr_decode(img_name):
    img = Image.open(img_name)
    #img.show()
    decoded_text = decode(img)[0][0].decode("UTF-8")
    return decoded_text