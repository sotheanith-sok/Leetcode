""" 
Problem:
    You are given an m x n integer array grid where grid[i][j] could be:

    1 representing the starting square. There is exactly one starting square.
    2 representing the ending square. There is exactly one ending square.
    0 representing empty squares we can walk over.
    -1 representing obstacles that we cannot walk over.
    Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

    Example 1:
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
    
    Example 2:
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    Output: 4
    Explanation: We have the following four paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
    
    Example 3:
    Input: grid = [[0,1],[2,0]]
    Output: 0
    Explanation: There is no path that walks over every empty square exactly once.
    Note that the starting and ending square can be anywhere in the grid.

Solution:
    We will solve this problem using two steps. For the first step, we will iterate through all nodes in the grid and find the starting, ending, and the number of walkable nodes. Then, we will traverse the grid to find paths from the starting node to the ending node and keep count of such paths. 

    We can only visit a next node if..
        1. It is valid
        2. It hasn't been visited yet
        3. It isn't a wall
        4. It is an end cell and we have visited all walkable cells already. 

Complexity:
    Time: O(4**mn)
    Space: O(mn)
"""

from itertools import product


class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:

        # Find the number of rows and cols
        m, n = len(grid), len(grid[0])

        # Intialize the starting and ending nodes and the number of walkable nodes
        start, end, maxSteps = None, None, 0

        # Iterate through all nodes and find above information
        for row, col in product(range(m), range(n)):
            if grid[row][col] == 1:
                start = (row, col)

            if grid[row][col] == 2:
                end = (row, col)

            if grid[row][col] == 0:
                maxSteps += 1

        # Start DFS to count valid paths from starting to ending nodes
        # A helper for 4-directional movements
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Intialize the result and a set to keep track of visited nodes
        res, visited = 0, set([start])

        # DFS through the grid to find the ending node
        def dfs(row, col, steps):
            nonlocal res

            # If we have reach the ending node, update the result
            if (row, col) == end:
                res += 1
                return

            # Else, check next nodes
            for dRow, dCol in directions:
                nRow, nCol = row + dRow, col + dCol

                # We can visit next node if 
                # 1. It is valid
                # 2. It hasn't been visited yet
                # 3. It isn't a wall
                # 4. It is an end cell and we have visited all walkable cells already.

                if (
                    0 <= nRow < m
                    and 0 <= nCol < n
                    and (nRow, nCol) not in visited
                    and grid[nRow][nCol] != -1
                    and ((nRow, nCol) != end or steps == maxSteps)
                ):
                    # Mark the next node as visited
                    visited.add((nRow, nCol))

                    # Visit the next node
                    dfs(nRow, nCol, steps + 1)

                    # Unmark the next node as visited
                    visited.remove((nRow, nCol))

        # DFS through the grind starting from the starting node
        dfs(start[0], start[1], 0)

        # Return the number of valid paths
        return res

