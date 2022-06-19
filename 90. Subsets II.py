"""
Problem:
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.

    Example 1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    
    Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Solution:
    A list A is a subset of a list B if all elements in A exists in B (order does not matter). Thus, we will sort nums. For each value, we have two decisions. If we add it to a list, we will continue to the next element in nums. If we don't add it to a list, we will skip the next element and all subsequent elements that have the same value. Once, we reach the end of nums, we append the subset to the result. 

Complexity:
    Time: O(n**2)
    Space: O(2**n)

"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):

            # Add the subset to the result once we reach the end of nums.
            if i == len(nums):
                # Add a copy of the list instead of the reference.
                res.append(subset[::])
                return

            # If we pick this element, continue to the next element
            backtrack(i + 1, subset + [nums[i]])

            # If we don't pick this element, we will skip all subsequent elements that have the same values.
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i = i + 1
            backtrack(i + 1, subset)

        backtrack(0, [])

        return res

