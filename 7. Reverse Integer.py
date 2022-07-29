"""
Problem:
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Example 1:
    Input: x = 123
    Output: 321
    
    Example 2:
    Input: x = -123
    Output: -321
    
    Example 3:
    Input: x = 120
    Output: 21

Solution:
    Convert integer to string and reverse it. Then, check for edge cases
    1. If length of reversed int is larger than intMax/intMin, return 0
    2. If length of reversed int is smaller than intMax/intMin, convert and return reversed int
    3. If length of reversed int is equal to intMax/intMin,
        3.1 If the leading digit of reversed int is larger than intMax/intMin, return 0
        3.2 If the leading digit of reversed int is smaller than intMax/intMine, convert and return reversed int
        3.3 If the leading digit of reversed int is eqaul to intMax/intMine,
            3.3.1 If the remaining digits are less than intMax/intMin, convert and return reversed int
            3.3.2 Else, return 0

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def reverse(self, x: int) -> int:

        # Initialize the min and max value of int32
        intMax, intMin = "2147483647", "2147483648"

        # Keep track if the original x is positive or negative
        pos = True if x >= 0 else False

        # Convert x to string and reversed it
        x = str(abs(x))[::-1]

        # 1. If length of reversed int is larger than intMax/intMin, return 0
        if len(x) > len(intMax):
            return 0

        # 2. If length of reversed int is smaller than intMax/intMin, convert and return reversed int
        if len(x) < len(intMax):
            return (1 if pos else -1) * int(x)

        # 3. If length of reversed int is equal to intMax/intMin,
        # 3.1 If the leading digit of reversed int is larger than intMax/intMin, return 0
        if int(x[0]) > int(intMax[0]):
            return 0

        # 3.2 If the leading digit of reversed int is smaller than intMax/intMine, convert and return reversed int
        if int(x[0]) < int(intMax[0]):
            return (1 if pos else -1) * int(x)

        # 3.3 If the leading digit of reversed int is eqaul to intMax/intMine,
        # 3.3.1 If the remaining digits are less than intMax/intMin, convert and return reversed int
        if (pos and int(x[1:]) <= int(intMax[1:])) or (
            not pos and int(x[1:]) <= int(intMin[1:])
        ):
            return (1 if pos else -1) * int(x)

        # 3.3.2 Else, return 0
        return 0

