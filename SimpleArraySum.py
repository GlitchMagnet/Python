#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#

def simpleArraySum(arr):
    sum = 0
    i = len(arr) - 1
    while i >= 0 :
        sum += arr[i]
        i -= 1
    return sum    
    #
    # Write your code here.
    #
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = simpleArraySum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
