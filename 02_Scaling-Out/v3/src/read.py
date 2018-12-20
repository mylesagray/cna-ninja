import os

# Import mongoengine libraries
from mongoengine import connect

# Import libraries for base64 encoding for DB
import base64
from io import BytesIO

# Connect to MongoDB database
connect('qrsite')

# Import our database models
from models import QRCode

# Assign user record to variable
qr = QRCode.objects.first()

# Convert image from b64 to png
img_bytes = base64.b64decode(qr.content.decode())

# Set the name of the output directory for the QRCode
directory = "output"

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Save QR to dir
f = open(directory+"/"+qr.title+".png", 'wb')
f.write(img_bytes)
f.close()
