"""
Problem:
    Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

    A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

    0 <= i, j < nums.length
    i != j
    nums[i] - nums[j] == k
    Notice that |val| denotes the absolute value of val.

    Example 1:
    Input: nums = [3,1,4,1,5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.
    
    Example 2:
    Input: nums = [1,2,3,4,5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
    
    Example 3:
    Input: nums = [1,3,1,5,4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Solution:
    If k == 0, return the number of numbers that occrued at least twice in nums.
    
    If k != 0, we will use the lookback technique to solve this problem (similiar to leetcode 1). Use a set to maintain previous numbers. Iterate through all numbers. If the current number (n) exists previously, skip it. Else, check if there exists a previous number where the difference between the two numbers is equal to k. 
    
    ie a - b = k
    1. let the current num = a, prev num = b
        => prev num = current num - k
    2. let the current num = b, prev num = a
        => prev num = k + current num

Complexity:
    Time: O(n)
    Space: O(n)
"""
from collections import Counter


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:

        # If k == 0, return the number of numbers that occured at least twice
        if k == 0:
            return sum(1 for c in Counter(nums).values() if c >= 2)

        # Else, if k != 0

        # Initialize a set to keep track previous numbers and a result
        prev, res = set(), 0

        # Iterate through all numbers
        for n in nums:

            # If the current number exists previously, skip it
            if n in prev:
                continue

            # Else, check if there is a previous number such that the difference between the two is equal to k
            if k + n in prev or n - k in prev:

                # If yes, update the result
                # Given set = [6, 2], k =2, and n = 4
                # k+n will check for (6, 4)
                # n-k will check for (4, 2)
                res += (k + n in prev) + (n - k in prev)

            # Add the current number to the set
            prev.add(n)

        return res

