# Import necessary libraries
import sys
import qrcode
import os

# Set the name of the output directory for the QRCode
directory = "output"

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create a QRCode from the input query of the application and save to disk
img = qrcode.make(sys.argv[1])
img.save(directory+"/"+sys.argv[1]+".png", "PNG")

# Output confirmation text to the CLI
print("Created QR Code for: " + sys.argv[1])
