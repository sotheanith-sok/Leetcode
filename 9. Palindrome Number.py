"""
Problem:
    Given an integer x, return true if x is palindrome integer.

    An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.
    
    Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    
    Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    
    Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Follow up: Could you solve it without converting the integer to a string?

Solution:
    If x is positive, start by finding how many digits to represent such number. Then, continue to divide x by 10 and multiply the remainder with 10**n where n is the place of significant. Accumulate the result and decrement n. Repeat until x is zero. Lastly, return True if x is equal to reversed x. Else, false.
    If x is negative, return false because it is impossible for a negative number to be a palindrome.
    If x is zero, return True 

Complexity:
    Time: O(log10(n))
    Space: O(1)
"""


import math


class Solution:
    def isPalindrome(self, x: int) -> bool:

        # If x is less than 0, return False. Can't make palindrome from a negative number
        if x < 0:
            return False

        # If x is 0, return True
        if x == 0:
            return True

        # Find the number of significant digits requires to represent x
        n = int(math.log10(x))

        # Save x as temp
        temp = x

        # Initialize the reversed x
        reversedX = 0

        # While temp is not zero
        while temp > 0:

            # Divide temp by 10
            temp, re = divmod(temp, 10)

            # Multiply 10**n with the remainder and add it to the reversed x
            reversedX += 10 ** n * re

            # Decrement significant digit
            n -= 1

        return x == reversedX
