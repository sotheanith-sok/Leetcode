"""
Problem:
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
    
    Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
    
    Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Solution:
    Use binary search to find the target value. If we found it, return the index. Else, return one of the two pointers as both of them will point to the index to insert the target such that the list of integers remains sorted.

Complexity:
    Time: O(nlogn)
    Space: O(1)
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        # Initialize the left and right pointers
        l, r = 0, len(nums) - 1

        # Iterate until both pointers cross
        while l <= r:

            # Find the mid pointer
            m = (r - l) // 2 + l

            # If the target is equal to the value at the mid pointer, return the mid pointer
            if target == nums[m]:
                return m

            # Else if the target is less than the value at the mid pointer, search the left partition
            if target < nums[m]:
                r = m - 1

            # Else, search the right parition
            else:
                l = m + 1

        return l
