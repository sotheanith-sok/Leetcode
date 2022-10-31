""" 
Problem:
    Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

    Example 1:
    Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    Output: true
    Explanation:
    In the above grid, the diagonals are:
    "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
    In each diagonal all elements are the same, so the answer is True.
    
    Example 2:
    Input: matrix = [[1,2],[2,2]]
    Output: false
    Explanation:
    The diagonal "[1, 2]" has different elements.

Solution:
    Check all position diagonal for discrepancy. If there is one, return False. Else, return True.

Complexity:
    Time: O(mn)
    Space: O(1)
"""

from itertools import chain, product


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:

        # Get length of rows and cols
        m, n = len(matrix), len(matrix[0])

        # Iterate through all starting row and col of all diagonal
        for row, col in chain(product(range(m), [0]), product([0], range(n))):

            # Get the target value for a diagonal
            target = matrix[row][col]

            # Itereate through all values in a diagonal
            while row < m and col < n:

                # If there is a value that is different than the target, return False
                if matrix[row][col] != target:
                    return False

                # Else, increment both row and col
                row, col = row + 1, col + 1

        # Return True if there is no discrepancy
        return True

