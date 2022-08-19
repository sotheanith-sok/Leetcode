"""
Problem:
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

    Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

    Example 1:
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
    
    Example 2:
    Input: n = 1
    Output: [["Q"]]

Solution:
    Solve this problem using backtracking. In order to maintain invalid cells, we will use 3 sets: column (col), positive diagonal (row-col), and negative diagonal (row+col). Iterate through every row and try to place a queen at an available column. Once, we are able to reach nth row, we have found a solution. Save such solution before backtracking. 

Complexity:
    Time: O(n!)
    Space: O(n!)
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        # Initialize a board of all "."
        board = [["." for _ in range(n)] for _ in range(n)]

        # Initialize the result
        res = []

        # Initialize the three invalid sets
        cols, posDiag, negDiag = set(), set(), set()

        # Perform backtracking
        def backtrack(row):

            # Once we reached nth row, we have found a solution
            if row == n:

                # Add such board to the result
                res.append(["".join(r) for r in board])
                return

            # Iterate through all columns at the current row
            for col in range(n):

                # If the current column isn't in any of the three invalid set
                if (
                    col not in cols
                    and (row - col) not in posDiag
                    and (row + col) not in negDiag
                ):

                    # Add the current column to the three sets
                    cols.add(col)
                    posDiag.add(row - col)
                    negDiag.add(row + col)

                    # Place a queen
                    board[row][col] = "Q"

                    # Go to the next row
                    backtrack(row + 1)

                    # Once we come back
                    # Remove the current column from the three sets before we are going to the next column
                    cols.remove(col)
                    posDiag.remove(row - col)
                    negDiag.remove(row + col)

                    # Remove the queen
                    board[row][col] = "."

        backtrack(0)

        return res
