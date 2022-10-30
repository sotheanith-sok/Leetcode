""" 
Problem:
    You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

    Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

    Example 1:
    Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
    Output: 6
    Explanation: 
    The shortest path without eliminating any obstacle is 10.
    The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
    
    Example 2:
    Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
    Output: -1
    Explanation: We need to eliminate at least two obstacles to find such a walk.
    
Solution:
    Use bfs to solve this problem since we want the shortest path. For every cell, we can visit it 1 to k times and thus, our visited set would store (row, col, k). 

    You will see a large improvement if we prune the input a bit. Without any obstacle, the shortest path is m+n-2 where m,n are length of rows and cols respectively. Thus, if we have enough k to convert entire shorest path, we can just return it.  

Complexity:
    Time: O(mnk)
    Space: O(mnk)
"""

from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:

        # Get length of rows and cols
        m, n = len(grid), len(grid[0])

        # Check if we have enough skip to cover the shortest path
        # If yes, return the shortest path
        if k >= m + n - 2:
            return m + n - 2

        # Else, start BFS algorithm
        # A helper function for 4 directional movement
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Initialize the queue and the set
        queue, visited = deque([(0, 0, k)]), set([(0, 0, k)])

        # Initialize the current step count
        step = 0

        # While queue isn't empty
        while queue:

            # Find the number of node at this step
            i = len(queue)

            # Process all nodes
            for _ in range(i):

                # Pop a node
                row, col, k = queue.popleft()

                # Check if we reach the end
                if row == m - 1 and col == n - 1:
                    return step

                # Find the neighboring nodes
                for dRow, dCol in directions:
                    nRow, nCol = row + dRow, col + dCol

                    # If the neighboring node is valid and we haven't visit it using a certain amount of skip before
                    if (
                        0 <= nRow < m
                        and 0 <= nCol < n
                        and (nRow, nCol, k - int(grid[nRow][nCol] == 1)) not in visited
                        and (grid[nRow][nCol] != 1 or k > 0)
                    ):
                        # Mark such node as visited and add it to the queue
                        visited.add((nRow, nCol, k - int(grid[nRow][nCol] == 1)))
                        queue.append((nRow, nCol, k - int(grid[nRow][nCol] == 1)))
            
            # Increment the step count
            step += 1

        # Return -1 if we can't find a valid path
        return -1
