""" 
Problem:
    Given an integer num, return a string of its base 7 representation.
    Example 1:

    Input: num = 100
    Output: "202"
    Example 2:

    Input: num = -7
    Output: "-10"

Solution:
    Similar to how you convert from base 10 to base 2. Using modula 7 to find which digit go with the current bit and divide by 7 to move on to the next bit.

Complexity:
    Time: O(n) where n is the number time we need to divide num by 7 to reach 0
    Space: O(n) where n is the number time we need to divide num by 7 to reach 0
"""


class Solution:
    def convertToBase7(self, num: int) -> str:

        # Return "0" if num is 0
        if num == 0:
            return "0"

        # Keep track num is negative
        neg = num < 0

        # Change num to positive
        num = abs(num)

        # Initialize result to store bits
        res = []

        # While num bigger than 0
        while num > 0:

            # Find the bit and append it to the result
            res.append(str(num % 7))

            # Divide by 7 to move on to the next bit
            num = num // 7

        # Add negative sign if the original num is negative
        if neg:
            res.append("-")

        # Form the solution
        res.reverse()
        res = "".join(res)

        return res

