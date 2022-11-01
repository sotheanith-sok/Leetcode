""" 
Problem:
    You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

    Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

    A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
    A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
    We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

    Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

    Example 1:
    Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    Output: [1,-1,-1,-1,-1]
    Explanation: This example is shown in the photo.
    Ball b0 is dropped at column 0 and falls out of the box at column 1.
    Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
    Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
    Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
    Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
    
    Example 2:
    Input: grid = [[-1]]
    Output: [-1]
    Explanation: The ball gets stuck against the left wall.

    Example 3:
    Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    Output: [0,1,2,3,4,-1]

Solution:
    Use BFS to solve this problem. The key here is that a ball can only move right if the direction of the current grid and the next grid is the same and a ball can only move left if the direction of the current grid and the previous grid is the same. 

    We can simply grid checking by converting grid to defaultdict of 0. 

Complexity:
    Time: O(mn)
    Space: O(n)
"""


from collections import defaultdict, deque
from itertools import product


class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:

        # Get the length of rows and cols
        m, n = len(grid), len(grid[0])

        # Convert grid direction to a defaultdict of 0
        directions = defaultdict(int)
        for row, col in product(range(m), range(n)):
            directions[(row, col)] = grid[row][col]

        # Intialize the result
        res = [-1] * n

        # Initialize the queue
        queue = deque([(i, 0, i) for i in range(n)])

        # Iterate until the queue is empty
        while queue:

            # Get the number of balls at this row
            k = len(queue)

            # Process all balls
            for _ in range(k):

                # Pop a ball
                i, row, col = queue.popleft()

                # If a ball able to pass through the grid, update its exit location
                if row == m:
                    res[i] = col
                    continue

                # Check if a ball can fall right
                if directions[(row, col)] == directions[(row, col + 1)] == 1:
                    queue.append((i, row + 1, col + 1))
                    continue

                # Check if the ball can fall left
                if directions[(row, col)] == directions[(row, col - 1)] == -1:
                    queue.append((i, row + 1, col - 1))
                    continue

        return res

