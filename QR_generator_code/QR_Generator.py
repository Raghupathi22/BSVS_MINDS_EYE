# This program wil be with the manufacturer and used to create the QR Sticker

import datetime
import QR
from PIL import Image

seed_name = input("Enter the seed name: ")
date_time = str(datetime.datetime.now())
loc = input("Enter the location: ")
price = input("Enter the price: ")
mfc = date_time[:10]
exp_date = "90"

text = seed_name+" "+date_time+" "+loc+" "+price+" "+mfc+" "+exp_date
file_name = seed_name+date_time[-6:-1]

QR.qr_gen(text, file_name, 9)
img = Image.open(file_name+".png")
img.show()





