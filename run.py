#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:03:49 2016

@author: zhy
"""

import sys
import Simulator as S

fout = open("log.txt", "w")
sys.stdout = fout

sim = S.Simulator(0)
sim.write("c.txt", 0)
for i in range(0,3000):
    sim.executeOneStep()
    #sim.printMemory()
    #sim.printRegister()

#sim.execute(400)
sim.printMemory()
sim.printRegister()
