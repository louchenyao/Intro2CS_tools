#! /usr/bin/env python3

import argparse
import sys

class State(object):
    def __init__(self, s):
        #print(s.strip().split())
        name, cur, write, dirct, next = s.strip().split()
        self.name = name
        self.cur = cur
        self.write = write
        self.dirct = dirct
        self.next = next

    def __repr__(self):
        return str([self.name, self.cur, self.write, self.dirct, self.next])


def run(tape, start):
    cur_s = "START"
    pos = start
    while True:
        print(tape)
        print(cur_s, pos)
        input("Press the <ENTER> key to continue...")

        if cur_s == "HALT":
            break

        for s in states:
            if s.name == cur_s and (tape[pos] == s.cur or s.cur.lower() == "(ignored)"):
                tape[pos] = s.write
                if s.dirct.lower() == "left":
                    pos -= 1;
                    if pos < 0:
                        pos = 0
                        tape = ["x"] + tape
                elif s.dirct.lower() == "right":
                    pos += 1;
                    if pos >= len(tape):
                        tape = tape + ["x"]
                elif s.dirct.lower() == "nomove":
                    pass
                else:
                    raise Exception()
                cur_s = s.next
                break

    print(tape)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulator of Turning Machine.")
    parser.add_argument("tape", help="The file of tape.")
    parser.add_argument("program", help="The source file of Turning Machine.")

    args = parser.parse_args()
    args = vars(args)

    tape = ""
    start = 0
    states_str = ""
    with open(args["tape"]) as f:
        tape = f.readline()
        start = int(f.readline())

    with open(args["program"]) as f:
        states_str = f.read()

    states = []
    for line in states_str.splitlines():
        if len(line.strip()) < 2:
            continue
        states.append(State(line))
    tape = list(tape.strip())

    print(states)
    print(tape)
    print(start)
    print(tape[start])

    run(tape, start)
