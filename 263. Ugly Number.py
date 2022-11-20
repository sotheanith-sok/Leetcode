""" 
Problem:
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return true if n is an ugly number.

    Example 1:
    Input: n = 6
    Output: true
    Explanation: 6 = 2 × 3
    
    Example 2:
    Input: n = 1
    Output: true
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
    
    Example 3:
    Input: n = 14
    Output: false
    Explanation: 14 is not ugly since it includes the prime factor 7.

Solution:
    n has a prime factor of 2, 3, 5 only means that it can be calcuated from a multiple of those three numbers. 
    
    Ex: 172800 = 2**8 * 3**3 * 5**2

    Thus, we can check if n is such a prime number by continue to divide n by those three numbers until it is no longer divisible. Then, we just have to check if n equal 1 at the end. 

Complexity:
    Time: log(n)
    Space: O(1)
"""


class Solution:
    def isUgly(self, n: int) -> bool:

        # If n == 0, return False
        if n == 0:
            return False

        # Continue to divide n by 5 until it is no longer divisible
        while n % 5 == 0:
            n = n / 5

        # Continue to divide n by 3 until it is no longer divisible
        while n % 3 == 0:
            n = n / 3

        # Continue to divide n by 2 until it is no longer divisible
        while n % 2 == 0:
            n = n / 2

        return n == 1
