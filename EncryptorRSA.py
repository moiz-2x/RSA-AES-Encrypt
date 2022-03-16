from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def Encrypt(path_in, plainText):
    with open(path_in, "rb") as f:
            if path_in[-8] == "c":
                pub_key = serialization.load_pem_public_key(f.read())
            else:
                pri_key = serialization.load_pem_private_key(f.read(), password=None)
                pub_key = pri_key.public_key()
    f.close()
    cipherText = pub_key.encrypt(plainText,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    return cipherText

def Decrypt(path_in, cipherText):
    with open(path_in, "rb") as f:
        pri_key = serialization.load_pem_private_key(f.read(), password=None)
        f.close()
    plainText = pri_key.decrypt(cipherText, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    return plainText
    