"""
Problem:
    You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

    A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

    Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

    Example 1:
    Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    Output: 3
    Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
    
    Example 2:
    Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    Output: 0
    Explanation: All 1s are either on the boundary or can reach the boundary.

Solution:
    Find coordinate of all lands. Iterate through all lands at the boundary and start removing all lands connected to such lands from the list of lands. Return the number remaning lands

Complexity:
    Time: O(mn)
    Space: O(mn)
"""


from itertools import chain, product


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:

        # Find the length of rows and cols
        m, n = len(grid), len(grid[0])

        # A helper function for 4-directional movements
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Find coordinate of all lands
        lands = set(
            (row, col)
            for row, col in product(range(m), range(n))
            if grid[row][col] == 1
        )

        # DFS through the grid and remove all connected lands
        def dfs(row, col):

            # Remove the current land from the list
            lands.discard((row, col))

            # Check neighboring lands and remove those lands too
            for dRow, dCol in directions:
                nRow, nCol = row + dRow, col + dCol

                if (
                    not (0 <= nRow < m)
                    or not (0 <= nCol < n)
                    or (nRow, nCol) not in lands
                ):
                    continue

                dfs(nRow, nCol)

        # Iterate through all boundary lands and remove all connected lands to such lands
        for row, col in chain(
            product([0, m - 1], range(n)), product(range(m), [0, n - 1])
        ):

            if grid[row][col] == 0:
                continue
            dfs(row, col)

        return len(lands)
