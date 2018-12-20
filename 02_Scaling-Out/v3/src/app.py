# Import necessary libraries
import sys
import qrcode
import os

# Import libraries for base64 encoding for DB
import base64
from io import BytesIO

# Import mongoengine libraries
from mongoengine import connect

# Import our database models
from models import User, QRCode

# Connect to MongoDB database
connect('qrsite')

# Get user input
text = sys.argv[1]

# Create in-memory storage for image for later conversion to base64
buffered_image = BytesIO()

# Create a QRCode from the input query of the application and save to disk
img = qrcode.make(text)
img.save(buffered_image, format="PNG")
b64png = base64.b64encode(buffered_image.getvalue())

# Save generated image to mongodb
qr = QRCode(title=text)
qr.content = b64png
qr.save()

# Output confirmation text to the CLI 
print("Created QR Code for: " + text + " and stored in MongoDB.")
