#!/bin/python3

import sys
from functools import reduce
from operator import xor

def lonely_integer(a):
    return reduce(xor, a)

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
