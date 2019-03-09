import numpy as np
from operator import xor

class DES:
    def __init__(self):
        self.key_64 = np.random.randint(2, size=64)
        self.CP_1 = [57, 49, 41, 33, 25, 17, 9,
                     1, 58, 50, 42, 34, 26, 18,
                     10, 2, 59, 51, 43, 35, 27,
                     19, 11, 3, 60, 52, 44, 36,
                     63, 55, 47, 39, 31, 23, 15,
                     7, 62, 54, 46, 38, 30, 22,
                     14, 6, 61, 53, 45, 37, 29,
                     21, 13, 5, 28, 20, 12, 4]
        self.CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
                     15, 6, 21, 10, 23, 19, 12, 4,
                     26, 8, 16, 7, 27, 20, 13, 2,
                     41, 52, 31, 37, 47, 55, 30, 40,
                     51, 45, 33, 48, 44, 49, 39, 56,
                     34, 53, 46, 42, 50, 36, 29, 32]

        self.givens = np.random.randint(2, size=64)

        self.E = [32, 1, 2, 3, 4, 5,
                  4, 5, 6, 7, 8, 9,
                  8, 9, 10, 11, 12, 13,
                  12, 13, 14, 15, 16, 17,
                  16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25,
                  24, 25, 26, 27, 28, 29,
                  28, 29, 30, 31, 32, 1]

        self.S_5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

        self.P = [16, 7, 20, 21, 29, 12, 28, 17,
                  1, 15, 23, 26, 5, 18, 31, 10,
                  2, 8, 24, 14, 32, 27, 3, 9,
                  19, 13, 30, 6, 22, 11, 4, 25]

        self.halves = [0,1,8,15] # indeksy dla ktorych przesuwamy o 1

    def perm_cp_1(self): ## robienia klucza 48bit
        temp_key = []
        for i in self.CP_1: # reduce 64->56
            temp_key.append(self.key_64[i-1])

        left = temp_key[:28] ## podzial na lewy i prawo
        right = temp_key[28:]


        left = np.roll(np.array(left), -2)
        right = np.roll(np.array(right), -2)

        temp_key = np.concatenate((left, right), axis=0)

        self.key = []
        for i in self.CP_2:
            self.key.append(temp_key[i-1]) ## permutacja

        self.key = np.array(self.key) ## 48 bit

    def given_step(self):
        temp_given = self.givens[32:] ## prawa strona danych
        new_given = []
        for i in self.E:
            new_given.append(temp_given[i-1]) ## permutacja

        xored_array = []
        for i in range(48):
            xored_array.append(xor(new_given[i], self.key[i])) ## xorowanie z kluczem

        self.S = []

        for i in range(8):
            self.S.append(xored_array[i*6 : (i+1)*6]) ## dzielenie na boxy

    def permut_boxes(self):
        four_bit_arr = []
        print(self.S)
        for s in self.S: ## liczenie kolumny i wiersza
            row = str(s[0])+str(s[-1])
            row = int(row,2)

            column = str(s[1]) + str(s[2]) + str(s[3]) + str(s[4])
            column = int(column, 2)
            four_bit_arr.append(list(bin(self.S_5[row][column])[2:])) ## zamiana int -> bit

        for f in four_bit_arr:
            for i in range(len(f)):
                f[i] = int(f[i])
            if len(f)<4:
                for i in range(4-len(f)): ## dopelnianie do 4bit
                    f.append(0)

        self.afer_boxes = np.concatenate(four_bit_arr)

    def permut_P(self):
        temp_array = []
        print(self.afer_boxes)
        for p in self.P:
            temp_array.append(self.afer_boxes[p-1]) ## zaszyfrowane 32bit
