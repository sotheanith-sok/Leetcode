"""
Problem:
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

    Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.
    
    Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.
    
    Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Solution:
    Solve this problem using thresholding. Let t1 and t2 be the threshold where t1 is the smallest number and t2 be the next smallest number. Initialize t1 and t2 to infinity.
    
    Iterate through nums. If the current number is less than or equal to t1, set t1 to such number and continue. Else if the current number is less than or equal to t2, set t2 to such number and continue. Else, the current number must be greater than t2 and this is only possible if there exists a previous number that less than t2 because if there isn't, then t2 will be still be infinity. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


from math import inf


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        # If there are less than 3 numbers, return False
        if len(nums) < 3:
            return False

        # Initialize the two thresholds to infinity
        t1, t2 = inf, inf

        # Iterate through nums
        for num in nums:

            # If the current number is less than or equal to the first threshold, update such threshold
            if num <= t1:
                t1 = num
                continue

            # If the current number is less than or equal to the second threshold, update such threshold
            if num <= t2:
                t2 = num
                continue

            # Else, return True because the current number must be greater than the second threshold and the second threshold must be greater than a previous number
            return True

        return False

