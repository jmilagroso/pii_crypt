import json
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from pii_crypt.country_codes import country_codes

BLOCK_SIZE = 16


def pad(s): return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
    chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def unpad(s): return s[:-ord(s[len(s) - 1:])]


class PIICrypt:

    def __init__(self, key):
        self.key = key

        self.phone_number_prefixes = country_codes

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return b64encode(
            cipher.encrypt(
                raw.encode('utf8'))).decode('utf8')

    def decrypt(self, encrypted):
        encrypted = b64decode(encrypted)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return unpad(cipher.decrypt(encrypted)).decode('utf8')

    def anonymize_phone_number(self, phone_number):
        prefix = None

        if phone_number.startswith('0'):
            prefix = '0'
            phone_number = phone_number[1:]

        if phone_number.endswith('.0'):
            phone_number = '{}'.format(int(float(phone_number)))

        if phone_number.startswith('+'):
            phone_number = phone_number[1:]

        if prefix is None:
            iterations = [1, 2, 3, 4]

            for iteration in iterations:
                prefix = phone_number[:iteration]
                if prefix in self.phone_number_prefixes:
                    phone_number = phone_number[iteration:]
                    break

        return (
            self.encrypt(prefix),
            self.encrypt(phone_number)
        )
