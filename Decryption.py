from asyncio.windows_events import NULL
import binascii
from gettext import find
from secrets import token_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
class Decryptor:
    def __init__(self, cipherText, cipher):
        self.cipherText = cipherText
        self.cipher = cipher
        self.plainText = NULL
    
    def decrypt(self):
        self.plainText = self.cipher.decrypt(self.cipherText)
        self.plainText = unpad(self.plainText, AES.block_size, 'pkcs7')
        return self.plainText.decode("utf-8")

class Decryptor_File:
    def __init__(self, path_in, path_out, cipher):
        self.cipher = cipher
        self.path_in = path_in
        tail = os.path.split(path_in)
        tail = tail[1]
        tail = tail[:-4]
        self.path_out = path_out + '/' + tail
    
    def decrypt(self):
        with open(self.path_in, 'rb') as f_in:
            data = f_in.read()
            decrypted = self.cipher.decrypt(data)
            decrypted = unpad(decrypted,AES.block_size,'pkcs7')
        f_in.close()
        with open(self.path_out, 'wb') as f_out:
            f_out.write(decrypted)
        f_out.close()



