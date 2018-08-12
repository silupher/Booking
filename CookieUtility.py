from Model.CookieClass import CookieClass
from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib


class CookieUtility:
    Key = hashlib.sha256('IMPASSWORD!!!'.encode()).digest()

    def pad(s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    def unpad(s):
        return s[:-ord(s[len(s) - 1:])]

    def CreateCookie(text):
        text = CookieUtility.pad(text)

        iv = Random.new().read(AES.block_size)
        aes = AES.new(CookieUtility.Key, AES.MODE_CBC, iv)
        raw = aes.encrypt(text)
        return base64.b64encode(iv + raw).decode('utf-8')

    def ParseCookie(text):
        txt = base64.b64decode(text)
        iv = txt[:AES.block_size]
        cipher = AES.new(CookieUtility.Key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(txt[AES.block_size:])
        return CookieUtility.unpad(decrypted).decode('utf-8')