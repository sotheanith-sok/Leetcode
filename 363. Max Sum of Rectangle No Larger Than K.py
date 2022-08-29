"""
Problem:
    Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

    It is guaranteed that there will be a rectangle with a sum no larger than k.

    Example 1:
    Input: matrix = [[1,0,1],[0,-2,3]], k = 2
    Output: 2
    Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

    Example 2:
    Input: matrix = [[2,2,-1]], k = 3
    Output: 3

Solution:
    Use two pointers to generate prefix sums of each rows. Left pointer will go from 0 to n and right pointer will go from left to n. By calculating prefix sums for each row, we reduce all rectangle from 2d to 1d where each rectangle is represented by 1d array of rows prefix sum.

    For each row prefix sum, we will calculate column prefix sum and use binary search to find maximum area lesser than k. Start by initialize a list to store previously calculated column prefix sum. Iterate through all values in the row prefix sum. At each iteration, calculate the column prefix sum and check if there exists a previous column prefix sum that is larger than the different between the current column sum and k but the smallest among all previous prefix sums that are greater than the different. Use binary search to find such values. If there is, update the result.

    Ex: Given matrix = [[1,0,1],[0,-2,3]], k = 2
    l   r   rowSums     colSums     area        res        
    0   0   [1, 0]      [1, 1]      [1,  1]     1
    0   1   [1, -2]     [1, -1]     [1, -1]     1
    0   2   [2, 1]      [2, 3]      [2, None]   2
    1   1   [0, -2]     [0, -2]     [0, -2]     2
    1   2   [1, 1]      [1, 2]      [1, 2]      2
    2   2   [1, 3]      [1, 4]      [1, None]   2


    P.S. Kadane Algorithm: Given a list of numbers. You can calculate the maximum area ended at each number by taking the maximum between the current number vs the maximum area of previous number plus the current number. 
        area(i) = max(area(i-1) + nums[i], nums[i])


Complexity:
    Time: O(m**2 n**2)
    Space:  O(m)
"""


from bisect import bisect_right, insort
from math import inf


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:

        # Get the length of rows and colums
        m, n = len(matrix), len(matrix[0])

        # Initialize the result
        res = -inf

        # Iterate the left pointer from 0 to n
        for l in range(n):

            # Initialize the row prefix sum
            rowSums = [0] * m

            # Iterate the right pointer from left to n
            for r in range(l, n):

                # Calculate the row prefix sum from left to right
                for i in range(m):
                    rowSums[i] += matrix[i][r]

                # Calculate the column prefix sums
                # Initialize a list to store previous column prefix sum
                colSums = [0]

                # Intialize the column prefix sum
                colSum = 0

                # Iterate through all row prefix sums
                for rowSum in rowSums:

                    # Add the current row prefix sum to the column prefix sum
                    colSum += rowSum

                    # Calculate the different between the column prefix sum and k
                    diff = colSum - k

                    # Perform a binary search to find an index of a value is larger but cloest to the different among previously calculated column prefix sums
                    idx = bisect_right(colSums, diff)

                    # Check if the different exists among the previously calculated column prefix sums
                    if idx - 1 >= 0 and colSums[idx - 1] == diff:

                        # If yes, update the result
                        res = max(res, colSum - colSums[idx - 1])

                        # End the search because we found the largest possible result
                        return k

                    # Else, if the different does not exist among the previously calculated column prefix sums, check if there is a previously calculated column prefix sum larger than the different
                    elif idx != len(colSums):

                        # If yes, update the result with the new area if it is larger than previous result
                        res = max(res, colSum - colSums[idx])

                    # Insert the current column prefix sum into the list while maintaining the sorted order
                    insort(colSums, colSum)

        return res

