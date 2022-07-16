"""
Problem:
    There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

    Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

    Example 1:
    Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
    Output: 6
    
    Example 2:
    Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
    Output: 12

Solution:
    The idea is that a number of move at step i into a node is the accumulation of its neighboring nodes moves at step i-1. Thus, we will use a 2d arrays to keep track of moves at every step. Start by initalize the starting node at step 0 with the value of 1. Then, we can calculate all nodes at step 1 by iterating through every node and adding all of its neighboring node move from the previous time. If a node is at a border, its next move will contribute to the count of paths that lead out of the boundary. 

Complexity:
    Time: O(m n maxMove)
    Space: O(m n maxMove)
"""


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:

        # If there is 0 move, we return 0
        if maxMove == 0:
            return 0

        # Intialize the path count
        pathCount = [[0 for _ in range(n)] for _ in range(m)]
        pathCount[startRow][startColumn] = 1

        # A helper function for the four directional movement
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        
        # The count of path lead out of the boundary
        res = 0


        # Iterate through every step
        for _ in range(0, maxMove):

            # Intialize the path count for the next step
            nextPathCount = [[0 for _ in range(n)] for _ in range(m)]

            # Iterate through all nodes
            for row in range(m):
                for col in range(n):

                    
                    # If the current node path count is 0, skip it because it won't contribute to its neighboring nodes path count at the next step or the result
                    if pathCount[row][col] == 0:
                        continue

                    # Check all of its neighboring nodes
                    for dRow, dCol in directions:

                        neiRow, neiCol = row + dRow, col + dCol

                        # If its neighboring node is out of bound, add the current node path count to the result
                        if neiRow < 0 or neiRow >= m or neiCol < 0 or neiCol >= n:
                            res += pathCount[row][col]

                        # Else, add the current node path count to its neighboring node path count for the next time step
                        else:
                            nextPathCount[neiRow][neiCol] += pathCount[row][col]

            # Set the next step path counts as the current step path counts
            pathCount = nextPathCount

        return res % 1000000007

