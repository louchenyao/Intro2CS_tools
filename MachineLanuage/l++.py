#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright Chenyao2333

import os
import argparse

VAR_TABLE = {}

def to_two_complement(n):
    if (n < 0):
        n = (-n) ^ 0xFF
        n += 1

    return n

def to_hex(n):
    return hex(n)[2:].upper()

def to_dec(n):
    return int(n, 16)

def is_dec(s):
    for i in s:
        if not i.isdigit():
            return False
    return True

def is_hex(s):
    if not s.startswith("0x"):
        return False
    try:
        int(s, 16)
        return True
    except:
        return False

def parse_var(v, var_table):
    if isinstance(v, int):
        return v
    elif v == "":
        return 0
    elif v in var_table:
        return var_table[v]
    elif is_hex(v):
        return int(v, 16)
    elif is_dec(v):
        return int(v)
    elif "+" in v:
        return sum(list(map(lambda x: parse_var(x, var_table), v.split("+"))))
    elif "-" in v:
        p = v.rfind("-")
        return parse_var(v[0:p], var_table) - parse_var(v[p+1:], var_table)
    else:
        raise Exception()

class Instruction(object):
    OP2CODE = {
        "load-memory": 1,
        "load-pattern": 2,
        "store": 3,
        "add": 5,
        "add-float": 6,
        "and": 8,
        "jump": 11,
    }
    OP_OPERAND = {
        "load-memory": "48",
        "load-pattern": "48",
        "store": "48",
        "add": "444",
        "add-float": "444",
        "and": "444",
        "jump": "48",
    }
    def __init__(self, operation, operand = []):
        print ("op = %s operand = %s" % (operation, operand))
        if (len(operand) != len(self.OP_OPERAND[operation])):
            raise Exception("Incorrect operation: %s %s" % (operation, operand))

        self.operation = operation
        self.operand = list(operand)

    def process_variable(self, var_table):
        for i in range(0, len(self.operand)):
            try:
                self.operand[i] = parse_var(self.operand[i], var_table)
            except:
                print("Failing to parse %s" % self.operand[i])
                pass

    def to_machine_code(self, var_table):
        n = self.OP2CODE[self.operation]
        pat = self.OP_OPERAND[self.operation]

        for i in range(0, len(self.operand)):
            # print(self.operand[i])
            n *= 2**to_dec(pat[i])
            n += to_two_complement(parse_var(self.operand[i], var_table))

        #print(n)
        return to_hex(n)

class MachineCode(object):
    def __init__(self, src):
        self.instructions = []
        self.var_table = {}

        for line in src.splitlines():
            line = line.strip()
            if line.startswith("#"):
                continue
            ops = line.split()
            if len(ops) == 0:
                continue

            if ops[0] == "using":
                self.var_table[ops[1]] = int(ops[-1])
            elif ops[0] == "tag":
                self.var_table[ops[1]] = len(self.instructions) * 2
            else:
                ins = Instruction(ops[0], ops[1:])
                ins.process_variable(self.var_table)
                self.instructions.append(ins)

        self.var_table["__code_length"] = len(self.instructions) * 2

    def __repr__(self):
        s = ""
        for i in self.instructions:
            s += i.to_machine_code(self.var_table) + "\n"
        return s

def compile(src):
    mc = MachineCode(src)
    return mc.__repr__()

if __name__  == "__main__":
    parser = argparse.ArgumentParser(description="Compile the \"lpp\" into \"A Simple Machine Language.\"")
    parser.add_argument("src_file", help="The source file of \"lpp\"")
    parser.add_argument("output_file", help="The source file of \"A Simple Machine Language\"")

    args = parser.parse_args()
    args = vars(args)

    with open(args["src_file"]) as f:
        src = f.read()
    output = compile(src)
    with open(args["output_file"], "w") as f:
        f.write(output)
