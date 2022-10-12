"""
Problem:
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

    Example 1:
    Input: nums = [2,1,2]
    Output: 5
    
    Example 2:
    Input: nums = [1,2,1]
    Output: 0

Solution:
    Sort nums and iterate through it from the end. Let c be current number and a and b be the two numbers to the left of the current number. If a + b <= c, then all combinations of numbers from 0 to b must be less than c. Thus, we need to decrement c and repeat the process until we found a, b, and c that satisfy a + b < c

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:

        # Find the length of numbers
        n = len(nums)

        # Sort numbers
        nums.sort()

        # Iterate through all numbers
        for i in range(n - 1, 1, -1):

            # Find a, b, c
            a, b, c = nums[i - 2], nums[i - 1], nums[i]

            # If we found three numbers that satisfy a + b < c, return their sum
            if a + b > c:
                return a + b + c

        # Return 0 if we couldn't found one
        return 0

