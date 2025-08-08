#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#

def processLogs(logs, threshold):
    # Write your code here
    
    # Time Complexity:
    # - Average Case: O(n log n) where n = number of logs
    # - Worst Case: O(n² + k log k) if dict ops take O(i) time where i = current entries
    # Space Complexity:
    # - Average Case: O(k) where k = unique users
    # - Worst Case: O(n) when all users are unique
    
    from collections import defaultdict
    transactions = defaultdict(int)
    for log in logs:
        user_a, user_b, _ = log.split()
        for user in set((user_a, user_b)):
            transactions[user] += 1
    return sorted(list(filter(lambda x: transactions[x] >= threshold, transactions)), key=lambda x: int(x))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
