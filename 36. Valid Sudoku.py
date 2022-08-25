"""
Problem:
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    
    Example 1:
    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true
    
    Example 2:
    Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Solution:
    Use 3 dictionaries to keep track of previously seen values for each row, col, and box. Iterate through all rows and cols. If the value at such row and col is ".", skip it. Else, check if such value exists in the three dictionaries. If yes, return False. Else, add such value to all 3 dictionaries and continue to the next row and col. 

Complexity:
    Time: O(n**2)
    Space: O(n**2)
"""


from collections import defaultdict
from itertools import product


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # Intialize the three dictionaries
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        # Iterate through all rows and cols
        for row, col in product(range(9), range(9)):

            # Find the value at the current row and col
            val = board[row][col]

            # If the current value is a ".", continue to the next entry
            if val == ".":
                continue

            # Else, check if the current value exists in any of the three dictionaries
            if (
                val in rows[row]
                or val in cols[col]
                or val in boxes[(row // 3, col // 3)]
            ):

                # If yes, return False
                return False

            # Else, add the current value to all three dictionaries
            rows[row].add(val)
            cols[col].add(val)
            boxes[(row // 3, col // 3)].add(val)

        return True

