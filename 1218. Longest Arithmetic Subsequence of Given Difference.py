"""
Problem:
    Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

    A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

    Example 1:
    Input: arr = [1,2,3,4], difference = 1
    Output: 4
    Explanation: The longest arithmetic subsequence is [1,2,3,4].
    
    Example 2:
    Input: arr = [1,3,5,7], difference = 1
    Output: 1
    Explanation: The longest arithmetic subsequence is any single element.
    
    Example 3:
    Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
    Output: 4
    Explanation: The longest arithmetic subsequence is [7,5,3,1].

Solution:
    Use dynamic programming to solve this problem. Longest sequence at starting at some arbritary num is 1 + longest sequence starting at (num+diff) of the right subarray of num. 

    ie dp(num) = 1 + dp(num + diff)

    Thus, we can solve this problem in two ways
    1. Top-down
        For the top-down dp, we will add all indices of numbers in arr into a dict such that we only have to search through indices of a next number. Then, start by calling dp on all numbers. For each dp call, calculate the next number and recursively call dp on such number if it exists at right side of the current number. Lastly, return the maximum of all dp call.

    2. Bottom-up
        Use a dict to maintain the longest sequence start at a number. Start from the end of arr. For each number, its longest sequence is 1 plus the longest sequence of the next number. Lastly, return the maximum of all values in the dict. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

# Top-down
from collections import defaultdict
from functools import lru_cache


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:

        # Save all values in the arr and its indices into a dict
        indices = defaultdict(list)
        for i, v in enumerate(arr):
            indices[v].append(i)

        # Get length of arr
        n = len(arr)

        # Recursively calculate the longest sequence starting from a number at index i
        @lru_cache(None)
        def longest(i):

            # Calculate the next number
            nextNum = arr[i] + difference

            # Iterate through all indices of the next number
            for j in indices[nextNum]:

                # If the current indices is less than or equal to i, continue
                if j <= i:
                    continue

                # Recrusively calculate the longest sequence starting from the next number at the right side of i
                return 1 + longest(j)

            # Return 1 if there is no next number
            return 1

        # Return the longest sequence starting from al numbers
        return max(longest(i) for i in range(n))


# Bottom-up
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:

        # Find the length of n
        n = len(arr)

        # A cache to keep track of the longest sequence starting at a number
        longest = defaultdict(int)

        # Itearte from the last number
        for i in range(n - 1, -1, -1):

            # Calcualte the longest sequence starting from the current number
            longest[arr[i]] = 1 + longest[arr[i] + difference]

        # Return the longest sequence starting from all numbers
        return max(longest.values())

