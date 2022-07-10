""" 
Problem:
    Given an integer array nums and an integer k, return the number of good subarrays of nums.

    A good array is an array where the number of different integers in that array is exactly k.

    For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
    A subarray is a contiguous part of an array.

    Example 1:
    Input: nums = [1,2,1,2,3], k = 2
    Output: 7
    Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
    
    Example 2:
    Input: nums = [1,2,1,3,4], k = 3
    Output: 3
    Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Solution:
    It is hard to find all substrings that contains k exact unique numbers as we have to check every substrings. However, it is easier to find all substring that contains at most k unique numbers. Thus, we will split this problem into two calls: atMost(k) and atMost(k-1). 

    To find all substrings that contains at most k unique numbers, we use a sliding window and keep expanding it while tracking the number of unique numbers. If it surpasses k unique numbers, we will shrink the window back until we have a valid window. At each expansion, we will add the size of the window into the result. The intuition behind this is that for a list of size n, we can have n*(n-1)/2 substrings or (n)(n-1)(n-2)(n-3)...1. 
    ie max window size = 7
        size: 0     numbers of substring: 0
        size: 1     numbers of substring: 1 + 0 
        size: 2     numbers of substring: 2 + 1 + 0
        size: 3     numbers of substring: 3 + 2 + 1 + 0
        size: 4     numbers of substring: 4 + 3 + 2 + 1 + 0
        size: 5     numbers of substring: 5 + 4 + 3 + 2 + 1 + 0
        size: 6     numbers of substring: 6 + 5 + 4 + 3 + 2 + 1 + 0
                    Total substrings: 21
Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        # Find substrings contain at most k unique numbers
        def atMost(k):

            # Initialize the count
            count = Counter()

            # Initialize the res and the left pointer
            res = l = 0

            # Iterate through all numbers with the right pointer
            for r in range(len(nums)):

                # Update the count
                count[nums[r]] = count[nums[r]] + 1 if nums[r] in count else 1

                # Shrink the window if it is no longer valid
                while len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        count.pop(nums[l])
                    l += 1

                # Add the size of the window to the result
                res += r - l + 1

            return res

        return atMost(k) - atMost(k - 1)

