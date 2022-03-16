
from asyncio.windows_events import NULL
from pydoc import plain
from secrets import token_bytes
from urllib.parse import ParseResultBytes
import Encryption
import Decryption
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import uiAES
import RSAkey
import EncryptorRSA
def main():
    import sys
    app = uiAES.QtWidgets.QApplication(sys.argv)
    MainWindow = uiAES.QtWidgets.QMainWindow()
    ui = uiAES.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def Encrypt(plainText, key):
    key = pad(key, AES.block_size, 'pkcs7')
    cipher = AES.new(key, AES.MODE_ECB)
    cipherText = Encryption.Encryptor(plainText,cipher).encrypt()
    return cipherText

def Decrypt(cipherText, key):
    key = pad(key, AES.block_size, 'pkcs7')
    cipher = AES.new(key, AES.MODE_ECB)
    plainText = Decryption.Decryptor(cipherText, cipher).decrypt()
    return plainText
    
def EncryptFile(path_in, path_out, key):
    key = key.encode('utf-8')
    key = pad(key, AES.block_size, 'pkcs7')
    cipher = AES.new(key, AES.MODE_ECB)
    Encryption.Encryptor_File(path_in, path_out, cipher).encrypt()

def DecryptFile(path_in, path_out, key):
    key = key.encode("utf-8")
    key = pad(key, AES.block_size, 'pkcs7')
    cipher = AES.new(key, AES.MODE_ECB)
    Decryption.Decryptor_File(path_in, path_out, cipher).decrypt()

def CreatKeyRSA(path_out, check, sizeK):
    RSAkey.Creat_K(path_out, check, sizeK)

def EncryptRSA(path_in, plainText):
    return EncryptorRSA.Encrypt(path_in, plainText)

def DecryptRSA(path_in, cipherText):
    return EncryptorRSA.Decrypt(path_in, cipherText)

if __name__ == "__main__":
    main()