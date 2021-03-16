#!/usr/bin/env python3

import sys
import math
from calc import calc_one_loop
from calc import calc_transfer

def display_h(argv):
    if len(argv[1]) == 2 and argv[1][0] == '-' and argv[1][1] == 'h':
        print("USAGE")
        print("\t./107transfer [num den]*")
        print("DESCRIPTION")
        print("\tnum\tpolynomial numerator defined by its coefficients")
        print("\tden\tpolynomial denominator defined by its coefficients")
        return 1
    return 0

def error(argv):
    if len(argv) < 3 or len(argv) % 2 == 0:
        sys.stderr.write("Error: not enough argument\n")
        return -1
    for i in range(1, len(argv)):
        for x in range(0, len(argv[i])):
            if ((argv[i][x] < '0' or argv[i][x] > '9') and argv[i][x] != '.' and argv[i][x] != '*' and argv[i][x] != '-'):
                sys.stderr.write("SyntaxError: invalid syntax\n")
                return -1
            if x == len(argv[i]) - 1 or x == 0:
                if argv[i][x] == '*':
                    sys.stderr.write("SyntaxError: invalid syntax\n")
                    return -1
            else:
                if argv[i][x] == '*' and argv[i][x + 1] == '*':
                    sys.stderr.write("SyntaxError: invalid syntax\n")
                    return -1
    for i in range(1, len(argv)):
        if len(argv[i]) == 1:
            if argv[i] == '0':
                sys.stderr.write("SyntaxError: invalid syntax\n")
                return -1
    return 0

def main(argv):
    if len(argv) == 1:
        sys.stderr.write("Error: not enough argument\n")
        return 84
    if display_h(argv) == 1:
        return 0
    if error(argv) < 0:
        return 84
    calc_transfer(argv, len(argv) - 1)
    return 0