""" 
Problem:
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

    Given an integer n, return the number of distinct solutions to the n-queens puzzle.

    Example 1:
    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

    Example 2:
    Input: n = 1
    Output: 1

Solution:
    We can solve this problem with backtracking. Since adding a queen to any row will invalidate all colums at that row, we will iterate through all rows only. At any given row, we can check all columns and if it hasn't invalidated by the previous queen, we add a queen onto it and proceed to the next row. Once, we have added n queens, we found a distinct solution. 
    
    We will use three sets to keep track of if a column, a positive diagonal, or a negative diagonal has been invalidated. The trick is that for any given (m,n) entry, any subsequence entries in its positive diagonal will have their differences be the same as the orignal entry. i.e. m-n == m+1 - n+1 == m+2 - n+2 and so on. Thus, we only need a single value in the set to represent all entries in a positive diagonal. Similar, situation applied to the negative diagonal direction but we do the sum instead of the difference. i.e. m+n == m+1 + n+1 == m+2 + n+2 and so on.   

Complexity:
    Time: O(n!)
    Space: O(n!)

"""


class Solution:
    def totalNQueens(self, n: int) -> int:

        # Use three sets to keep track of invalided columns, positive diagonals, and negative diagonals.
        cols, pos_diag, neg_diag = set(), set(), set()

        # Keep track of how many distinct solution we have found
        count = 0

        # Backtracking
        def backtrack(row, cols, pos_diag, neg_diag):

            # Once we iterate through all rows, we found a solution
            if row == n:
                nonlocal count
                count += 1

            # Check all columns for a given row
            for col in range(n):

                # If it hasn't been invalidated
                if (
                    col not in cols # columns
                    and (col - row) not in pos_diag # positive diagonals
                    and (col + row) not in neg_diag # negative diagonals
                ):

                    # Add it to the three sets and proceed to the next row.
                    backtrack(
                        row + 1,
                        cols.union({col}),
                        pos_diag.union({col - row}),
                        neg_diag.union({col + row}),
                    )

        backtrack(0, cols, pos_diag, neg_diag)
        return count

