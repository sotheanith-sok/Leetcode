"""
Problem:
    Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

    Example 1:

    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].
    
    Example 2:
    Input: low = 8, high = 10
    Output: 1
    Explanation: The odd numbers between 8 and 10 are [9].

Solution:
    We can find the count of odd numbers using the following formula.

    1. If low is even: count = ceil((high - low) / 2)
    2. If low is odd: count = floor((high - low) / 2) + 1


    low     high        res
    0       0           0
    0       1           1
    0       2           1
    0       3           2
    0       4           2
    0       5           3
    0       6           3

    1       1           1
    1       2           1
    1       3           2
    1       4           2 
    1       5           3
    1       6           3


Complexity:
    Time: O(1)
    Space: O(1)
"""

from math import ceil, floor


class Solution:
    def countOdds(self, low: int, high: int) -> int:

        return ceil((high - low) / 2) if low % 2 == 0 else floor((high - low) / 2) + 1
