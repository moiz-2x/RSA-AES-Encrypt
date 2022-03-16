from asyncio.windows_events import NULL

from Crypto.Cipher import AES
from secrets import token_bytes
from Crypto.Util.Padding import pad
import binascii
import os

class Encryptor:
    def __init__(self, plainText, cipher):
        plainText = plainText.encode("utf-8")
        self.plainText = plainText
        self.cipher = cipher
        self.cipherText = NULL

    def encrypt(self):
        self.plainText = pad(self.plainText, AES.block_size, 'pkcs7')
        self.cipherText = self.cipher.encrypt(self.plainText) 
        return self.cipherText

class Encryptor_File:
    def __init__(self, path_in, path_out, cipher):
        self.path_in = path_in
        tail = os.path.split(path_in)
        tail = tail[1]
        self.path_out = path_out+'/'+tail+'.enc'
        self.cipher = cipher
    
    def encrypt(self):
        with open(self.path_in, 'rb') as f_in:
            data = f_in.read()
            cipherText = self.cipher.encrypt(pad(data, AES.block_size,'pkcs7'))
        f_in.close()
        with open(self.path_out, 'wb') as f_out:
            f_out.write(cipherText)
        f_out.close()





