import json
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES


class PIICrypt:

    def __init__(self, key):
        self.key = key

        self.encoding = 'utf8'

        self.BLOCK_SIZE = 16

    def pad(self, s): return s + \
        (self.BLOCK_SIZE - len(s) %
            self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(s) %
                                   self.BLOCK_SIZE)

    def unpad(self, s): return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, raw):
        raw = self.pad(raw)
        cipher = AES.new(self.key.encode(self.encoding), AES.MODE_ECB)
        return b64encode(
            cipher.encrypt(
                raw.encode(self.encoding))).decode(self.encoding)

    def decrypt(self, encrypted):
        encrypted = b64decode(encrypted)
        cipher = AES.new(self.key.encode(self.encoding), AES.MODE_ECB)
        return self.unpad(
            cipher.decrypt(encrypted)).decode(
            self.encoding)
