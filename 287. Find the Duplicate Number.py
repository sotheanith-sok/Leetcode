"""
Problem:
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.

    Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2
    
    Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Solution:
    Use floyd cycle detection algorithm to find the starting node of a cycle. Start with a slow and a fast pointers placed at the 0th node. Slow will move at the pace of 1 and fast will move at the pace of 2. Two pointers will meet if there is a cycle. Then, reset one of the pointer to the 0th node. Move both pointers at the pace of 1. They will meet again at the node that start the cycle. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        # Intialize the two pointers
        slow, fast = 0, 0

        # Find the first meeting node
        while slow == 0 or slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]

        # Find the start of the cycle
        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow

