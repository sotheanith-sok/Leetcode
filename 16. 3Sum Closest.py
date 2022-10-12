"""
Problem:
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.

    Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
    Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0

Solution:
    Reduce this problem to two sum.
    
    Use three pointers to solve this problem. Start by sorting nums and iterate through nums. At each iteration, use other two pointers to find two numbers such that the sum of numbers at all three pointers sum up as cloest to target. Return the closest sum.  

Complexity:
    Time: O(n**2)
    Space: O(1)
"""


from math import inf


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        # Find the length of numbers
        n = len(nums)

        # Sort nums
        nums.sort()

        # Initialize the result
        res = -inf

        # Iterate through all numbers
        for bound in range(n - 2):

            # Initialize the left and right pointers
            l, r = bound + 1, n - 1

            # While left and right pointers haven't cross each other
            while l < r:

                # Calculate the current sum
                cSum = nums[bound] + nums[l] + nums[r]

                # If the current sum is closer to the target than the previous sum, save it into the result
                if abs(res - target) > abs(cSum - target):
                    res = cSum

                # End the search if current sum is equal to the target
                if cSum == target:
                    return res

                # Elif the current sum is less than the target, increment the left pointer
                elif cSum < target:
                    l += 1

                # Else, decrement the right pointer
                else:
                    r -= 1

        return res
