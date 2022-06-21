""" 
Problem:
    You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

    Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
    
    Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    
    Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Solution:
    Use BFS to solve this problem. Iterate through the grid and keep track of the number of fresh orange and add all rotten orange to the queue. Mark all rotten orange as visited by change it to empty. Then, perform BFS and keep track of the time. For each node in queue, pop them and check if its neighboring node is a fresh orange. If yes, mark it as visited and decrement the number of fresh orange. Once we done with a level, increment the time if the queue is not empty. If the number of fresh orange reaches 0 when we complete the BFS, return the time. Else, return -1.   

Complexity:
    Time: O(m * n)
    Space: O(1)
"""
from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Use deque so you can pop from the front a queue in O(1)
        queue = deque()

        # Get the dimension of the grid
        m, n = len(grid), len(grid[0])

        # Initialize a varaible to keep track of the number of fresh orange.
        fresh = 0

        # Iterate through the grid, count the number of fresh orange and add the rotten orange to the queue.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1

                if grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append((i, j))

        # Initialize a time to keep track of the level of BFS and a helper to help with directional movement.
        time = 0
        helper = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Perform the BFS
        # While the queue is not empty
        while queue:

            # Count how many node at this level
            count = len(queue)

            # Itearte through all node at this level
            for _ in range(count):

                # Pop a node.
                i, j = queue.popleft()

                for di, dj in helper:
                    new_i, new_j = i + di, j + dj

                    # Check if we can visit its neighbor.
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:

                        # If yes, add its neighbor to the queue and mark it as visited.
                        queue.append((new_i, new_j))
                        grid[new_i][new_j] = 0

                        # Decrement the number of fresh orange.
                        fresh -= 1

            # Only increase the time if the queue isn't empty.
            if queue:
                time += 1

        # Return the time if the number of fresh orange is 0. Else, return -1,
        return time if fresh == 0 else -1

