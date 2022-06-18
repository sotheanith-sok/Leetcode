""" 
Problem:
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    
    Example 2:
    Input: nums = [0]
    Output: [0]

Solution:
    We will use two pointers. The left pointer will point to the slot we have to insert the number in and the right pointer will iterate through all values in nums. At each iteration, if the value at the right pointer is non zero, insert it into the left pointer slot and increment the left pointer. 

Complexity:
    Time: O(n)
    Space: O(1)

"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l =0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1


