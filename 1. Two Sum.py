"""
Problem:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    
    You can return the answer in any order.
    
    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    
    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Solution (Dynamic Programming):
    Use a hashmap to keep tracks of previous values and indices (val -> index). For each number in the list, calculate the difference between its value and the target value. If the difference exists in the hashmap, you found the answer.   

Complexity
    Running Time: O(n)
    Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap.keys():
                return [hashmap[diff], i]

            hashmap[num] = i