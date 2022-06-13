"""
Problem:
    Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

    Example:

    Input: nums = [3,5,2,1,6,4]
    Output: One possible answer is [3,5,1,6,2,4]

Solution:
    The pattern is that the value at odd indices will be larger than the number before and after it. Thus, we can iterate through all odd indices and swap the value at such indices with the max between the three values.

Complexity:
    Time: O(n)
    Space: O(1)

"""

class Solution:
    def wiggleSort(self, nums:list[int]) -> list[int]:
        for i in range(1, len(nums), 2):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            
            if i+1<len(nums) and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        return nums
