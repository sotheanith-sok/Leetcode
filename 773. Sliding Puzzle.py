"""
Problem:
    On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

    The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

    Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

    Example 1:
    Input: board = [[1,2,3],[4,0,5]]
    Output: 1
    Explanation: Swap the 0 and the 5 in one move.
    
    Example 2:
    Input: board = [[1,2,3],[5,4,0]]
    Output: -1
    Explanation: No number of moves will make the board solved.
    
    Example 3:
    Input: board = [[4,1,2],[5,0,3]]
    Output: 5
    Explanation: 5 is the smallest number of moves that solves the board.
    An example path:
    After move 0: [[4,1,2],[5,0,3]]
    After move 1: [[4,1,2],[0,5,3]]
    After move 2: [[0,1,2],[4,5,3]]
    After move 3: [[1,0,2],[4,5,3]]
    After move 4: [[1,2,0],[4,5,3]]
    After move 5: [[1,2,3],[4,5,0]]

Solution:
    Use BFS to search through all possible state of the board. To simplfy the process, we will flatten the board and store states as a string instead of a 2d list. Start by populating a queue with the initial state. While queue isn't empty, process all states of each move. At each move, pop a state and check if it is equal the end state. If yes, return move used. Else, calculate the next state. If we can't reach an end state, return -1. 

Complexity:
    Time: O(720) there are 720 possible states. 
    Space: O(720)
"""


from collections import deque


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:

        # Map an index to indices of its neighbors
        nextIndices = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [3, 5, 1],
            5: [2, 4],
        }

        # Intialize the start and end states
        start, end = "".join(str(c) for c in board[0] + board[1]), "123450"

        # Add start state to the queue and a set to keep track of visited state
        queue, visited = deque([(start, start.index("0"))]), set([start])

        # Initialize move used starting at 0
        move = 0

        # While queue isn't empty
        while queue:

            # Find how many states to process at the current move
            n = len(queue)

            # Go through all states
            for _ in range(n):

                # Pop a state and index of 0
                state, i = queue.popleft()

                # If we reach the end state, return move used
                if state == end:
                    return move

                # Else, calcualate next states
                for j in nextIndices[i]:

                    # Swap digit at neighboring digits with 0 to calculate next state
                    low, high = min(i, j), max(i, j)

                    nextState = (
                        state[:low]
                        + (
                            (state[j] + state[low + 1 : high] + state[i])
                            if state[low] == state[i]
                            else (state[i] + state[low + 1 : high] + state[j])
                        )
                        + state[high + 1 :]
                    )

                    # If we haven't visit the next state yet, add it the queue
                    if nextState not in visited:
                        queue.append((nextState, j))
                        visited.add(nextState)

            # Increment the move
            move += 1

        return -1

