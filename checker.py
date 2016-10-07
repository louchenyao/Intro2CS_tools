# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:03:49 2016

@author: zhy
"""

import Simulator as S

def main():
    sim = S.Simulator(0)
    sim.write("c.txt", 0)

    while(True):
        s = input(">>")
        if (s == 'q'):
            break
        else:
            for i in range(0, 810):
                sim.executeOneStep()
            sim.printMemory()
            sim.printRegister()

if __name__ == '__main__':
    main()
