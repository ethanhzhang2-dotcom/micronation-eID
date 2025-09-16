import qrcode
import cryptography.hazamt.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#pip install cryptography
#pip install "qrcode[pil]"


private_key = rsa.generate_private_key(public_exponent=65537, key_size 4096)

public_key = private_key.public_key();

PII_Birth = input("BIRTHDATE(ddmmyyyy):")
PII_name = input("NAME:")

byte_birth = PII_Birth.encode("utf-8")
byte_name = PII_names.encode("utf-8")
PII = byte_birth + byte_name


Sig = private_key.sign(PII, PADDING pss(
  mgf=padding.MGF1(hashes.SHA256()),
  salt_length=padding.PSS.MAX_LENGTH
), hashes.SHA256())

img = qrcode.make(String(Sig))
img.save("id.png")

