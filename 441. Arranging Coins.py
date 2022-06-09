"""
Problem:
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Solution:
    The stair is arranged as 1,2,3,4,... where each step is one more than the previous step. Thus, we can calculate the number of coin used for any given steps using the finite sum of natural numbers. I.E [n(n+1)]/2 = k where n is the step and k is the total of coin used. Consequently, we can derive the the number of step for any given arbitrary number of coins (k) by solving for the step (n) using quadratic formula. 

Complexity:
    Time: O(1)
    Space: O(1)
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:

        # [-b +- sqrt(b**2 - 4ac)]/2
        return max(
            int(((-1 + (1 + 8 * n) ** (0.5)) / 2).real),
            int(((-1 - (1 + 8 * n) ** (0.5)) / 2).real),
        )

