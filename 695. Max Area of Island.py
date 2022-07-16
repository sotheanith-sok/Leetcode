"""
Problem:
    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

    The area of an island is the number of cells with a value 1 in the island.

    Return the maximum area of an island in grid. If there is no island, return 0.

    Example 1:
    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
    
    Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

Solution:
    Iterate through the grid and use a node that is 1 and has not been visited as a starting node. Then, dfs through all neighboring nodes to calculate the area. Return the maximum area. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        # Get length of rows and cols
        m, n = len(grid), len(grid[0])

        # A set to keep track of visited nodes
        visited = set()

        # A helper to access neighbors
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # A result to store the largest area
        res = 0

        # Iterate through the grid
        for i in range(m):
            for j in range(n):

                # If there is a node that is 1 and hasn't been visited yet
                if grid[i][j] == 1 and (i, j) not in visited:

                    # Intialize the area
                    area = 0

                    # Add the starting node to the stack
                    stack = [(i, j)]

                    # Mark the starting node as visited
                    visited.add((i, j))

                    # While the stack isn't empty
                    while stack:

                        # Pop a node
                        row, col = stack.pop()

                        # Increment the area
                        area += 1

                        # Add all unvisted neighbors that are 1 to the stack
                        for dRow, dCol in directions:
                            neiRow, neiCol = row + dRow, col + dCol
                            if (
                                0 <= neiRow < m
                                and 0 <= neiCol < n
                                and grid[neiRow][neiCol] == 1
                                and (neiRow, neiCol) not in visited
                            ):
                                stack.append((neiRow, neiCol))
                                visited.add((neiRow, neiCol))

                    # Save the largest area
                    res = max(res, area)

        return res
