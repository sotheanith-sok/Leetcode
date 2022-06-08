""" 
Problem:
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

    Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Solution (Binary Search):
    Do a simple binary search. Use two pointers and check if the value at the mid pointer is equal to the target. If it is, return the mid pointer. Else, if it is less than the target, search the right side. Otherwise, search the left side. Repeat until the left pointer is more than the right pointer. 
    If you can't find the target, return -1. 

Complexity: 
    Time: O(logn)
    Space: O(1)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

            pass

        return -1
