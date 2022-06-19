""" 
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

Complexity: 
    Time:
    Space:

"""


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        helper = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        cache = [[1 for j in range(m)] for i in range(n)]

        def explore(i, j):
            if cache[i][j] > 1:
                return cache[i][j]

            steps = [1]

            for di, dj in helper:
                new_i, new_j = i + di, j + dj

                if (
                    0 <= new_i < n
                    and 0 <= new_j < m
                    and matrix[new_i][new_j] > matrix[i][j]
                ):
                    steps.append(1 + explore(new_i, new_j))

            cache[i][j] = max(steps)
            return max(steps)



        for i in range(n):
            for j in range(m):
                if cache[i][j] == 1:
                    explore(i, j)

        return max(max(x) for x in cache)


print(Solution().longestIncreasingPath( [[1]]))

