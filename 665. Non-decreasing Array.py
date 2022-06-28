""" 
Problem:
    Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

    Example 1:
    Input: nums = [4,2,3]
    Output: true
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
    
    Example 2:
    Input: nums = [4,2,1]
    Output: false
    Explanation: You can't get a non-decreasing array by modify at most one element.

Solution:
    To maintain a non-decreasing order, we will check each pair of values in nums and make sure that value 1 is less than or equal to value 2. Thus, if value 2 less than value 1, we will want to update value 1 to be value 2. However, there is a edge case that we have to consider. If there exists a value before value 1 that is larger than value 2, we have to set value 2 to value 1 instead in order to maintain a non-decreasing order. Repeat the process until we have iterate through nums and return True. Or return False we have to make if we can't maintain a non-decreasing order after an edit.  

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:

        # Keep track of if we did a edit
        edit = False

        # Iterate through nums
        for i in range(len(nums) - 1):

            # If value 1 is larger than value 2
            if nums[i] > nums[i + 1]:

                # If we have edited before, return False
                if edit:
                    return False

                # If value 2 is also larger than or equal to the value before value 1, update value 1 to the value at value 2. ie [2,7,3] -> [2,3,3]
                if i == 0 or nums[i + 1] >= nums[i - 1]:
                    nums[i] = nums[i + 1]

                # Else, update value 2 to value 1. ie [2,7,1] -> [2,7,7]
                else:
                    nums[i + 1] = nums[i]

                # Update the edit
                edit = True

        return True

