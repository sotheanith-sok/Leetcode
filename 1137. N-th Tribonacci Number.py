"""
Problem:
    The Tribonacci sequence Tn is defined as follows: 

    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

    Given n, return the value of Tn.

    Example 1:
    Input: n = 4
    Output: 4
    Explanation:
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4
    
    Example 2:
    Input: n = 25
    Output: 1389537

Solution:
    Solve this problem using bottom-up dp. Maintain three variables to store the 3 previously calculated tribonacci and continue to calculate all tribonacci up to n. Return the nth tribonacci.

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def tribonacci(self, n: int) -> int:

        # Base cases for 0th, 1st, and 2nd tribonacci
        if n < 3:
            return 0 if n == 0 else 1

        # Initialize the first 3 calculated tribonacci
        a, b, c = 0, 1, 1

        # Calculate tribonacci from 3rd to nth
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        # Return the nth tribonacci
        return c
