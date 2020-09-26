#!/usr/bin/env python3

import unittest
import sys

sys.path.append('../caesar')

import caesar_code

class CaesarCodeTest(unittest.TestCase):
    '''
    Test class for CaesarCode encode and decode methods correctness
    '''

    def setUp(self):
        self.tested_caesar_code = caesar_code.CaesarCode()
        self.alpahbet = 'abcdefghijklmnopqrstuvwxyz'

    def test_upper_a_encrypt_one(self):
        self.assertEqual(self.tested_caesar_code.encrypt('A', 1), 'B')

    def test_lower_letters_encrypt_two(self):
        self.assertEqual(
            self.tested_caesar_code.encrypt(self.alpahbet, 2),
            self.alpahbet[2:] + self.alpahbet[:2])

    def test_upper_letters_encrypt_ten(self):
        self.assertEqual(
            self.tested_caesar_code.encrypt(self.alpahbet.upper(), 10),
            self.alpahbet[10:].upper() + self.alpahbet[:10].upper())

    def test_sentence_encrypt_thirteen(self):
        self.assertEqual(
            self.tested_caesar_code.encrypt('Ala ma kota!', 7),
            'Hsh th rvah!')

    def test_sentence_encrypt_forty(self):
        '''
        Shifting by more than available letters set.
        '''
        self.assertEqual(
            self.tested_caesar_code.encrypt('Ala ma kota!', 40),
            'Ozo ao ycho!')

    def test_upper_a_decrypt_one(self):
        self.assertEqual(self.tested_caesar_code.decrypt('A', 1), 'Z')

    def test_lower_letters_decrypt_two(self):
        self.assertEqual(
            self.tested_caesar_code.decrypt(self.alpahbet, 2),
            self.alpahbet[-2:] + self.alpahbet[:-2])

    def test_upper_letters_decrypt_ten(self):
        self.assertEqual(
            self.tested_caesar_code.decrypt(self.alpahbet.upper(), 10),
            self.alpahbet[-10:].upper() + self.alpahbet[:-10].upper())

    def test_sentence_decrypt_thirteen(self):
        self.assertEqual(
            self.tested_caesar_code.decrypt('Ala ma kota!', 13),
            'Nyn zn xbgn!')

    def test_sentence_decrypt_forty(self):
        '''
        Shifting by more than available letters set.
        '''
        self.assertEqual(
            self.tested_caesar_code.decrypt('Ala ma kota!', 40),
            'Mxm ym wafm!')

if __name__ == '__main__':
    unittest.main()
