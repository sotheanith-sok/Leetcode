"""
Problem:
    There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).

    You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).

    The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:

    The next instruction will move the robot off the grid.
    There are no more instructions left to execute.
    Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.

    Example 1:
    Input: n = 3, startPos = [0,1], s = "RRDDLU"
    Output: [1,5,4,3,1,0]
    Explanation: Starting from startPos and beginning execution from the ith instruction:
    - 0th: "RRDDLU". Only one instruction "R" can be executed before it moves off the grid.
    - 1st:  "RDDLU". All five instructions can be executed while it stays in the grid and ends at (1, 1).
    - 2nd:   "DDLU". All four instructions can be executed while it stays in the grid and ends at (1, 0).
    - 3rd:    "DLU". All three instructions can be executed while it stays in the grid and ends at (0, 0).
    - 4th:     "LU". Only one instruction "L" can be executed before it moves off the grid.
    - 5th:      "U". If moving up, it would move off the grid.
    
    Example 2:
    Input: n = 2, startPos = [1,1], s = "LURD"
    Output: [4,1,0,0]
    Explanation:
    - 0th: "LURD".
    - 1st:  "URD".
    - 2nd:   "RD".
    - 3rd:    "D".
    
    Example 3:
    Input: n = 1, startPos = [0,0], s = "LRUD"
    Output: [0,0,0,0]
    Explanation: No matter which instruction the robot begins execution from, it would move off the grid.

Solution:
    1. BFS
        Intialize starting points for each instruction in s. Then, bfs through all instructions and find how many instruction we can executed for each starting point. Save the amount of instruction executed into the result and return it. 

    2. Suffix Sum
        For a given n and starting position, determine the maximum move possible for all four directions. Then, iterate through s from the end and keep track of the suffix sum(move we took) for both dimensions. At each instruction, if we made more move than it is allowed, find a previous instruction that cause us to move out of bound and save the difference between the two indices as the amount of instruction executable. 
        
        ie if we made x = -5 moves and we can only make y = -2 moves to reach the boundary, we need to find where we made z = x-y = -3 moves. Then, the difference between indices of x moves and z moves will how many execution is possible. 

        Ex: Let work with only one dimesion.
            n = 3, s = 'RLLLLLLLRR', startPoint = 1

            Thus, we can make 2 moves left and right respectively to hit the boundary
            leftMoves = -1-1 = -2, rightMoves = 3-1 = 2

        i   instruction     col     cols(moves -> indices)                          leftBoundary         rightBoundary        res
        0   R              -4       {-5:1, -4:2, -3:3, -2:4, -1:5, 0:6, 1:7, 2:8}  -4-(-2) =-2 ✓        -4-(2) =-6 ✗         4-0-1  = 3
        1   L              -5       {-4:2, -3:3, -2:4, -1:5, 0:6, 1:7, 2:8}        -5-(-2) =-3 ✓        -5-(2) =-7 ✗         3-1-1  = 1
        2   L              -4       {-3:3, -2:4, -1:5, 0:6, 1:7, 2:8}              -4-(-2) =-2 ✓        -4-(2) =-6 ✗         4-2-1  = 1
        3   L              -3       {-2:4, -1:5, 0:6, 1:7, 2:8}                    -3-(-2) =-1 ✓        -3-(2) =-5 ✗         5-3-1  = 1
        4   L              -2       {-1:5, 0:6, 1:7, 2:8}                          -2-(-2) = 0 ✓        -2-(2) = 4 ✗         6-4-1  = 1
        5   L              -1       {0:6, 1:7, 2:8}                                -1-(-2) = 1 ✓        -1-(2) =-3 ✗         7-5-1  = 1
        6   L               0       {0:10, 1:7, 2:8}                                0-(-2) = 2 ✓         0-(2) =-2 ✗         8-6-1  = 1
        7   L               1       {0:10, 1:9, 2:8}                                1-(-2) = 3 ✗         1-(2) =-1 ✗         10-7   = 3
        8   R               2       {0:10, 1:9}                                     2-(-2) = 0 ✓         2-(2) = 0 ✓         10-8-1 = 1
        9   R               1       {0:10}                                          1-(-2) = 3 ✗         1-(2) =-1 ✗         10-9   = 1

Complexity:
    Time: BFS: O(m**2), Suffix Sum: O(m)
    Space: O(m)
"""


from collections import deque

# BFS
class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:

        # A helper function to help with direction
        directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

        # Find the number of instructions
        m = len(s)

        # Intialize the result
        res = [0] * m

        # Intialize the starting point for all instructions
        queue = deque((i, startPos[0], startPos[1], i) for i in range(m))

        # Intialize the number of execution possible
        exe = 0

        # While queue isn't empty
        while queue:

            # Find how many instruction for this execution
            k = len(queue)

            # Go through all instruction
            for _ in range(k):

                # Pop an instruction
                sIndex, row, col, nIndex = queue.popleft()

                # Save the number of execution to the result
                res[sIndex] = exe

                # Go to the next instruction if possible
                if nIndex < m:
                    dRow, dCol = directions[s[nIndex]]
                    nRow, nCol = row + dRow, col + dCol
                    if 0 <= nRow < n and 0 <= nCol < n:
                        queue.append((sIndex, nRow, nCol, nIndex + 1))

            # Increment the number of execution
            exe += 1

        return res


# Suffix sum
class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:

        # Find the number of instructions
        m = len(s)

        # A helper function for four directional movements
        directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

        # Initialize the number of moves possible before we hit a boundary for all 4 directions
        left, right, up, down = (
            -1 - startPos[1],
            n - startPos[1],
            -1 - startPos[0],
            n - startPos[0],
        )

        # Intialize dicts to keep track of indices where we made each moves
        rows, cols = {0: m}, {0: m}

        # Intialize a varaible to keep track of the current moves
        row, col = 0, 0

        # Initialize the result
        res = []

        # Iterate through all instruction starting from the end
        for i in range(m - 1, -1, -1):

            # Find the direction
            dRow, dCol = directions[s[i]]

            # Update the current move
            row, col = row + dRow, col + dCol

            # Initialize the number of instruction executable if we didn't reach a boundary
            exe = m - i

            # If we reach the top boundary, update the number of instruction executable
            if row - up in rows:
                exe = min(exe, rows[row - up] - i - 1)

            # If we reach the bottom boundary, update the number of instruction executable
            if row - down in rows:
                exe = min(exe, rows[row - down] - i - 1)

            # If we reach the left boundary, update the number of instruction executable
            if col - left in cols:
                exe = min(exe, cols[col - left] - i - 1)

            # If we reach the right boundary, update the number of instruction executable
            if col - right in cols:
                exe = min(exe, cols[col - right] - i - 1)

            # Save the current index and moves into dicts
            rows[row], cols[col] = i, i

            # Append the number of instruction executable into the result
            res.append(exe)

        return res[::-1]
