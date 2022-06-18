""" 
Problem:
    Given an m x n integers matrix, return the length of the longest increasing path in matrix.

    From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

    Example 1:
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].
    
    Example 2:
    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
    
    Example 3:
    Input: matrix = [[1]]
    Output: 1

Solution:
    Use recursive DFS to solve this problem(Iterative DFS is hard to implement since you want to process all neighboring nodes before the current nodes). During DFS call, we will take the max paths from all of its neighboring nodes and add one to 1. If a node, doesn't have a neighbor, we will assume that its max path is 1.  

Complexity:
    Time: O(m*n)
    Space: O(m*n)
"""


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:

        # Get the length of rows and cols.
        n, m = len(matrix), len(matrix[0])

        # A helper function for directional movements.
        helper = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # A cache to store all intermediate results. Assume unvisited node as 0.
        cache = [[0 for _ in range(m)] for _ in range(n)]

        # A dfs to explore a node and all of its neighbors.
        def dfs(i, j):

            # If we visited this node before, return the cached max path.
            if cache[i][j] > 0:
                return cache[i][j]

            # Assume a node has a max path of 1 if it doesn't have a neighbor.
            possible_max_paths = [1]

            # Explore the node neighbors
            for di, dj in helper:

                # Calculate the neighboring i and j
                new_i, new_j = i + di, j + dj

                # If a neighbor has larger value than the current node, call a dfs function on it.
                if (
                    0 <= new_i < n
                    and 0 <= new_j < m
                    and matrix[new_i][new_j] > matrix[i][j]
                ):
                    possible_max_paths.append(1 + dfs(new_i, new_j))

            # Save the maximum path into the cache.
            cache[i][j] = max(possible_max_paths)

            return cache[i][j]

        # Store the maximum path.
        max_path = 0

        # Check the max path of all nodes.
        for i in range(n):
            for j in range(m):
                max_path = max(max_path, dfs(i, j))

        return max_path
