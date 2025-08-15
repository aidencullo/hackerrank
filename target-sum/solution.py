#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findOptimalSequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER size
#  2. LONG_INTEGER target_sum
#

def target_sum(nums, target):
    """
    Find all unique combinations of numbers that sum to the target value.
    
    Args:
        nums: List of integers
        target: Target sum to achieve
        
    Returns:
        List of lists containing valid combinations
    """
    def backtrack(start, curr_sum, path):
        if curr_sum == target:
            result.append(path[:])
            return
        
        for i in range(start, len(nums)):
            if curr_sum + nums[i] > target:
                break
            path.append(nums[i])
            backtrack(i, curr_sum + nums[i], path)
            path.pop()
    
    nums.sort()  # Sort to avoid duplicates and optimize
    result = []
    backtrack(0, 0, [])
    return result


def main():
    # Example usage
    nums = [2, 3, 6, 7]
    target = 7
    
    print(f"Numbers: {nums}")
    print(f"Target: {target}")
    
    combinations = target_sum(nums, target)
    print(f"Valid combinations: {combinations}")


if __name__ == "__main__":
    main()
