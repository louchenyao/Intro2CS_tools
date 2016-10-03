# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:04:47 2016

@author: zhy
"""

class Simulator(object):
    def __init__(self, counter):
        self.memory = [0] * 0x100
        self.program_counter = counter
        self.register = [0] * 0x10
        self.count = 0

    def clearAll(self):
        self.memory = [0] * 0x100
        self.register = [0] * 0x10
        self.program_counter = 0
        self.count = 0

    def setCounter(self,x):
        self.program_counter = x

    def write(self, filename, location):
        i = location
        file = open(filename)
        for line in file:
            instruction = int(line, 16)
            first = instruction // 0x100
            second = instruction % 0x100
            self.memory[i] = first
            self.memory[i+1] = second
            i += 2
        print("writting complete")
        file.close()

    def executeOneStep(self):
        self.count += 1
        #print("One Step Mode")
        a = self.memory[self.program_counter]
        b = self.memory[self.program_counter + 1]
        print(str(self.count) + " " + str(hex(a)) + " " + str(hex(b)))
        op_code = a // 0x10
        oprand = 0X100 * (a % 0x10) + b
        self.program_counter  = (self.program_counter + 2) % 0x100
        if op_code == 1:
            #print("execute 1")
            R = oprand // 0x100
            XY = oprand % 0x100
            self.register[R] = self.memory[XY]
        elif op_code == 2:
            #print("execute 2")
            R = oprand // 0x100
            XY = oprand % 0x100
            self.register[R] = XY
        elif op_code == 3:
            #print("execute 3")
            R = oprand // 0x100
            XY = oprand % 0x100
            self.memory[XY] = self.register[R]
        elif op_code == 4:
            #print("execute 4")
            S = oprand % 0x10
            R = (oprand % 0x100) // 0x10
            self.register[S] = self.register[R]
        elif op_code == 5:
            #print("execute 5")
            R = oprand // 0x100
            S = (oprand % 0x100) // 0x10
            T = oprand % 0x10
            self.register[R] = (self.register[S] + self.register[T]) % 0x100
        elif op_code == 6:
            pass
        elif op_code == 7:
            #print("execute 7")
            R = oprand // 0x100
            S = (oprand % 0x100) // 0x10
            T = oprand % 0x10
            self.register[R] = self.register[S] | self.register[T]
        elif op_code == 8:
            #print("execute 8")
            R = oprand // 0x100
            S = (oprand % 0x100) // 0x10
            T = oprand % 0x10
            self.register[R] = self.register[S] & self.register[T]
        elif op_code == 9:
            #print("execute 9")
            R = oprand // 0x100
            S = (oprand % 0x100) // 0x10
            T = oprand % 0x10
            self.register[R] = self.register[S] ^ self.register[T]
        elif op_code == 0xA:
            #print("execute A")
            R = oprand // 0x100
            X = oprand % 0x10
            self.register[R] = self.register[R] >> X
        elif op_code == 0xB:
            #print("execute B")
            R = oprand // 0x100
            XY = oprand % 0x100
            if oprand == 0x070:
                print(self.count)
                print(self.count)
            if self.register[R] == self.register[0]:
                self.program_counter = XY
        elif op_code == 0xC and oprand == 0:
            print("execute C")
            return
        else:
            print("execute else")
            return


    def printMemory(self):
        print("show memory")
        for i in range(0, 0x10):
            for j in range(0, 0x10):
                print(str(hex(self.memory[0x10 * i + j])), end = " ")
            print("\n")

    def printRegister(self):
        print("show register")
        for i in range(0, 0x10):
            print(str(hex(self.register[i])), end = ' ')
        print("\n")
