"""
Problem:
    Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

    Example 1:
    Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
    Output: 2
    Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
    
    Example 2:
    Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
    Output: 0

Solution:
    Start by generating the prefix sum of the matrix where each entry are the sum of all numbers from origin to such entry. This approach allows us to calculate the sum of any sub-matrix in O(1) time. 

    Initialize the result to 0. Iterate through all entries and check if it can make a submatrix of size res+1 where its sum is less than or equal to the threshold. If yes, increment res by 1. Else, continue to the next entry. 

Complexity:
    Time: O(mn)
    Space: O(mn)
"""


from collections import defaultdict
from itertools import product


class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:

        # Find the number of rows and cols
        m, n = len(mat), len(mat[0])

        # Use defaultdict such that out of bound indices will return 0
        prefix = defaultdict(int)

        # Generate prefix sum for all entires
        for i, j in product(range(m), range(n)):
            prefix[(i, j)] = (
                mat[i][j]
                + prefix[(i - 1, j)]
                + prefix[(i, j - 1)]
                - prefix[(i - 1, j - 1)]
            )

        # Initialize the result
        res = 0

        # Iterate through all entries
        for i, j in product(range(m), range(n)):

            # While the current entry can make a submatrix of size res+1 and such matrix sum is less than or equal to the threshold, increment the result
            while (
                min(i, j) + 1 > res
                and prefix[(i, j)]
                - prefix[(i - res - 1, j)]
                - prefix[(i, j - res - 1)]
                + prefix[(i - res - 1, j - res - 1)]
                <= threshold
            ):
                res += 1

        return res

