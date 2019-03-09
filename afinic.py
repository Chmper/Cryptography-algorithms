from sympy import mod_inverse

class Coder:
    def __init__(self, a, b, file_name):
        self.a = a
        self.b = b
        self.m = 26
        self.file = file_name

    def code_char(self, char):
        letter = self.a*(ord(char)-97)+self.b
        letter = letter % self.m
        return chr(letter+97)

    def code_file(self):
        with open(self.file, 'r') as file:
            lines = file.readlines()

        coded_string = ''
        for line in lines:
            for char in line:
                if char == '\n':
                    coded_string += '\n'
                elif char == ' ':
                    coded_string += ' '
                else:
                    coded_string += self.code_char(char)
        return coded_string

    def write_coded_file(self):
        coded_string = self.code_file()
        with open('afiniczny.txt', 'w') as file:
            file.write(coded_string)


class Decoder:
    def __init__(self, a, b, file_name):
        self.a = a
        self.b = b
        self.m = 26
        self.file = file_name

    @property
    def inverse(self):
        return mod_inverse(self.a, self.m)

    def decode_char(self, char):
        # d(y) = self.inverse * (y - self.a) % 26
        decoder_char = self.inverse*((ord(char)-97)-self.b) % self.m
        return chr(decoder_char+97)

    def decode_file(self):
        with open(self.file, 'r') as file:
            lines = file.readlines()

        decoded_string = ''
        for line in lines:
            for char in line:
                if char == '\n':
                    decoded_string += '\n'
                elif char == ' ':
                    decoded_string += ' '
                else:
                    decoded_string += self.decode_char(char)
        return decoded_string

    def write_decoded_file(self):
        decoded_string = self.decode_file()
        with open('decoded_afiniczny.txt', 'w') as file:
            file.write(decoded_string)

if __name__ == '__main__':
    coder = Coder(3,3, 'szyfrogram.txt')
    coder.write_coded_file()

    decoder = Decoder(7,5, 'afiniczny.txt')
    decoder.write_decoded_file()
