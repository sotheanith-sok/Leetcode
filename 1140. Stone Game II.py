"""
Problem:
    Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

    Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

    On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

    The game continues until all the stones have been taken.

    Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
    Example 1:
    Input: piles = [2,7,9,4,4]
    Output: 10
    Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
    
    Example 2:
    Input: piles = [1,2,3,4,5,100]
    Output: 104

Solution:
    Start by calculating the surfix sum aka piles[i] is the sum of all piles starting from i to the end. Then, use dynamic programming to solve this problem. For some arbitrary i and m, the maximized amount of stone at i is piles[i] - the minimum among maximized amount of stone at i+x and max(x, m) where 1 <= x <= 2m aka the worst among all possible best next moves.
    
    Ex: 
    piles[i] - maximized amount of stone at i+1 == we pick i pile only
    piles[i] - maximized amount of stone at i+2 == we pick i and i+1 piles
    piles[i] - maximized amount of stone at i+3 == we pick i, i+1, i+2 piles

    ie Given piles = [8,6,9,1,7,9]

        SurfixSum   Index   m =  0  1   2   3   4   5   6  
        40          0           [0, 25, 24, 40, 40, 40, 40  ], 
        32          1           [0, 15, 23, 32, 32, 32, 32  ], 
        26          2           [0, 18, 26, 26, 26, 26, 26  ], 
        17          3           [0, 8,  17, 17, 17, 17, 17  ], 
        16          4           [0, 16, 16, 16, 16, 16, 16  ], 
        9           5           [0, 9,  9,  9,  9,  9,  9   ]
    
    Let dp(i,m) be the maximized amount of stone starting at index i and given m moves. Then, 
        dp(0, 2) = piles[0] - min(dp(1, 2), dp(2,2), dp(3,3), dp(4,4)) = 40 - min(23, 26, 17, 16) = 24
    

Complexity:
    Time: O(n**2)
    Space: O(n**2)
"""

# Top-down dp
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:

        # Get the number of piles
        n = len(piles)

        # Convert piles to surfix sum
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]

        # Top-down dp to find the maximized amount of stone for a given starting ith pile and m move
        @lru_cache(None)
        def dp(i, m):

            # If we have enough moves to take all remaining piles, return the sum of stone starting from ith pile
            if i + (2 * m) >= n:
                return piles[i]

            # Check for the least amount of stones among next moves. This will maximize the current move
            return piles[i] - min(dp(i + x, max(x, m)) for x in range(1, 2 * m + 1))

        return dp(0, 1)

# Bottom-up dp
from itertools import product


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:

        # Get the number of piles
        n = len(piles)

        # Convert piles to surfix sum
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]

        # Generate cache containing base cases
        # If we have 0 move, then we can't pick any pile. Else, assume we can all remaining piles
        dp = [[0] + ([piles[i]] * n) for i in range(n)]

        # Iterate through all possible i and m
        for i, m in product(range(n - 1, -1, -1), range(n, 0, -1)):

            # Skip any i and m where we have enough moves to pick all remaining stones
            if i + 2 * m >= n:
                continue

            # Update the rest of entires
            dp[i][m] = dp[i][m] - min(dp[i + x][max(x, m)] for x in range(1, 2 * m + 1))

        return dp[0][1]
