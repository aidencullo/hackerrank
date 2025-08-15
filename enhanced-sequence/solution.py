#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateEnhancedSequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING userKey
#  2. STRING systemKey
#

def calculateEnhancedSequences(userKey, systemKey):
    # Write your code here
    def explore(user_index, system_index):
        nonlocal total
        if system_index == m and user_index == n:
            return
        if system_index == m:
            total += 2 ** ((n - 1) - (user_index - 1))
            return
        if user_index == n:
            return

        if userKey[user_index] > systemKey[system_index]:
            total += 2 ** ((n - 1) - user_index)
        elif userKey[user_index] < systemKey[system_index]:
            explore(user_index + 1, system_index)
        else:
            explore(user_index + 1, system_index)
            explore(user_index + 1, system_index + 1)


    n = len(userKey)
    m = len(systemKey)
    total = 0
    explore(0, 0)
    return total  % (10^9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    userKey = input()

    systemKey = input()

    result = calculateEnhancedSequences(userKey, systemKey)

    fptr.write(str(result) + '\n')

    fptr.close()
