""" 
Problem:
    Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    
    Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1
    
    Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

Solution:
    Since we are trying to find a minimum subarray where its sum is larger than the target, we will use a sliding window technique with a left and a right pointer. Initially, we will set the minimum subarray to be something large (len(arr) + 1) and iterate through all values in the array. The right pointer will iterate through all values in the array and add them to the total. At each iteration, while total is larger than target, we try calculate the windows size and compare it to the previous minimum length and we take the minimum. Finally, return the minimum length if it is valid. Else, return 0.   

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        N = len(nums)

        # Initialize the left pointer, total, and minimum subarray size.
        l, total, min_len = 0, 0, N + 1

        # Iterate through all numbers using the right pointer
        for r in range(N):

            # Add value at the right pointer to the total
            total += nums[r]

            # While total is larger than target and l is less than equal right. Try to shrink the window by increment the left pointer. 
            while total >= target and l <= r:
                min_len = min(min_len, r - l + 1)
                total -= nums[l]
                l += 1

        # Return valid minimum size of the subarray or 0
        return 0 if min_len == N + 1 else min_len

