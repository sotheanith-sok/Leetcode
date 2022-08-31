"""
Problem:
    Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.

    Example 1:
    Input: num = 33
    Output: [10,11,12]
    Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
    10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
    
    Example 2:
    Input: num = 4
    Output: []
    Explanation: There is no way to express 4 as the sum of 3 consecutive integers.

Solution:
    Do some math to solve this problem. Let x be the middle number of the three consecutive numbers that added to num aka 
        (x-1) + x + (x+1) == num
        3x == num
        x == num/3

Complexity:
    Time: O(1)
    Space: O(1)
"""


class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        res, remains = divmod(num, 3)
        return [res - 1, res, res + 1] if remains == 0 else []

