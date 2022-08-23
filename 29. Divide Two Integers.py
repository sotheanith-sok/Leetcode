"""
Problem:
    Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

    The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

    Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = 3.33333.. which is truncated to 3.
    
    Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Solution:
    We will do bit-wise division. Let Q = N/D where N is the dividend and D is the divisior
        1. Convert N and D to a positive number
        2. Let n be the different of the bit length of N and D
        3. Left shift D by n
        4. t = N-D (we can do this instead of N/D because we are working with base 2)
        5. If t >= 0, assign 1 bit to the least significant bit of the result and N = t
        6. Left shift result by 1
        7. Left shift N by 1
        8. Go to step 2 and repeat n times
        9. Right shift result by 1 and return the correct result

    Ex: Do bit-wise division but with based 10
        N = 1500    D = 30      n = 2

        n       N       D       N/D         result    
        0       1500    3000    -1500       0
        1       15000   3000    5           5
        2       0       3000    0           0

        res = 50

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Keep track if the result will be a negative number or not
        neg = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)

        # Convert dividend and divisor to a positive number
        dividend, divisor = abs(dividend), abs(divisor)

        # If dividend is less than divisor, return 0
        if dividend < divisor:
            return 0

        # Check the bit lengths of both numbers
        n = dividend.bit_length() - divisor.bit_length()

        # Left shift divisior by n bits
        divisor <<= n

        # Initialize the result
        res = 0

        # Start dividing
        for _ in range(n + 1):

            # Calculate the difference between the two numbers
            diff = dividend - divisor

            # If the difference is bigger than 0
            if diff >= 0:

                # Set the lsb of the result to 1
                res |= 1

                # Set dividend as the difference
                dividend = diff

            # Left shift result
            res <<= 1

            # Left shift dividend
            dividend <<= 1

        # Right shift the result due to the extra shift from the last division
        res = res >> 1

        return max(-res, -(2 ** 31)) if neg else min(res, 2 ** 31 - 1)



