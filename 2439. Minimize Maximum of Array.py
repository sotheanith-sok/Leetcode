"""
Problem:
    You are given a 0-indexed array nums comprising of n non-negative integers.

    In one operation, you must:

    Choose an integer i such that 1 <= i < n and nums[i] > 0.
    Decrease nums[i] by 1.
    Increase nums[i - 1] by 1.
    Return the minimum possible value of the maximum integer of nums after performing any number of operations.

    Example 1:
    Input: nums = [3,7,1,6]
    Output: 5
    Explanation:
    One set of optimal operations is as follows:
    1. Choose i = 1, and nums becomes [4,6,1,6].
    2. Choose i = 3, and nums becomes [4,6,2,5].
    3. Choose i = 1, and nums becomes [5,5,2,5].
    The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
    Therefore, we return 5.
    
    Example 2:
    Input: nums = [10,1]
    Output: 10
    Explanation:
    It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

Solution:
    Since decreasing a value will increase a neighboring value to its left, all values can be distributed to the left. Iterate through all values while keep tracking of the current floor and the number of free spaces. 
    
    If the difference between the current value and the floor is greater than the available free spaces, we have to raise the floor using the following steps:

        1. Calculate the remaining value after filling all free spaces.
        2. Find how many times we have to raise the floor such that the remaining value are evenly distributed to all previous values
        3. Update the floor and free spaces

    Lastly, calculate the remaining free spaces after distributed the current value to the left.


Complexity:
    Time: O(n)
    Space: O(1)
"""


from math import ceil


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:

        # Find the length of numbers
        n = len(nums)

        # Intialize the floor and free spaces
        floor, freeSpaces = nums[0], 0

        # Iterate through all numbers
        for i in range(1, n):

            # If the difference between the current value and the floor is greater than the free spaces, we have to raise the floor
            if nums[i] - floor > freeSpaces:

                # Calculate the remaining value after we filled all available free spaces
                values = nums[i] - floor - freeSpaces

                # Calculate how many times we have to raise the floor such that the remaining values can be distributed evenly to the left
                multiplier = ceil(values / (i + 1))

                # Update the new floor
                floor += multiplier

                # Update the new free spaces
                freeSpaces += multiplier * i

            # Calculate the remaining free spaces after distributed the current value to the left
            freeSpaces += -(nums[i] - floor)

        return floor
