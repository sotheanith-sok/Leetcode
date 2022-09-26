"""
Problem:
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

    Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

    Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

Solution:
    Perform a simple multiplication where we take each digit in num2 and multiply them by all digit in num1 and then sum everything up. We can calculate the each digit of the resulting multiplcation using grouping. 

    Ex: num1=[1, 2, 3, 4] num2 = [a, b, c]

    place   digit/carry     groupSize
    0       d4              1
    1       d3 + c4         2
    2       d2 + c3 + b4    3
    3       d1 + c2 + b3    3
    4       c1 + b2         2
    5       b1              1

    First loop will calculate all digits from 1 to maxGroupSize and the second loop will calcualte all digits from maxGroupSize - 1 to 1. 


Complexity:
    Time: O(mn)
    Space: O(m + n)
"""


from collections import deque
from itertools import zip_longest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # If num1 or num2 is 0, return 0
        if num1 == "0" or num2 == "0":
            return "0"

        # A mapper converting string to int
        nums = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        # Find lengths of num1 and num2
        m, n = len(num1), len(num2)

        # Find the maximum group size
        maxSize = min(m, n)

        # Variable to keep track of the carry
        carry = 0

        # Deque used to store the result
        res = deque()

        # First Loop: calcualte all digts from 1 to max group size
        for size, (i, j) in enumerate(
            zip_longest(range(m - 1, -1, -1), range(n - 1, -1, -1), fillvalue=0)
        ):

            # Calculate the current group size capped at max group size
            size = min(size + 1, maxSize)

            # Element wise multiplcation for parts of num1 (start -> end) with parts of num2 (end -> start) and sum the result
            s = (
                sum(
                    nums[num1[a]] * nums[num2[b]]
                    for a, b in zip(range(i, i + size), range(j + size - 1, j - 1, -1))
                )
                + carry
            )

            # Calculate the digit and carry over
            carry, digit = divmod(s, 10)

            # Append the digit into the result
            res.appendleft(str(digit))

        # Second loop: calculate all digits from max group size - 1 to 1
        size = size - 1

        while size > 0:

            # Element wise multiplcation for parts of num1 (start -> end) with parts of num2 (end -> start) and sum the result
            s = (
                sum(
                    nums[num1[a]] * nums[num2[b]]
                    for a, b in zip(range(i, i + size), range(j + size - 1, j - 1, -1))
                )
                + carry
            )

            # Calculate the digit and carry over
            carry, digit = divmod(s, 10)

            # Append the digit into the result
            res.appendleft(str(digit))

            # Decrement the current group size
            size -= 1

        # If there is any carry left, append it to the result
        if carry != 0:
            res.appendleft(str(carry))

        return "".join(res)

