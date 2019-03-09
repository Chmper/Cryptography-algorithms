import numpy as np
from operator import xor
import os

class A5:
    def __init__(self):
        self.lsfr1 = [1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1] # 13, 16, 17, 18
        self.lsfr1=np.array(self.lsfr1)
        self.lsfr2 = [1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,1]
        self.lsfr2=np.array(self.lsfr2)
        self.lsfr3 = [1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,0,1,0,0,0]
        self.keystream = []
        self.lsfr3=np.array(self.lsfr3)

    def __str__(self):
        return self.lsfr1.__str__()

    @property
    def key(self):
        for idx, k in enumerate(self.keystream):
            if idx%4 == 0:
                print(' ', end='')
            print(k, end='')


    def shift_r1(self):
        a = xor(xor(xor(self.lsfr1[18], self.lsfr1[17]), self.lsfr1[16]), self.lsfr1[13])
        self.lsfr1 = np.roll(self.lsfr1,1)
        self.lsfr1[0] = a

    def shift_r2(self):
        a = xor(self.lsfr2[20], self.lsfr2[21])
        self.lsfr2 = np.roll(self.lsfr2,1)
        self.lsfr2[0] = a

    def shift_r3(self):
        a = xor(xor(xor(self.lsfr3[22], self.lsfr3[21]), self.lsfr3[20]), self.lsfr3[7])
        self.lsfr3 = np.roll(self.lsfr3,1)
        self.lsfr3[0] = a


    def step4(self): # keystrem obliczanko
        for i in range(228):
            zeros = 0
            ones = 0
            self.keystream.append(xor(xor(self.lsfr1[-1], self.lsfr2[-1]), self.lsfr3[-1]))

            if self.lsfr1[8] == 1:
                ones += 1
            else:
                zeros += 1

            for lsfr in [self.lsfr2, self.lsfr3]:
                if lsfr[10] == 1:
                    ones += 1
                else:
                    zeros += 1

            if ones > zeros:
                if self.lsfr1[8] == 1:
                    self.shift_r1()
                if self.lsfr2[10] == 1:
                    self.shift_r2()
                if self.lsfr3[10] == 1:
                    self.shift_r3()

            else:
                if self.lsfr1[8] == 0:
                    self.shift_r1()
                if self.lsfr2[10] == 0:
                    self.shift_r2()
                if self.lsfr3[10] == 0:
                    self.shift_r3()

            os.system("cls")
            print(self.keystream)
            input()

if __name__ == "__main__":
    crypto = A5()
    print("R1: ", crypto.lsfr1)
    print("R2: ", crypto.lsfr2)
    print("R3: ", crypto.lsfr3)

    while(1):
        a = input("1-przesun rejestry, 2-podaj keystream >> ")
        a = int(a)
        if(a == 1):
            crypto.shift_r1()
            crypto.shift_r2()
            crypto.shift_r3()

            print("R1: ", crypto.lsfr1)
            print("R2: ", crypto.lsfr2)
            print("R3: ", crypto.lsfr3)
        else:
            crypto.step4()
            print(crypto.key)
