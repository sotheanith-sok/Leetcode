"""
Problem:
    Given a matrix and a target, return the number of non-empty submatrices that sum to target.

    A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

    Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

    Example 1:
    Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
    Output: 4
    Explanation: The four 1x1 submatrices that only contain 0.

    Example 2:
    Input: matrix = [[1,-1],[-1,1]], target = 0
    Output: 5
    Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
    
    Example 3:
    Input: matrix = [[904]], target = 0
    Output: 0

Solution:
    Use prefix sum technique to iterate through sum of all possible matrix. Start by performing prefix sum on all rows. Then, we will pick two coloumns: c1 and c2. c1 will be between 0 and the number of columns and c2 will be between range of c1 and the number of columns. This will let us iterate through all columns using the following prefix sum formula sum(c2) - (sum(c1) if c1 > 0 else 0). 
    Ex: given columns: 1, 2, 3 
        let c1 == 1 and     c2 == 1 -> [1]
                            c2 == 2 -> [1,2]
                            c3 == 3 -> [1,2,3]
        let c2 == 2 and     c2 == 2 -> [2]
                            c2 == 3 -> [2,3]
        let c3 == 3 and     c3 == 3 -> [3]

    Then, for each column pairs, we will iterate through all rows to get all combinations the sum of all submatrix. Next, at each matrix we will calculate the difference between total and target (Order is important here as total will be larger than the target). If the difference exists previously, we add its count to the result and save the current total into the cache.

Complexity:
    Time: O(mnn)
    Space: O(m)
"""


from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:

        # Get the length of rows and columns
        m, n = len(matrix), len(matrix[0])

        # Perform prefix sum on all rows
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j] + matrix[i][j - 1]

        # Initialzie the result
        res = 0

        # Iterate through all possible columns
        for j1 in range(n):
            for j2 in range(j1, n):
                
                # For each column pairs, find how many submatrix sum up the target
                # Initialize the cache
                cache = defaultdict(int)

                # Initialize the total and the base case 0:1
                total, cache[0] = 0, 1

                # Iterate through all rows
                for i in range(m):

                    # Calculate the total up to the current row
                    total += matrix[i][j2] - (matrix[i][j1 - 1] if j1 > 0 else 0)
                    
                    # Similar to Leetcode 1
                    # If the difference between the current total and target exists previously, add its count to the result
                    res += cache[total - target]
                    
                    # Save the total to the cache
                    cache[total] += 1

        return res

