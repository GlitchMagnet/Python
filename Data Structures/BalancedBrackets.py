#!/bin/python3

import sys

def isBalanced(string):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for char in string:
        if not stack:
            stack.append(char)
        elif char not in table:
            stack.append(char)
        elif table[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        print("NO")
    else:
        print("YES")
    # Complete this function

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        isBalanced(input())
