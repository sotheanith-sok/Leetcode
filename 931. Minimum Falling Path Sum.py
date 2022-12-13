"""
Problem: 
    Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

    A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

    Example 1:
    Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    Output: 13
    Explanation: There are two falling paths with a minimum sum as shown.
    
    Example 2:
    Input: matrix = [[-19,57],[-40,-5]]
    Output: -59
    Explanation: The falling path with a minimum sum is shown.

Solution:
    Iterate through all entires in the matrix. For some arbitrary entry, the minimum path sum to reach it is the sum of its cost and the minimum cost to reach one of the three entries above it. Then, we can simply return the least path sum in the last row for the result. 

Complexity:
    Time: O(n**2)
    Space: O(1)
"""


from itertools import product
from math import inf


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        # Find the length of rows and cols
        n = len(matrix)

        # Iterate through all entries
        for row, col in product(range(n), repeat=2):

            # We can skip the first row
            if row == 0:
                continue

            # Calculate the path sum to reach the current entry
            matrix[row][col] = matrix[row][col] + min(
                matrix[row - 1][col - 1] if col - 1 >= 0 else inf,
                matrix[row - 1][col],
                matrix[row - 1][col + 1] if col + 1 < n else inf,
            )

        # Return the least path sum to reach the last row
        return min(matrix[-1])
