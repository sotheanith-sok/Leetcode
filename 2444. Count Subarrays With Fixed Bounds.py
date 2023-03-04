"""
Problem:
    You are given an integer array nums and two integers minK and maxK.

    A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

    The minimum value in the subarray is equal to minK.
    The maximum value in the subarray is equal to maxK.
    Return the number of fixed-bound subarrays.

    A subarray is a contiguous part of an array.

    Example 1:
    Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
    Output: 2
    Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
    
    Example 2:
    Input: nums = [1,1,1,1], minK = 1, maxK = 1
    Output: 10
    Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Solution:
    Since a subarray must contains numbers between minK and maxK, any number outside such range will act as a divider and we can consider subarrays to the left and to the right of it independently.

    Iterate through all numbers and find the count of valid subarrays ending at each number.
     
    For a subarray starting from the divider and ending at some arbitrary number, we can shrink such subarray from the left and it will remain valid until it no longer includes minK or maxK. Thus, the count of valid subarrays is equal to the count of numbers starting from divider to the first of the last occurence of minK and maxK.
    
Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        # Initialize three variables to keep track of indices of latest divider, minK, maxK
        div, minLast, maxLast = 0, -1, -1

        # Initialize the result
        res = 0

        # Iterate through all numbers
        for i, num in enumerate(nums):

            # If the current number is a divider, we can disregard all numbers before it
            if not (minK <= num <= maxK):
                div, minLast, maxLast = i + 1, -1, -1
                continue

            # Update the latest indices of minK and maxK
            minLast, maxLast = (
                i if num == minK else minLast,
                i if num == maxK else maxLast,
            )

            # Update the result with the number of valid subarrays ending at the current number if we have seen minK and maxK
            res += (
                min(maxLast, minLast) - div + 1
                if minLast != -1 and maxLast != -1
                else 0
            )

        return res
