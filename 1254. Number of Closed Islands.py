"""
Problem:
    Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.

    Example 1:
    Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    Output: 2
    Explanation: 
    Islands in gray are closed because they are completely surrounded by water (group of 1s).
    
    Example 2:
    Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    Output: 1
    
    Example 3:
    Input: grid = [[1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1],
                [1,0,1,1,1,0,1],
                [1,0,1,0,1,0,1],
                [1,0,1,1,1,0,1],
                [1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1]]
    Output: 2

Solution:
    Iterate through all entries. If the current entry is an unvisited land, mark it as visited and explore all neighboring lands. An island is considered to be open if we are able to reach a land on the edge of the grid. Return the number of closed islands. 

Complexity:
    Time: O(mn)
    Space: O(mn)
"""


from itertools import product


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        # Find the number of rows and cols
        m, n = len(grid), len(grid[0])

        # A helper function for 4-directional movement
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Initialize a set to keep track of visited set
        visited = set()

        # DFS through the grid to find all connected lands and check if such island is opened
        def isOpen(row, col):

            # Check if the current entry is located on the edge of the grid
            opened = row == 0 or row == m - 1 or col == 0 or col == n - 1

            # Check all 4 neighboring entires
            for dRow, dCol in directions:
                nRow, nCol = row + dRow, col + dCol

                # If a neighboring entry is an unvisited land, skip it
                if (
                    not (0 <= nRow < m)
                    or not (0 <= nCol < n)
                    or (nRow, nCol) in visited
                    or grid[nRow][nCol] == 1
                ):
                    continue

                # Else, visit it
                visited.add((nRow, nCol))
                opened = isOpen(nRow, nCol) or opened

            return opened

        # Initialize the result
        res = 0

        # Iterate through all entires
        for row, col in product(range(m), range(n)):

            # If the current entry is already visited or it is a water, skip it
            if (row, col) in visited or grid[row][col] == 1:
                continue

            # Else, mark the current entry as visited
            visited.add((row, col))

            # Start finding all lands
            res += int(not isOpen(row, col))

        return res
