import qrcode
import cryptography.hazamt.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#pip install cryptography


private_key = rsa.generate_private_key(public_exponent=65537, key_size 4096)

public_key = private_key.public_key();

