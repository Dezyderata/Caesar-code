import argparse

class CaesarCode:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.__code_a = ord('a')
        self.__code_capital_a = ord('A')
        self.__difference = ord('z') - ord('a') + 1

    def decrypt(self, text, shift):
        return self.encrypt(text, -shift)

    def encrypt(self, text, shift):
        result = []
        for letter in text:
            if letter.islower():
                result.append(self.inner_function(
                    letter, self.__code_a, shift))
            elif letter.isupper():
                result.append(self.inner_function(
                    letter, self.__code_capital_a, shift))
            else:
                result.append(letter)
        return ''.join(result)

    def inner_function(self, letter, code, shift):
        letter_numeric = (lambda x: ord(x) - code)(letter)
        return chr(code + (letter_numeric + shift)%self.__difference)

    def cli(self):
        '''
        Possible arguments
        '''
        self.parser.add_argument(
            'option', choices=['encrypt', 'decrypt'],
            help='''Possible actions''')
        self.parser.add_argument(
            '--offset', type=int, required=True,
            help=''' Shift by number. Argument is required.''')
        self.parser.add_argument(
            '--text', type=str, required=True,
            help='''Text to shift. Argument is required.''')
        self.parser.usage = self.parser.format_help()

    def run(self):
        self.cli()
        args = self.parser.parse_args()
        if args.option == 'encrypt':
            print(self.encrypt(args.text, args.offset))
        elif args.option == 'decrypt':
            print(self.decrypt(args.text, args.offset))
        else:
            print(self.parser.print_usage())
