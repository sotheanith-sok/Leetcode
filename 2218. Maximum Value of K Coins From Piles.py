"""
Problem:
    There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

    In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

    Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.
    
    Example 1:
    Input: piles = [[1,100,3],[7,8,9]], k = 2
    Output: 101
    Explanation:
    The above diagram shows the different ways we can choose k coins.
    The maximum total we can obtain is 101.
    
    Example 2:
    Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
    Output: 706
    Explanation:
    The maximum total can be obtained if we choose all coins from the last pile.

Solution:
    Solve this problem using top-down dynamic programming. Let dp be the function that return the maximum value of coins given we start picking from some arbitrary i-th pile and have k remaining choice. We can define dp as

    dp(i, k) = max(
                    0 + dp(i+1, k)                      => This is the case where we don't pick any coin from i-th pile
                    sum(piles[i][0:1]) + dp(i+1, k-1)   => Pick 1st coin from the i-th pile
                    sum(piles[i][0:2]) + dp(i+1, k-2)   => Pick 1st and 2nd coins from the i-th piles
                    ...            
    ) 

Complexity:
    Time: O(nk**2) because we can pick at most k elmements from each pile
    Space: O(nk)
"""


from functools import lru_cache


class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:

        # Find the number of piles
        n = len(piles)

        # Top-down dp to find the maximum value of coins if we start picking from ith piles and have k remaining choice
        @lru_cache(None)
        def dp(i, k):

            # If we reach the end of piles or have 0 remaining choice, we have reach the end
            if i == n or k == 0:
                return 0

            # Find maximum value of coins if we don't pick any coins from the current pile
            res = dp(i + 1, k)

            # Initialize the sum of all coins picked
            total = 0

            # Start picking one coin at a time
            for j in range(min(len(piles[i]), k)):

                # Pick a 0th to jth coins
                total += piles[i][j]

                # Check if by picking the current sequence of coins will lead to the largest maximum value of coins
                res = max(res, total + dp(i + 1, k - j - 1))

            return res

        return dp(0, k)
