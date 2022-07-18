"""
Problem:
    Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

    Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000
    
    Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100
    
    Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

Solution:
    Normal power operation will take O(n) time because we have to multiply x by itself n time. However, we can reduce the complexity to O(logn) by imagining n to be a power of 2. For example, x**9 is equal to x**8 * x**1 or x**(2**3) * x**(2**0). Thus, we can see that everytime, we see a 1 bit, we will multiply the result by x and for every bit, we will raise x to the power of 2. 

    ie x ** 9 => 9 : 1001
    bit x       res
    1   x**1    x**1
    0   x**2    x**1
    0   x**4    x**1
    1   x**8    x**1 * x**8

Complexity:
    Time: O(logn) since we shift bit by 1 everytime and this operation is the same as n/2
    Space: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Remember if n is a positive or negative number
        pos = True if n >= 0 else False

        # Change n to a positive number
        n = abs(n)

        # Initialize the result
        res = 1

        # While n is larger than 0
        while n != 0:

            # Check if the last bit is 1,
            if n & 1 == 1:

                # If yes, multiply the result by x
                res *= x

            # Shift the bit right by 1
            n >>= 1

            # Raise x to the power of 2
            x = x * x

        # Return inverse if n was a negative number
        return res if pos else (1.0 / res)
