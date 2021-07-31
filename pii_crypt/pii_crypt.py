from base64 import b64decode
from base64 import b64encode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class PIICrypt:

    def __init__(self, key):
        self.key = key

        self.BLOCK_SIZE = 16
        self.ENCODING = 'utf-8'

        self.cipher = Cipher(
            algorithms.AES(
                self.key.encode(self.ENCODING)
            ),
            modes.ECB()
        )

        self.encryptor = self.cipher.encryptor()

        self.decryptor = self.cipher.decryptor()

    def pad(self, s):
        return s \
            + (self.BLOCK_SIZE - len(s) %
               self.BLOCK_SIZE) * chr(self.BLOCK_SIZE - len(s) %
                                      self.BLOCK_SIZE)

    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, raw):
        raw = self.pad(raw)

        return b64encode(
            self.encryptor.update(
                raw.encode(self.ENCODING)) +
            self.encryptor.finalize()
        ).decode(self.ENCODING)

    def decrypt(self, encrypted):
        encrypted = b64decode(encrypted)

        return self.unpad(
            self.decryptor.update(encrypted) +
            self.decryptor.finalize()
        ).decode(self.ENCODING)
