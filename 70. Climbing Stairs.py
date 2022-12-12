""" 
Problem:
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    
    Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Solution:
    Use dp to solve this problem. Let dp be the function that return the number of unique lead to nth step. Thus, we can define dp as 
        dp(n) = dp(n-1) + dp(n-2) where dp(0) == dp(1) == 1

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        # Initialize the cache
        dp = [1, 1] + [0] * (n - 1)

        # Calculate the number of unique way to climb to nth step
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the result
        return dp[n]
