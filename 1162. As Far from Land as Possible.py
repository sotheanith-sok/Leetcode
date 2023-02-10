"""
Problem:
    Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

    The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

    Example 1:
    Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
    Output: 2
    Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
    
    Example 2:
    Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
    Output: 4
    Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Solution:
    Rather than trying to find the furthest water cell from any land, we should find the last water cell to be visited if we were to start from all land cells and taking one step at a time. 

    BFS through the grid starting from land cells and return the number of steps required to visit all water cells.  

Complexity:
    Time: O(n^2)
    Space: O(n)
"""

from collections import deque
from itertools import product


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:

        # Find the number of rows and cols
        n = len(grid)

        # Add all land cells into the queue
        queue = deque(
            (row, col)
            for row, col in product(range(n), repeat=2)
            if grid[row][col] == 1
        )

        # If all cells are land or water, return -1
        if not queue or len(queue) == n * n:
            return -1

        # Initialize a helper function for 4-directional movements and a variable to keep track of the number of steps
        directions, step = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0

        # Iterate until the queue is empty
        while queue:

            # Find the number of cells visitable at this step
            k = len(queue)

            # Visit all cells
            for _ in range(k):

                # Pop a cell
                row, col = queue.popleft()

                # Check if we can visit any neighboring cell from the current cell
                for dRow, dCol in directions:
                    nRow, nCol = row + dRow, col + dCol

                    if (
                        not (0 <= nRow < n)
                        or not (0 <= nCol < n)
                        or grid[nRow][nCol] != 0
                    ):
                        continue

                    # If yes, mark such neighboring cell as visited and add it into the queue
                    grid[nRow][nCol] = 1

                    queue.append((nRow, nCol))

            # Increment the step by 1
            step += 1

        return step - 1
