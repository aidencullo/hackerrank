#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    # Write your code here

    def dfs(i):
        if i in seen:
            return 0
        
        seen.add(i)
        
        for j in graph[i]:
            dfs(j)

        return 1
        
        
    seen = set()
    from collections import defaultdict
    graph = defaultdict(list)

    n = len(related)
    m = len(related[0])

    for i in range(n):
        for j in range(m):
            if related[i][j] == '1':
                graph[i].append(j)

    total = 0
    for i in range(n):
        total += dfs(i)

    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    related_count = int(input().strip())

    related = []

    for _ in range(related_count):
        related_item = input()
        related.append(related_item)

    result = countGroups(related)

    fptr.write(str(result) + '\n')

    fptr.close()
