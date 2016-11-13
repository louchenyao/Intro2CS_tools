# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:04:47 2016

@author: zhy
"""

class Simulator(object):
    def __init__(self, counter):
        self.memory = [0] * 0x100
        self.program_counter = counter
        self.registor = [0] * 0x10
        self.count = 0

    def clearAll(self):
        self.memory = [0] * 0x100
        self.registor = [0] * 0x10
        self.program_counter = 0
        self.count = 0

    def setCounter(self,x):
        self.program_counter = x
        
    def setMem(self, pos, val):
        self.memory[pos] = val

    def load(self, filename, location):
        i = location
        file = open(filename)
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            instruction = int(line, 16)
            first = instruction // 0x100
            second = instruction % 0x100
            self.memory[i] = first
            self.memory[i+1] = second
            i += 2
        print("loading complete")
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
            self.registor[R] = self.memory[XY]
        elif op_code == 2:
            #print("execute 2")
            R = oprand // 0x100
            XY = oprand % 0x100
            self.registor[R] = XY
        elif op_code == 3:
            #print("execute 3")
            R = oprand // 0x100
            XY = oprand % 0x100
            self.memory[XY] = self.registor[R]
        elif op_code == 4:
            #print("execute 4")
            S = oprand % 0x10
            R = (oprand % 0x100) // 0x10
            self.registor[S] = self.registor[R]
        elif op_code == 5:
            #print("execute 5")
            R = oprand // 0x100
            S = (oprand % 0x100) // 0x10
            T = oprand % 0x10
            self.registor[R] = (self.registor[S] + self.registor[T]) % 0x100
        elif op_code == 6:
            pass
        elif op_code == 7:
            #print("execute 7")
            R = oprand // 0x100
            S = (oprand % 0x100) // 0x10
            T = oprand % 0x10
            self.registor[R] = self.registor[S] | self.registor[T]
        elif op_code == 8:
            #print("execute 8")
            R = oprand // 0x100
            S = (oprand % 0x100) // 0x10
            T = oprand % 0x10
            self.registor[R] = self.registor[S] & self.registor[T]
        elif op_code == 9:
            #print("execute 9")
            R = oprand // 0x100
            S = (oprand % 0x100) // 0x10
            T = oprand % 0x10
            self.registor[R] = self.registor[S] ^ self.registor[T]
        elif op_code == 0xA:
            #print("execute A")
            R = oprand // 0x100
            X = oprand % 0x10
            self.registor[R] = self.registor[R] >> X
        elif op_code == 0xB:
            #print("execute B")
            R = oprand // 0x100
            XY = oprand % 0x100
            if oprand == 0x070:
                print(self.count)
                print(self.count)
            if self.registor[R] == self.registor[0]:
                self.program_counter = XY
        elif op_code == 0xC and oprand == 0:
            print("execute C")
            return False
        else:
            print("execute else")
            return False
        return True
    
    def preExecute(self, pre_exe):
        s = Simulator(0)
        s.execute(pre_exe)
        self.memory = s.memory
        self.registor = s.registor
    
    def execute(self, source_file, pre_exe = ""):
        self.clearAll()
        # print("%s %s\n" % (source_file, pre_exe))
        if pre_exe:
            self.preExecute(pre_exe)
        self.load(source_file, 0)
        while self.executeOneStep():
            pass
        return True


    def printMemory(self):
        print("show memory")
        for i in range(0, 0x10):
            for j in range(0, 0x10):
                print(str(hex(self.memory[0x10 * i + j])), end = " ")
            print("\n")

    def printRegistor(self):
        print("show registor")
        for i in range(0, 0x10):
            print(str(hex(self.registor[i])), end = ' ')
        print("\n")
