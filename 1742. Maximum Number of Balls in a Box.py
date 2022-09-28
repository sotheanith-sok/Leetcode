"""
Problem:
    You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

    Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

    Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

    Example 1:
    Input: lowLimit = 1, highLimit = 10
    Output: 2
    Explanation:
    Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
    Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
    Box 1 has the most number of balls with 2 balls.
    
    Example 2:
    Input: lowLimit = 5, highLimit = 15
    Output: 2
    Explanation:
    Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
    Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
    Boxes 5 and 6 have the most number of balls with 2 balls in each.
    
    Example 3:
    Input: lowLimit = 19, highLimit = 28
    Output: 2
    Explanation:
    Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
    Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
    Box 10 has the most number of balls with 2 balls.

Solution:
    We will calculate all ball numbers from lowLimit to highLimit to find which box each ball fall into. However, we can avoid some repeated work by splitting each num into offset(num[:-1]) and index(num[-1]). Then, we can sum up all digits in offset and cache the result. 

Complexity:
    Time: O(nlogm) where n is the number of ball and m is the number of digits of the largest ball number.
    Space: O(k) where k is equal to highLimit//10
"""


from functools import lru_cache


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        # Calculate sum of all digits in a number and cache the result
        @lru_cache(None)
        def pSum(num):
            res = 0
            while num != 0:
                num, remin = divmod(num, 10)
                res += remin
            return res

        # Keep track of counts of each box
        counts = [0] * 46

        # Iterate through all ball numbers
        for num in range(lowLimit, highLimit + 1):

            # Split each number into the offset and index
            offset, i = divmod(num, 10)

            # Update the count of the corresponding box
            counts[pSum(offset) + i] += 1

        return max(counts)
