"""
Problem:
    Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

    Example 1:
    Input: matrix =
    [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
    Output: 15
    Explanation: 
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.
    
    Example 2:
    Input: matrix = 
    [
        [1,0,1],
        [1,1,0],
        [1,1,0]
    ]
    Output: 7
    Explanation: 
    There are 6 squares of side 1.  
    There is 1 square of side 2. 
    Total number of squares = 6 + 1 = 7.

Solution:
    Instead of iterating through matrix and count the number of square submatrices of size 1 to n, we will use each entry as an anchor. Each entry will store the largest possible square submatrix that can be form starting from such entry as the top-left corner. Since we know that if an entry can form a submatrix of size n, it should be able to form a submatrix of size n-1, n-2,...1. Thus, we can count the number of possible submatrices by summing all entries. 

    To determine the largest possible square submatrix that can be form for a given entry at (i,j), we will take the minimum among entries at (i+1, j), (i, j+1), and (i+1, j+1) and adding 1 (this account for a 1x1 submatrix).

    ie given matrix = 
    [
        [1, 1, 1], 
        [1, 1, 1], 
        [1, 1, 0]
    ]
    largest submatriccies = 
    [
        [2, 2, 1], 
        [2, 1, 1], 
        [1, 1, 0]
    ]  

    dp(0, 0) = min(dp(0, 1), dp(1, 0), dp(1, 1)) + 1 = min(2, 2, 1) + 1 = 2 

Complexity:
    Time: O(mn)
    Space: O(mn)
"""

from functools import lru_cache
from itertools import product

# Top-down dp
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        
        # Get lengths of rows and cols
        m, n = len(matrix), len(matrix[0])

        # Recursively calculate the largest submatrix starting at i and j
        @lru_cache(None)
        def dp(i, j):

            # If the current entry is 0 or we reach the last row or col, return matrix[i][j]
            if matrix[i][j] == 0 or i == m - 1 or j == n - 1:
                return matrix[i][j]

            # Else, take the minimum among the largest possible submatrix of surrounding entries and adding 1 to find the largest possible submatrix starting at the current entry
            return min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1)) + 1

        # Sum up the largest submatrix for all entries
        return sum(dp(i, j) for i, j in product(range(m), range(n)))

# Bottom-up dp
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:

        # Get lengths of rows and cols
        m, n = len(matrix), len(matrix[0])

        # Reuse matrix as the dp cache
        # Calculate the largest possible submatrix for each entry starting from the bottom-right to top-left
        # Skip the last row and col
        for i, j in product(range(m - 2, -1, -1), range(n - 2, -1, -1)):
            
            # If the current entry contains 0, skip it
            if matrix[i][j] == 0:
                continue

            # Else, take the minimum among the largest possible submatrix of surrounding entries and adding 1 to find the largest possible submatrix starting at the current entry
            matrix[i][j] = (
                min(matrix[i + 1][j], matrix[i][j + 1], matrix[i + 1][j + 1]) + 1
            )

        # Sum up the largest submatrix for all entries
        return sum(sum(row) for row in matrix)
