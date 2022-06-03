""" 
Problem:
    Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

    In one shift operation:

    Element at grid[i][j] moves to grid[i][j + 1].
    Element at grid[i][n - 1] moves to grid[i + 1][0].
    Element at grid[m - 1][n - 1] moves to grid[0][0].
    Return the 2D grid after applying shift operation k times.

    Example 1:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]
    
    Example 2:
    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    
    Example 3:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]

Solution:
    Convert the 2d coordinate of each element in the matrix to a 1d coordinate and shift them by k. Then, convert the 1d coordinate back to 2d coordinate. Finally, transfer value from the old to the new 2d coordinate.  

Complexity:
    Time: O(m * n) where m is the length of row and n is the length of col.
    Space: O(m * n)
"""


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:

        # Find how many rows and cols we are working with
        rows = len(grid)
        cols = len(grid[0])

        # Generate a result matrix containing 0
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        # Iterate through every element
        for row in range(rows):
            for col in range(cols):

                # Convert 2D coordinate to 1D
                index = (row * cols) + col

                # Shift and bound the index to the size of the matrix
                index += k
                index = index % (rows * cols)

                # Convert from 1D to 2D coordinate
                new_col = index % cols
                new_row = index // cols

                # Transfer the value from one coordinate to the new coordinate
                res[new_row][new_col] = grid[row][col]

        return res

