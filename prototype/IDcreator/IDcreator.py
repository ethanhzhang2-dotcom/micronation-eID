import qrcode
import cryptography.hazamt.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backend import default_backend.

#pip install cryptography

#generates private-public key pair for individual
private_key = rsa.generate_private_key(public_exponent=65537, key_size 4096)

public_key = private_key.public_key();

#upload private key of micronation

micronation_public_DST = "<path of key file>"
micronation_private_DST = "<path of key file>"
micronation_public = ""
micronation private = ""

with open(micronation_public_DST, "rb") as key_file:
  micronation_public = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
  
with open(micronation_private_DST, "rb") as keyfile:
  micronation_private = serialization.load_pem_private_key(
            keyfile.read(),
            password=none,
            backend=default_backend()
        )
  
  #generating visible values on id

#converting all values needed into byte objects

message = bytes(public_key)

signature = micronation_private.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()

  print("Public Key: ", public_key)
  print("Private key: ", private_key)
  print("signature: ", signature)
