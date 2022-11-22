""" 
Problem:
    Given an integer n, return the least number of perfect square numbers that sum to n.

    A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

    Example 1:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.
    
    Example 2:
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.

Solution:
    With Lagrange's four-square theorem, we know that any natural numbers can be written as a sum of 4 integer squares. Thus, the largest possible answer is 4. 

    1. n is a perfect square 

    2. n is a sum of two perfect square:
        Pick a number from 1 to n as the first integer square. Then, check if the difference between n and the first integer square is also a perfect square. 

    3. n is a sum of three perfect square:
        By Legendre's three-square theorem, n is a sum of three perfect square if and only if it doesn't have a form n = 4**a (8b+7) for some arbitrary a and b. We can check for this case by continue to divide n by 4 until it isn't divisible by 4 anymore. Then, we check if the remain of n divde by 8 is not equal to 7.

    4. n is a sum of four perfect square:
        This is the base case. 

Complexity: 
    Time: O(sqrt(n))
    Space: O(1)
"""


from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:

        # 1. Check if n is a perfect square
        if isqrt(n) ** 2 == n:
            return 1

        # 2. Check if n is a sum of two perfect squares
        for i in range(1, n):
            if i**2 > n:
                break
            
            # Calculate the difference between n and the first perfect square
            diff = n - i**2

            # Check if the difference is a perfect square
            if isqrt(diff) ** 2 == diff:
                return 2

        # 3. Check if n is a sum of three perfect squares
        while n % 4 == 0:
            n /= 4

        if n % 8 != 7:
            return 3

        # 4. n is a sum of 4 perfect squares
        return 4
