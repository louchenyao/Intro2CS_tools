#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import Simulator as S


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Simulator for Machine Language")
    parser.add_argument("source_file", type = str)
    parser.add_argument("--pre_file", type = str, default = "")
    parser.add_argument("--debug", action = "store_true")
    args = parser.parse_args()
    
    sim = S.Simulator(0)
    if args.debug:
        if args.pre_file:
            sim.preExecute(args.pre_file)
        sim.load(args.source_file, 0)
        while sim.executeOneStep():
            sim.printMemory()
            sim.printRegistor()
            input("Press <Enter> to continue.")
    else:
        sim.execute(args.source_file, args.pre_file)
        sim.printMemory()
        sim.printRegistor()
