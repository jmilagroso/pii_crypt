import unittest
from pii_crypt import PIICrypt


class TestPIISecurity(unittest.TestCase):

    def setUp(self):
        # 128 bit test key (16)
        self.test_128bit_secret_key = '1234567812345678'

        # 256 bit test key (32)
        self.test_256bit_secret_key = '12345678123456781234567812345678'

        # PIICrypt 128bit key instance
        self.pg128bit = PIICrypt(self.test_128bit_secret_key)

        # PIICrypt 256bit key instance
        self.pg256bit = PIICrypt(self.test_256bit_secret_key)

    def test_128bit_mobile_number_should_pass(self):

        test_mobile_number = '9171230000'

        expected_encrypted_number = 'K/uURi3ZioVMuHnWXgNFgA=='
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg128bit.encrypt(
            test_mobile_number)

        self.assertEqual(result, expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg128bit.decrypt(
                result),
            expected_raw_number)

    def test_128bit_mobile_number_should_fail(self):

        test_mobile_number = '9171230000'

        expected_encrypted_number = 'q5NFKb/kBxPPoxRDK+F1RQ=='
        expected_raw_number = '9171230001'

        # encrypt
        result = self.pg128bit.encrypt(
            test_mobile_number)

        self.assertNotEqual(result, expected_encrypted_number)

        # decrypt
        self.assertNotEqual(
            self.pg128bit.decrypt(
                result),
            expected_raw_number)

    def test_256bit_mobile_number_should_pass(self):

        test_mobile_number = '9171230000'

        expected_encrypted_number = 'mZ/lGTxiyVRjAv1pjHHSjw=='
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg256bit.encrypt(
            test_mobile_number)

        self.assertEqual(result, expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg256bit.decrypt(
                result),
            expected_raw_number)

    def test_256bit_mobile_number_should_fail(self):

        test_mobile_number = '9171230000'

        expected_encrypted_number = 'Mj1plEkVKmwPBD52MesuWA=='
        expected_raw_number = '9171230001'

        # encrypt
        result = self.pg256bit.encrypt(
            test_mobile_number)

        self.assertNotEqual(result, expected_encrypted_number)

        # decrypt
        self.assertNotEqual(
            self.pg256bit.decrypt(
                result),
            expected_raw_number)
