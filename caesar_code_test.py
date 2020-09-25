import unittest
import caesar_code

class CaesarCodeTest(unittest.TestCase):
    '''
    Test class for CaesarCode encode and decode methods correctness
    '''

    def setUp(self):
        self.tested_caesar_code = caesar_code.CaesarCode()
        self.alpahbet = 'abcdefghijklmnopqrstuvwxyz'

    def test_upper_a_encode_one(self):
        self.assertEqual(self.tested_caesar_code.encode('A', 1), 'B')

    def test_lower_letters_encoded_two(self):
        self.assertEqual(
            self.tested_caesar_code.encode(self.alpahbet, 2),
            self.alpahbet[2:] + self.alpahbet[:2])

    def test_upper_letters_encoded_ten(self):
        self.assertEqual(
            self.tested_caesar_code.encode(self.alpahbet.upper(), 10),
            self.alpahbet[10:].upper() + self.alpahbet[:10].upper())

    def test_sentence_encode_thirteen(self):
        self.assertEqual(
            self.tested_caesar_code.encode('Ala ma kota!', 7),
            'Hsh th rvah!')

    def test_sentence_encode_forty(self):
        '''
        Shifting by more than available letters set.
        '''
        self.assertEqual(
            self.tested_caesar_code.encode('Ala ma kota!', 40),
            'Ozo ao ycho!')

    def test_upper_a_decode_one(self):
        self.assertEqual(self.tested_caesar_code.decode('A', 1), 'Z')

    def test_lower_letters_decoded_two(self):
        self.assertEqual(
            self.tested_caesar_code.decode(self.alpahbet, 2),
            self.alpahbet[-2:] + self.alpahbet[:-2])

    def test_upper_letters_decoded_ten(self):
        self.assertEqual(
            self.tested_caesar_code.decode(self.alpahbet.upper(), 10),
            self.alpahbet[-10:].upper() + self.alpahbet[:-10].upper())

    def test_sentence_decode_thirteen(self):
        self.assertEqual(
            self.tested_caesar_code.decode('Ala ma kota!', 13),
            'Nyn zn xbgn!')

    def test_sentence_decode_forty(self):
        '''
        Shifting by more than available letters set.
        '''
        self.assertEqual(
            self.tested_caesar_code.decode('Ala ma kota!', 40),
            'Mxm ym wafm!')
