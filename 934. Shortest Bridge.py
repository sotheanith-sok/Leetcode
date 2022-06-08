""" 
Problem:
    You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

    An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

    You may change 0's to 1's to connect the two islands to form one island.

    Return the smallest number of 0's you must flip to connect the two islands.

    Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: 1
    
    Example 2:
    Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
    Output: 2
    
    Example 3:
    Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    Output: 1

Solution:
    Iterate through the grid until you find a node that contains 1. Then, start from that node, use dfs or bfs to find other nodes that contain 1. Finally, use found nodes as the first level and perform bfs. For every level of neighboring node we go down to, we increase the cost by one. Return the (cost - 1) when we found a neighboring node that contains 1. 

Complexity:
    Time: O(n**2)
    Space: O(n**2)

"""

import itertools

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # Get the length of rows and cols
        n = len(grid)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # Find the starting node 
        row, col = 0, 0
        for row, col in list(itertools.product(range(n), range(n))):
            if grid[row][col] == 1:
                break

        # Grab all nodes that contain 1 from the starting node using DFS and add them to a queue.
        queue = []
        stack, visited = [[row, col]], set([(row,col)])

        while stack:

            # Pop a node from the stack.
            row, col = stack.pop()
            queue.append([row, col])

            # Add all its neighboring nodes that contain 1 to the stack.
            for di, dj in directions:
                new_i, new_j = row + di, col + dj

                if (
                    0 <= new_i < n
                    and 0 <= new_j < n
                    and (new_i, new_j) not in visited
                    and grid[new_i][new_j] == 1
                ):
                    stack.append([new_i, new_j])
                    visited.add((new_i, new_j))

        # Perform BFS with increasing cost per level.
        # We will continues to use visited set from the above DFS because it already contains all nodes belong to an island. 
        cost = 0

        while queue:

            # Get the size of the current level
            size = len(queue)

            # Iterate through all nodes at the current level.
            for _ in range(size):

                # Remove a node from the queue
                row, col = queue.pop(0)

                # If we pass the first level and current node contains, return cost - 1
                if cost > 0 and grid[row][col] == 1:
                    return cost -1


                # Add all neighboring unvisited nodes to the queue.
                for di, dj in directions:
                    new_i, new_j = row + di, col + dj

                    if (
                        0 <= new_i < n
                        and 0 <= new_j < n
                        and (new_i, new_j) not in visited
                    ):
                        queue.append([new_i, new_j])
                        visited.add((new_i, new_j))


            # Increment the cost once we processed all nodes in a level. 
            cost += 1

