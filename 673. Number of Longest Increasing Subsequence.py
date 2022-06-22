""" 
Problem:
    Given an integer array nums, return the number of longest increasing subsequences.

    Notice that the sequence has to be strictly increasing.

    Example 1:
    Input: nums = [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
    
    Example 2:
    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

Solution:
    We will solve this problem backward using dynamic programming. At each num starting from the last number in nums, we assume that the max length and count are 1. Then, we check length and count of subsequent numbers if such numbers are less than the target number. If the current length is larger than the max length, we set max length and max count to the current length and count. Else if the current length is equal to max length, increment the max count by current count. Finally, update the global max length and the global max count following the same logic and save the max length and count into the cache.   

Complexity:
    Time: O(n**2)
    Space: O(n)
"""


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        # A cache to store indices ->(maxLength, maxCount)
        cache = {}

        # Global varaibles for tracking maxLength and maxCount
        globalMaxLength, globalMaxCount = 0, 0

        for i in range(len(nums) - 1, -1, -1):

            # Assume that maxLength and maxCount are 1 initially
            maxLength, maxCount = 1, 1

            # Check all subsequent numbers
            for j in range(i + 1, len(nums)):

                # If a subsequent number is larger than the current number
                if nums[j] > nums[i]:

                    # Find the length and count of such subsequent number
                    length, count = cache[j]

                    # If such subsequent number is a part of a LIS length larger than the current maxLength
                    if length + 1 > maxLength:

                        # Set the maxLength and maxCount to its length and count.
                        maxLength, maxCount = length + 1, count

                    # Else if such subsequent number is a part of a LIS length equal to the current maxLength
                    elif length + 1 == maxLength:

                        # Increment the maxCount by its count
                        maxCount += count

            # If the current maxLength is larger than the global maxLength, update the global maxLength and maxCount
            if maxLength > globalMaxLength:
                globalMaxLength, globalMaxCount = maxLength, maxCount

            # Else, If the current maxLength is equal to the global maxLength, increment the global maxCount by the current maxCount
            elif maxLength == globalMaxLength:
                globalMaxCount += maxCount

            # Store the current maxLength and maxCount into the cache.
            cache[i] = [maxLength, maxCount]

        return globalMaxCount
