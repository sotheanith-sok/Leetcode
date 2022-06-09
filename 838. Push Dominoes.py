""" 
Problem:
    There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

    After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

    When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

    For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

    You are given a string dominoes representing the initial state where:

    dominoes[i] = 'L', if the ith domino has been pushed to the left,
    dominoes[i] = 'R', if the ith domino has been pushed to the right, and
    dominoes[i] = '.', if the ith domino has not been pushed.
    Return a string representing the final state.

    Example 1:
    Input: dominoes = "RR.L"
    Output: "RR.L"
    Explanation: The first domino expends no additional force on the second domino.
    
    Example 2:
    Input: dominoes = ".L.R...LR..L.."
    Output: "LL.RR.LLRRLL.."

Solution:
    We will simulate every dominoe using a queue. To start with, we will add all pushed dominoes into a queue (index, val). Then, while a queue is not empty, we pop a domino and check if it pushed left or right. If it is pushed left, we will check if the previous domino can be pushed. If yes, we push it and add that domino to the queue. If it is pushed right, we will check if the first next domino can be pushed. If yes, we also check if the second next domino is being pushed left. If yes, we won't push the first next domino and pop a domino from a queue(the second next domino should be the one on top). Else, we will push the first next domino and add it the queue. 

Complexity:
    Time: O(n)
    Space: O(n)

"""


from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        # Get the number of dominoes
        N = len(dominoes)

        # Convert str to list for easier editing
        dominoes = list(dominoes)

        # Use doublely link list for O(1) pop from the start and the end.
        queue = deque()

        # Find all dominoes that being pushed and add them to the queue.
        for i, v in enumerate(dominoes):
            if v != ".":
                queue.append((i, v))

        # While queue isn't empty.
        while queue:

            # Pop a domino
            i, v = queue.popleft()

            # If pushed left, check if the previous dominio can be pushed. If yes, push it and add the previous domino into the queue.
            if v == "L" and i - 1 >= 0 and dominoes[i - 1] == ".":
                dominoes[i - 1] = "L"
                queue.append((i - 1, dominoes[i - 1]))

            # If pushed right, check if the first next domino can be pushed. 
            if v == "R" and i + 1 < N and dominoes[i + 1] == ".":

                # If yes, check if the second next domino is being pushed left.
                if i + 2 < N and dominoes[i + 2] == "L":
                    # If yes, don't push the domino and pop a domino from the queue (It should be the second next domino).
                    queue.popleft()

                # Else, push the next domino and add it to the queue
                else:
                    dominoes[i + 1] = "R"
                    queue.append((i + 1, dominoes[i + 1]))

        return "".join(dominoes)
