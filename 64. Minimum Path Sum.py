"""
Problem:
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

    Example 1:
    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
    
    Example 2:
    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12

Solution:
    Let dp be the function that the minimum path sum to reach an arbitrary entry in the grid. We can define dp as
        dp[row][col] = cost[row][col] + min(dp[row-1][col], dp[row][col-1]) 
            where out of bound entries have "infinite" minimum path sum  

Complexity:
    Time: O(mn)
    Space: O(1)
"""


from itertools import product
from math import inf


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        # Find the number of rows and cols
        m, n = len(grid), len(grid[0])

        # Iterate through all entries
        for row, col in product(range(m), range(n)):

            # Skip the top left entry
            if row == col == 0:
                continue

            # Calculate the minimum path sum to reach each entry
            grid[row][col] += min(
                grid[row - 1][col] if 0 <= row - 1 < m else inf,
                grid[row][col - 1] if 0 <= col - 1 < n else inf,
            )

        # Return the minimum path sum to reach the bottom right entry
        return grid[-1][-1]
