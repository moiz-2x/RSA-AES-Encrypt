from pickle import TRUE
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def Creat_K(path, check, sizeK):
    private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=sizeK,
    )
    pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
    )
    if (check == 1):
        with open(path + "\privateKey.PEM", "wb") as f:
            f.write(pem)
            f.close()
        pub_key = private_key.public_key()
        pem =pub_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
        with open(path + "\publicKey.PEM", "wb") as f:
            f.write(pem)
            f.close()
    else:
        with open(path + "\privateKey.PEM", "wb") as f:
            f.write(pem)
            f.close()