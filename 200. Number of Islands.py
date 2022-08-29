"""
Problem:
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

    Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3

Solution:
    Solve this problem using iterative dfs.  Iterate through all locations in the map. If a location is a water or if it is a visited land, continue to the next location. Else, start from such location and use dfs to marks neighboring lands as visited. Lastly, increment the result by 1. 

Complexity:
    Time: O(mn) where m and n are the length of rows and cols respectively.
    Space: O(mn)
"""


from itertools import product


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        # Get the length of rows and cols
        m, n = len(grid), len(grid[0])

        # A set used to keep track of visited lands
        visited = set()

        # The result to keep track of the number of discovered islands
        res = 0

        # A helper function for 4-directional movement
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Iterate through all locations
        for i, j in product(range(m), range(n)):

            # If the current location is a water or if it is a visited land
            if grid[i][j] == "0" or (i, j) in visited:

                # Continue to the next location
                continue

            # Else, perform dfs to marks all neighboring lands as visited

            # Initialize the stack
            stack = [(i, j)]

            # While the stack isn't empty
            while stack:

                # Pop a location from the stack
                row, col = stack.pop()

                # Calculate neighboring locations
                for dRow, dCol in directions:
                    neiRow, neiCol = row + dRow, col + dCol

                    # If the neighboring location is a land and we haven't visited it yet
                    if (
                        0 <= neiRow < m
                        and 0 <= neiCol < n
                        and grid[neiRow][neiCol] == "1"
                        and (neiRow, neiCol) not in visited
                    ):
                        # Add such location to the stack
                        stack.append((neiRow, neiCol))

                        # Mark such location as visited
                        visited.add((neiRow, neiCol))

            # Increment the result by 1
            res += 1

        return res
