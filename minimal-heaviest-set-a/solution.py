#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimalHeaviestSetA(arr):
    # Write your code here
    arr.sort()
    total = sum(arr)
    running = 0
    n = len(arr)
    for i in range(n - 1, -1, -1):
        el = arr[i]
        running += el
        if running > total - running:
            return arr[i:]
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minimalHeaviestSetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
