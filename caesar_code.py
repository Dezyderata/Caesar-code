#!/usr/bin/env python3

class CaesarCode:

    __code_a = ord('a')
    __code_capital_a = ord('A')
    __difference = ord('z') - ord('a') + 1

    def decode(self, text, shift):
        return self.encode(text, -shift)

    def encode(self, text, shift):
        result = ''
        for letter in text:
            if letter.islower():
                result += self.inner_function(
                    letter, self.__code_a, shift)
            elif letter.isupper():
                result += self.inner_function(
                    letter, self.__code_capital_a, shift)
            else:
                result += letter
        return result

    def inner_function(self, letter, code, shift):
        letter_numeric = (lambda x: ord(x) - code)(letter)
        return chr(code + (letter_numeric + shift)%self.__difference)
