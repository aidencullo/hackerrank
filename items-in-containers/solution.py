#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#

def numberOfItems(s, startIndices, endIndices):
    # Write your code here
    
    # Time Complexity: O(n + m) where n = number of queries, m = length of string
    # Space Complexity: O(m) for storing prefix sums and pipe positions
    
    m = len(s)
    
    # Precompute prefix sums for items
    item_prefix = [0] * (m + 1)
    for i in range(m):
        item_prefix[i + 1] = item_prefix[i] + (1 if s[i] == '*' else 0)
    
    # Precompute next pipe positions (from left to right)
    next_pipe = [m] * m
    last_pipe_pos = m
    for i in range(m - 1, -1, -1):
        if s[i] == '|':
            last_pipe_pos = i
        next_pipe[i] = last_pipe_pos
    
    # Precompute previous pipe positions (from right to left)
    prev_pipe = [-1] * m
    first_pipe_pos = -1
    for i in range(m):
        if s[i] == '|':
            first_pipe_pos = i
        prev_pipe[i] = first_pipe_pos
    
    result = []
    for i in range(len(startIndices)):
        start_idx = startIndices[i] - 1  # Convert to 0-based
        end_idx = endIndices[i] - 1
        
        # Find the first pipe >= start_idx
        first_pipe_idx = next_pipe[start_idx]
        
        # Find the last pipe <= end_idx
        last_pipe_idx = prev_pipe[end_idx]
        
        # If no valid pipes found, return 0
        if first_pipe_idx >= m or last_pipe_idx < 0 or first_pipe_idx >= last_pipe_idx:
            result.append(0)
        else:
            # Count items between the pipes using prefix sums
            count = item_prefix[last_pipe_idx] - item_prefix[first_pipe_idx + 1]
            result.append(count)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
