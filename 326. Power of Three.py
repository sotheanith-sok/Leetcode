"""
Problem:
    Given an integer n, return true if it is a power of three. Otherwise, return false.

    An integer n is a power of three, if there exists an integer x such that n == 3x.

    Example 1:
    Input: n = 27
    Output: true
    
    Example 2:
    Input: n = 0
    Output: false
    
    Example 3:
    Input: n = 9
    Output: true

Solution:
    This is some black magic stuff. Basically, if n is a power of some prime number k, it must be a unique prime factorization composed of k only and thus, it should be divisible only by other unique prime factorization of k. aka 3**19 is divisible by 3**x where x = 1, 2,..., 19.

        ie. n = 729 k = 3
            n == 3**6 

            3**19 % 3**6 == 0
    
    However, if k is not a prime number, then n can not be a unique prime factorization composed of k only and thus, there might exists some arbitrary number m (m is a power k) that is divisible by n (n is not a power of k)     

        ie. n = 8, k = 4
            n == 2**4

            4**2 % 2**4 = 0


Complexity:
    Time: O(1)
    Space: O(1)
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        return n > 0 and 3 ** 19 % n == 0

