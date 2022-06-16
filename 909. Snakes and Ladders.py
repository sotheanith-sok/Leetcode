""" 
Problem:
    You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

    You start on square 1 of the board. In each move, starting from square curr, do the following:

    Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
    This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
    If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
    The game ends when you reach the square n2.
    A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

    Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

    For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
    Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

    Example 1:
    Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    Output: 4
    Explanation: 
    In the beginning, you start at square 1 (at row 5, column 0).
    You decide to move to square 2 and must take the ladder to square 15.
    You then decide to move to square 17 and must take the snake to square 13.
    You then decide to move to square 14 and must take the ladder to square 35.
    You then decide to move to square 36, ending the game.
    This is the lowest possible number of moves to reach the last square, so return 4.
    
    Example 2:
    Input: board = [[-1,-1],[-1,3]]
    Output: 1

Solution:
    Use bfs to solve this problem. At each iteration, the possible next nodes are the next 6 nodes. If a node is a shortcut (!=-1), replace the current neighboring node with the value at that short cut (aka it doesn't cost anything to jump).

Complexity:
    Time: O(n**2)
    Space: O(n**2)

"""

from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:

        # Get the size of the board
        n = len(board)

        # A helper function to convert from 1d indices to 2d indices.
        def convert(i: int, n=n):
            i = i - 1
            row = n - 1 - (i // n)

            if n % 2 == 0:
                col = n - 1 - (i % n) if row % 2 != 1 else (i % n)
            else:
                col = n - 1 - (i % n) if row % 2 == 1 else (i % n)

            return row, col

        # Intialize a visited set, a queue, and step counter
        visited = set()
        queue = deque()
        step = 0

        # Add the first value to the queue
        visited.add(1)
        queue.append(1)

        # Iterate until the queue is empty
        while queue:

            # Get all nodes at this step
            count = len(queue)

            # Iterate through all node
            for _ in range(count):

                # Pop a node from the queue
                i = queue.popleft()

                # If we found the target, return the step
                if i == n ** 2:
                    return step

                # Add all of its neighboring nodes to the queue
                for nei in range(i + 1, min(i + 6 + 1, n ** 2 + 1)):

                    # Convert the 1d index to a row and a col
                    row, col = convert(nei)

                    # If the current neighboring node is a shortcut, skip to the next node.
                    if board[row][col] != -1:
                        nei = board[row][col]

                    # Add all unvisited neighbors to the queue.
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            step += 1
        return -1

