#! /usr/bin/env python

import os

VAR_TABLE = {}

def to_hex(n):
    return hex(n)[2:].upper()

def to_dec(n):
    return int(n, 16)

def is_int(s):
    if s[0] in ('-', '+'):
    	return s[1:].isdigit()
    return s.isdigit()

def pharse_var(v):
    if is_int(v):
        return int(v)
    return VAR_TABLE[v]

class Instruction(object):
    OP2CODE = {
        "load-memory": 1,
        "load-pattern": 2,
        "store": 3,
        "add": 5,
        "jump": 11,
    }
    OP_OPERAND = {
        "load-memory": "48",
        "load-pattern": "48",
        "store": "48",
        "add": "444",
        "jump": "48",
    }
    def __init__(self, operation, operand = []):
        if (len(operand) != len(self.OP_OPERAND[operation])):
            raise Exception("Incorrect operation: %s %s" % (operation, operand))

        self.operation = operation
        self.operand = list(operand)

    def to_machine_code(self):
        n = self.OP2CODE[self.operation]
        pat = self.OP_OPERAND[self.operation]

        for i in range(0, len(self.operand)):
            # print(n)
            n *= 2**to_dec(pat[i])
            # print(to_dec(pat[i]))
            n += pharse_var(self.operand[i])

        return to_hex(n)

class MachineCode(object):
    def __init__(self)

def main(src):
    pass

if __name__  == "__main__":
    with open("b.txt") as f:
        src = f.read()
    mc = compile(src)
    mc.print()
