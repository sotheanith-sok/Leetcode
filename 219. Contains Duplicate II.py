"""
Problem:
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

    Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

    Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

    Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false


Solution:
    Use a set to store previous k numbers. Iterate through all numbers. If there are more than k numbers in the set, remove the first number that was added into the set. Then, check if the current number is in the set. If yes, return True. Else, add the current number into the set and continue. Return False if we can't find a solution.

Complexity:
    Time: O(n)
    Space: O(k)
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        # Find the length of numbers
        n = len(nums)

        # Initialize a set to store k previous numbers
        prev = set()

        # Intialize a pointer pointed to the first number that was added into the set
        p = 0

        # Iterate through all numbers
        for num in nums:

            # If we have more than k numbers in the set, remove the first number that was added into the set
            if len(prev) == k + 1:
                prev.remove(nums[p])
                p += 1

            # Return True if the current number exists in the set
            if num in prev:
                return True

            # Add the current number into the set
            prev.add(num)

        # Return False if we can't find a solution
        return False
