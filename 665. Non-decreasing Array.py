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
    To maintain a non-decreasing order, we will check each pair of values in nums and make sure that value 1 is less than or equal to value 2. Thus, in general, we will set both values to the minimum of the two and noted that we have perform an edit. However, there is a edge case that we have to consider. If there exists a value before value 1 that is larger than the minimum of the two values, we have to set both values to the maximum of the two values instead in order to maintain a non-decreasing order. Repeat the process until we have iterate through nums and return True. Or return False we have to make if we can't maintain a non-decreasing order after an edit.  

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

            # If value1 is larger than value 2
            if nums[i] > nums[i + 1]:

                # And we have edited before, return False
                if edit:
                    return False

                # Calculate the min value and the max value  of the two values
                maxV, minV = max(nums[i], nums[i + 1]), min(nums[i], nums[i + 1])

                # Set both values to the min value unless there exists a value before value that is larger than the min value
                nums[i] = nums[i + 1] = maxV if i > 0 and nums[i - 1] > minV else minV

                # Update the edit
                edit = True

        return True

