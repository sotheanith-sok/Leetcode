"""
Problem:
    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    The '.' character indicates empty cells.

    Example 1:
    Input: 
    board = 
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Output: 
    [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    Explanation: The input board is shown above and the only valid solution is shown below:

Solution:
    We can solve this problem using backtracking with bitmasks. Bitmask is used to keep track of used numbers. Start by generating bitmasks for each row, col, and box. Then, perform a row-wise traversal through all nodes. At each node, if its value is fixed, we continue to the next node. Else, we pick a number that is available in the three bitmasks as its value and go on to the next node. Return false if we reach a deadend aka when we have not pick numbers for all nodes and there isn't any available number left. We know that we found a solution if we are able to reach nth row. 

Complexity:
    Time: O(2**n)
    Space: O(n)
"""


from itertools import product


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Get the length of the board
        n = len(board)

        # Initiaize the bitmask
        # 2 ** 9 - 1 == 511 == 0b111111111
        bitmask = 2 ** n - 1

        # Initialize dictionaries mapped each row, col, and box to its respective bitmask
        rows, cols, boxes = (
            {i: bitmask for i in range(n)},
            {i: bitmask for i in range(n)},
            {i: bitmask for i in product(range(3), repeat=2)},
        )

        # Initialize a set to keep track of fixed node
        fixed = set()

        # Process fixed nodes
        # Iteration through all nodes
        for row, col in product(range(n), repeat=2):

            # If a node is fixed
            if board[row][col] != ".":

                # Add its coordinate to the set
                fixed.add((row, col))

                # Find its value
                val = int(board[row][col]) - 1

                # Update its three corresponding bitmasks
                rows[row], cols[col], boxes[(row // 3, col // 3)] = (
                    rows[row] ^ 1 << val,
                    cols[col] ^ 1 << val,
                    boxes[(row // 3, col // 3)] ^ 1 << val,
                )

        # Backtracking
        def dfs(row, col):

            # If we reach nth row, we have process all nodes and thus, return True
            if row == n:
                return True

            # Calculate the next node
            nextRow, nextCol = (row, col + 1) if (col + 1 < n) else (row + 1, 0)

            # If the current node isn't fixed
            if (row, col) not in fixed:

                # Iterate through all numbers
                for i in range(n):

                    # If a number is available in the current node's three corresponding bitmasks
                    if (
                        (rows[row] & 1 << i) >> i
                        == (cols[col] & 1 << i) >> i
                        == (boxes[(row // 3, col // 3)] & 1 << i) >> i
                        == 1
                    ):

                        # Update the board with this number
                        board[row][col] = str(i + 1)

                        # Update the current node's corresponding bitmasks
                        rows[row], cols[col], boxes[(row // 3, col // 3)] = (
                            rows[row] ^ 1 << i,
                            cols[col] ^ 1 << i,
                            boxes[(row // 3, col // 3)] ^ 1 << i,
                        )

                        # Go to the next node
                        # If the next node return True, it must lead to a solution and thus, we can end the search here.
                        if dfs(nextRow, nextCol):
                            return True

                        # Else, undo the changes made to the current's node corresponding bitmasks
                        rows[row], cols[col], boxes[(row // 3, col // 3)] = (
                            rows[row] | 1 << i,
                            cols[col] | 1 << i,
                            boxes[(row // 3, col // 3)] | 1 << i,
                        )

                # If there isn't a number that lead to a solution, return False
                return False

            # Else, if the current node is fixed, go to the next node.
            else:
                return dfs(nextRow, nextCol)

        dfs(0, 0)

