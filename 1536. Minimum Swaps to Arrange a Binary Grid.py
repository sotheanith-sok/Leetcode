"""
Problem:
    Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

    A grid is said to be valid if all the cells above the main diagonal are zeros.

    Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

    The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

    Example 1:
    Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
    Output: 3
    
    Example 2:
    Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
    Output: -1
    Explanation: All rows are similar, swaps have no effect on the grid.
    
    Example 3:
    Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
    Output: 0

Solution:
    Start by counting consecutive zeros in each row starting from the end of the column. Store (row, zero count) in an ordered dictionary. We will use this like a stack but we can remove any item in O(1).  

    Next, iterate through all rows and calculate how many zeros is needed in such row. Then, find the first row in the ordered dictionary that contains at least that much zeros. The index of such first row will be the amount of steps we need to swap to move such row to the correct position. Delete used row.  

    ie. Given grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]

    1. Count zeroes
        orderedDict = {0:3, 1:0, 2:3, 3:3}

    2. Calculate steps
        row     zerosNeeded     orderedDict           firstRow    firstRowIndex    swaps
        0       3               {0:3, 1:0, 2:3, 3:3}  0           0                0
        1       2               {1:0, 2:3, 3:3}       2           1                1
        2       1               {1:0, 3:3}            3           1                2
        3       0               {1:0}                 1           0                2

Complexity:
    Time: O(n**2)
    Space: O(n)
"""

from collections import OrderedDict


class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:

        # Get the number of rows and cols
        n = len(grid)

        # Calcualte zeros for each row
        # Initialize the ordered dict to store rows and their zeros
        zeroCounts = OrderedDict()

        # Iterate through all rows
        for row in range(n):

            count = 0

            # Count the number of consecutive zeros
            for col in range(n - 1, -1, -1):

                # End the count when we see the first one
                if grid[row][col] == 1:
                    break

                # Increment the zeros count
                count += 1

            # Save the row and its zeros count to the dict
            zeroCounts[row] = count


        # Calculate the number of swaps 
        # Intialize the swap to 0
        swaps = 0

        # Iterate through all rows
        for row in range(n):

            # Find the first row that has the required zeros
            for i, (col, count) in enumerate(zeroCounts.items()):

                # If we found one
                if count >= n - row - 1:

                    # Increment the swap based on the row index in the dict
                    swaps += i

                    # Remove such row
                    zeroCounts.pop(col)

                    # Continue to the next row
                    break

                # Else, if we couldn't find one, return -1
                if i == len(zeroCounts) - 1:
                    return -1

        return swaps

