"""
Problem:
    Given an unsorted integer array nums, return the smallest missing positive integer.

    You must implement an algorithm that runs in O(n) time and uses constant extra space.

    Example 1:
    Input: nums = [1,2,0]
    Output: 3
    
    Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2
    
    Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1

Solution:
    Start by extending nums by 1 such that its indices will be between 0 and n. 0 index will be used to store all values that is out of the valid range aka numbers<1 or numbers>n.

    ie.     nums = 3, 4, -1, 1], n = 4
    
            nums = [3, 4, -1, 1, 0], n = 5

    
    Then, iterate through nums and change out of range numbers to 0.

    ie.     nums = [3, 4, -1, 1, 0]
    
            nums = [3, 4, 0, 1, 0]


    Next, iterate through nums and count how many time we see each number by using such number as an index and increment the value at such index by n+1. This approach allows us to extract the original number by modding the value by n+1.

    ie.     nums = [3, 4, 0, 1, 0], n = 5

            nums = [13, 9, 0, 6, 5]

    Lastly, iterate through nums and find the first number that isn't a multiple of n+1. This will be the first missing positive number. If we couldn't find one, n+1 will be the result. 

    ie.     nums = [13,9,0,6,5]
            res  = 2

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        # Extend nums such that its indicies is between 0 and n
        nums.append(0)

        # Get the length of nums. n+1 in this case
        n = len(nums)

        # Change out of range numbers to 0
        for i in range(n):
            if not (1 <= nums[i] < n):
                nums[i] = 0

        # Count how many time we see each number using each number as an index
        for i in range(n):
            nums[nums[i] % n] += n

        # Find the first number that isn't a multiple of n+1
        for i in range(1, n):
            if nums[i] // n == 0:
                return i

        # If we can't find such number, n+1 is the result
        return n

