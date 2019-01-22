from mongoengine import *

class QRCode(Document):
    title = StringField(max_length=120, required=True)
    content = BinaryField()
