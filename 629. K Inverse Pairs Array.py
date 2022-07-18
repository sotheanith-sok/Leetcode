"""
Problem:
    For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

    Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

    Example 1:
    Input: n = 3, k = 0
    Output: 1
    Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
    
    Example 2:
    Input: n = 3, k = 1
    Output: 2
    Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Solution:
    For any given n and k, the number of inverse pairs are equal to the number of inverse pairs at n-1 and k-i where i is in range(0,n). Thus, we can use bottom-up dynamic programming to solve this problem. The base case is for any n and k == 1, the number of inverse pairs is always 1. We can optimizie the k-i look back by using the prefix sum. 

    Full explanation: https://leetcode.com/problems/k-inverse-pairs-array/discuss/846076/C%2B%2B-4-solutions-with-picture and https://leetcode.com/problems/k-inverse-pairs-array/solution/ 

Complexity:
    Time: O(nk)
    Space: O(nk)
"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        # Solution is always 1 when k == 0
        if k == 0:
            return 1

        # Intialize the cache
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

        # Add the base case
        dp[1][0] = 1

        # Using prefix sum to fill the remaining values in n==1 row
        for j in range(1, k + 1):
            dp[1][j] = dp[1][j - 1]

        # Fill in the remaining values for n==2...
        for i in range(2, n + 1):
            for j in range(k + 1):

                # If k==0, the solution is 1
                if j == 0:
                    dp[i][j] = 1
                    continue

                # We update each value using prefix sum to avoid n look back.
                dp[i][j] = (
                    dp[i - 1][j]  # value at dp[n-1][k]
                    - (dp[i - 1][j - i] if j - i >= 0 else 0)  # value at dp[n-1][k-n]
                    + dp[i][j - 1]  # value at dp[n][k-1]
                )

        return (dp[n][k] - dp[n][k - 1]) % 1000000007

