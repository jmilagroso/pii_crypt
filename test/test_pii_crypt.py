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

    def test_128bit_mobile_number_with_prefix_should_pass(self):

        test_mobile_number = '+639171230000'

        expected_code = 'XVqtVgFGyFGG4LAsR3OinA=='
        expected_encrypted_number = 'K/uURi3ZioVMuHnWXgNFgA=='
        expected_raw_code = '63'
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg128bit.anonymize_phone_number(
            test_mobile_number)

        self.assertEqual(result[0], expected_code)
        self.assertEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg128bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertEqual(
            self.pg128bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_128bit_mobile_number_with_prefix_should_fail(self):

        test_mobile_number = '+629171230000'

        expected_code = 'XVqtVgFGyFGG4LAsR3OinA=='
        expected_encrypted_number = 'q5NFKb/kBxPPoxRDK+F1RQ=='
        expected_raw_code = '63'
        expected_raw_number = '9171230001'

        # encrypt
        result = self.pg128bit.anonymize_phone_number(
            test_mobile_number)

        self.assertNotEqual(result[0], expected_code)
        self.assertNotEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertNotEqual(
            self.pg128bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertNotEqual(
            self.pg128bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_128bit_mobile_number_with_decimal_suffix_should_pass(
            self):

        test_mobile_number = '+639171230000.0'

        expected_code = 'XVqtVgFGyFGG4LAsR3OinA=='
        expected_encrypted_number = 'K/uURi3ZioVMuHnWXgNFgA=='
        expected_raw_code = '63'
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg128bit.anonymize_phone_number(
            test_mobile_number)

        self.assertEqual(result[0], expected_code)
        self.assertEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg128bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertEqual(
            self.pg128bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_128bit_mobile_number_with_zero_prefix_should_pass(self):

        test_mobile_number = '09171230000'

        expected_code = 'IF6DEdUrLRl+lXJpHu3sSg=='
        expected_encrypted_number = 'K/uURi3ZioVMuHnWXgNFgA=='
        expected_raw_code = '0'
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg128bit.anonymize_phone_number(
            test_mobile_number)

        self.assertEqual(result[0], expected_code)
        self.assertEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg128bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertEqual(
            self.pg128bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_128bit_mobile_number_with_zero_prefix_and_is_decimal_should_pass(
            self):

        test_mobile_number = '09171230000.0'

        expected_code = 'IF6DEdUrLRl+lXJpHu3sSg=='
        expected_encrypted_number = 'K/uURi3ZioVMuHnWXgNFgA=='
        expected_raw_code = '0'
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg128bit.anonymize_phone_number(
            test_mobile_number)

        self.assertEqual(result[0], expected_code)
        self.assertEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg128bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertEqual(
            self.pg128bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_256bit_mobile_number_with_prefix_should_pass(self):

        test_mobile_number = '+639171230000'

        expected_code = 'L4TeASt5zBmdJXBVCtIjRQ=='
        expected_encrypted_number = 'mZ/lGTxiyVRjAv1pjHHSjw=='
        expected_raw_code = '63'
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg256bit.anonymize_phone_number(
            test_mobile_number)

        self.assertEqual(result[0], expected_code)
        self.assertEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg256bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertEqual(
            self.pg256bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_256bit_mobile_number_with_prefix_should_fail(self):

        test_mobile_number = '+629171230000'

        expected_code = 'XVqtVgFGyFGG4LAsR3OinA=='
        expected_encrypted_number = 'q5NFKb/kBxPPoxRDK+F1RQ=='
        expected_raw_code = '63'
        expected_raw_number = '9171230001'

        # encrypt
        result = self.pg256bit.anonymize_phone_number(
            test_mobile_number)

        self.assertNotEqual(result[0], expected_code)
        self.assertNotEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertNotEqual(
            self.pg256bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertNotEqual(
            self.pg256bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_256bit_mobile_number_with_decimal_suffix_should_pass(
            self):

        test_mobile_number = '+639171230000.0'

        expected_code = 'L4TeASt5zBmdJXBVCtIjRQ=='
        expected_encrypted_number = 'mZ/lGTxiyVRjAv1pjHHSjw=='
        expected_raw_code = '63'
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg256bit.anonymize_phone_number(
            test_mobile_number)

        self.assertEqual(result[0], expected_code)
        self.assertEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg256bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertEqual(
            self.pg256bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_256bit_mobile_number_with_zero_prefix_should_pass(
            self):

        test_mobile_number = '09171230000'

        expected_code = 'ctz5MT3fQEdKi8UDp6RJkA=='
        expected_encrypted_number = 'mZ/lGTxiyVRjAv1pjHHSjw=='
        expected_raw_code = '0'
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg256bit.anonymize_phone_number(
            test_mobile_number)

        self.assertEqual(result[0], expected_code)
        self.assertEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg256bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertEqual(
            self.pg256bit.decrypt(
                result[1]),
            expected_raw_number)

    def test_256bit_mobile_number_with_zero_prefix_and_is_decimal_should_pass(
            self):

        test_mobile_number = '09171230000.0'

        expected_code = 'ctz5MT3fQEdKi8UDp6RJkA=='
        expected_encrypted_number = 'mZ/lGTxiyVRjAv1pjHHSjw=='
        expected_raw_code = '0'
        expected_raw_number = '9171230000'

        # encrypt
        result = self.pg256bit.anonymize_phone_number(
            test_mobile_number)

        self.assertEqual(result[0], expected_code)
        self.assertEqual(result[1], expected_encrypted_number)

        # decrypt
        self.assertEqual(
            self.pg256bit.decrypt(
                result[0]),
            expected_raw_code)
        self.assertEqual(
            self.pg256bit.decrypt(
                result[1]),
            expected_raw_number)
