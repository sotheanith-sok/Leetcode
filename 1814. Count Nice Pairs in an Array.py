"""
Problem:
    You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

    Example 1:
    Input: nums = [42,11,1,97]
    Output: 2
    Explanation: The two pairs are:
    - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
    - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
    
    Example 2:
    Input: nums = [13,10,35,24,76]
    Output: 4

Solution:
    Let a and b be some arbitrary numbers that match above condition. 
    ie  a + rev(b) == b + rev(a)
    or  a - rev(a) == b - rev(b)

    Thus, we can pair two numbers if their difference between a number and its reverse are the same. Thus, use dict (similar to leetcode 1) find how many previous numbers can be pair with the current number. Add the count to the result and continue to the next number.

Complexity:
    Time: O(nlogm) where n is the count of numbers and m is the length of the longest number
    Space: O(n)
"""

from collections import  defaultdict

class Solution:
    def countNicePairs(self, nums: list[int]) -> int:

        # Reverse number
        def reverseInt(num):
            res = 0
            while num > 0:
                num, remains = divmod(num, 10)
                res = res * 10 + remains

            return res

        # Initialize a dict to keep track of count of previous number based on the difference
        prev = defaultdict(int)

        # Intialize the result
        res = 0

        # Iterate through all numbers
        for num in nums:
            
            # Calculate the difference
            diff = num - reverseInt(num)

            # Add the count of previous numbers that match the difference to the result and increment count of numbers that have such difference by 1
            res, prev[diff] = res + prev[diff], prev[diff] + 1

        return res % (10 ** 9 + 7)
