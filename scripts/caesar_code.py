import argparse
from pprint import pprint

class CaesarCode:

    __code_a = ord('a')
    __code_capital_a = ord('A')
    __difference = ord('z') - ord('a') + 1

    def __init__(self):
        self.parser = argparse.ArgumentParser()

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

    def cli(self):
        '''
        Possible arguments
        '''
        self.parser.add_argument(
            'option', choices=['encode', 'decode'],
            help='''Possible actions''')
        self.parser.add_argument(
            '--offset', type=int, required=True,
            help=''' Shift by number''')
        self.parser.add_argument(
            '--text', type=str, required=True,
            help='''Text to shift''' )

    def run(self):
        self.cli()
        args = self.parser.parse_args()
        if args.option == 'encode':
            print(self.encode(args.text, args.offset))
        elif args.option == 'decode':
            print(self.decode(args.text, args.offset))
        else:
            pprint('Something went wrong!')
