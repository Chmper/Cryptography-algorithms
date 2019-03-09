class Coder:
    def __init__(self, key_word, file_name):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
        self.key_word = key_word
        self.table = [(self.letters * 2)[i:i+26] for i in range(26)]
        self.file = file_name

    def extend_key(self, string):
        extended_key = ''
        i = 0
        for char in string:
            if char == ' ':
                extended_key += ' '
            elif char == '\n':
                extended_key += '\n'
            else:
                extended_key += self.key_word[i%len(self.key_word)]
                i += 1

        return extended_key

    def code_file(self):
        string = ''
        with open(self.file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            string += line


        extend_key = self.extend_key(string)

        string_int = [ord(i) for i in string]
        key_int = [ord(i) for i in extend_key]

        coded_string = ''
        i = 0
        for char in string:
            if char == ' ':
                coded_string += ' '
                i += 1
            elif char == '\n':
                coded_string += '\n'
                i += 1
            else:
                coded_string += self.table[string_int[i]-97][key_int[i]-97]
                i += 1

        with open('viegnere.txt', 'w') as file:
            file.write(coded_string)

class Decoder:
    def __init__(self, key_word, file_name):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
        self.table = [(self.letters * 2)[i:i+26] for i in range(26)]
        self.key_word = key_word
        self.file = file_name

    def extend_key(self, string):
        extended_key = ''
        i = 0
        for char in string:
            if char == ' ':
                extended_key += ' '
            elif char == '\n':
                extended_key += '\n'
            else:
                extended_key += self.key_word[i%len(self.key_word)]
                i += 1

        return extended_key

    def decode_file(self):
        string = ''
        with open(self.file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            string += line

        extend_key = self.extend_key(string)

        decoded_string = ''
        i = 0
        for char in extend_key:
            if char == ' ':
                decoded_string += ' '
                i += 1
            elif char == '\n':
                decoded_string += '\n'
                i += 1
            else:
                decoded_string += chr((26-ord(string[i])-97)%26)


if __name__ == '__main__':
    coder = Coder('tajne', 'szyfrogram.txt')
    coder.code_file()

    decoder = Decoder('tajne', 'viegnere.txt')
    decoder.decode_file()

    for char in 'wakii':
        print(chr((26-ord(char))%26+97))
