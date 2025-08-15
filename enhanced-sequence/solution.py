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
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    userKey = input()

    systemKey = input()

    result = calculateEnhancedSequences(userKey, systemKey)

    fptr.write(str(result) + '\n')

    fptr.close()
