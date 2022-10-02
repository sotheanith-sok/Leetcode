"""
Problem:
    You have n dice and each die has k faces numbered from 1 to k.

    Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

    Example 1:
    Input: n = 1, k = 6, target = 3
    Output: 1
    Explanation: You throw one die with 6 faces.
    There is only one way to get a sum of 3.
    
    Example 2:
    Input: n = 2, k = 6, target = 7
    Output: 6
    Explanation: You throw two dice, each with 6 faces.
    There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
    
    Example 3:
    Input: n = 30, k = 30, target = 500
    Output: 222616187
    Explanation: The answer must be returned modulo 109 + 7.

Solution:
    Let dp be the function that return the number of way we can roll dices such that their sums are equal to the target. Thus, we can define dp as

    dp(n, target) = dp(n-1, target - i) for i in 1, 2,...,k

    aka we explore all ways we can roll each dice and how it will reduce the target. If we able to roll all dices and target is 0, we have found a valid route. 

Complexity:
    Time: O(nk)
    Space: O(nk)
"""


from functools import lru_cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def dp(n, target):

            # If we rolled all dices or target is less than equal 0, we reach the basecase
            if n == 0 or target <= 0:

                # Return 1 if target reaches 0 and we able to roll all dices
                return int(n == 0 and target == 0)

            # Else, sum all ways we can roll this dice and how it will reduce the target
            return sum(dp(n - 1, target - i - 1) for i in range(k))

        return dp(n, target) % (10 ** 9 + 7)

