"""
Problem:
    Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

    Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

    You may return the answer in any order.

    Example 1:
    Input: n = 3, k = 7
    Output: [181,292,707,818,929]
    Explanation: Note that 070 is not a valid number, because it has leading zeroes.
    
    Example 2:
    Input: n = 2, k = 1
    Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Solution:
    Use backtracking technique to solve this problem. If num is 0, the next digit can be any numbers between 1 and 9. Else, the next digit will be last digit +/- k. Continue to pick next digits until num has n digits.

Complexity: 
    Time: 2**n
    Space: 2**n
"""


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        res = []

        def backtrack(num):

            # If num has n digits, append num to the result
            if num // 10 ** (n - 1) != 0:
                res.append(num)
                return

            # Find next possible digits
            nextDigits = range(1, 10) if num == 0 else set([num % 10 - k, num % 10 + k])

            # Recursively add a digit to num
            for digit in nextDigits:
                if 0 <= digit <= 9:
                    backtrack(num * 10 + digit)

        # Start backtracking
        backtrack(0)

        return res

