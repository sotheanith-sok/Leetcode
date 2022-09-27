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
    We will BFS through all dominoes starting unpushed dominoes with a left pushed dominoe to its right and unpushed dominoes with right pushed dominoe to its left. While queue isn't empty, process all dominoes that will be pushed in this round. A dominoe can't be pushed if its left dominoe is a right pushed dominoe and its right dominoe is a left pushed dominoe. Else, we push such dominoe and add the next unpushed dominoe onto the queue. To avoiding a situation where one dominoe can't be pushed because its neighboring dominoe being pushed at the same round, we will update all dominoe orientation at the end of each round. 

Complexity:
    Time: O(n)
    Space: O(n)

"""

from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        # Convert dominoes to a list for faster updating
        dominoes = list(dominoes)

        # Find the number of dominoes
        n = len(dominoes)

        # A helper function to find the next dominoe
        directions = {"L": -1, "R": 1}

        # Intialize the queue storing dominoes that can be pushed
        queue = deque()

        # Initialize a list storing dominoes to be updated at the end of the round
        update = []

        # Add all dominoes that can be pushed in the first round into the queue
        for i in range(n):

            # If the current dominoe already pushed, skip it
            if dominoes[i] != ".":
                continue

            # If there is a left pushed dominoe to the right of the current dominoe, add the current dominoe into the queue
            if i + 1 < n and dominoes[i + 1] == "L":
                queue.append(i)

            # If there is a right pushed dominoe to the left of the current dominoe, add the current dominoe into the queue
            if i - 1 >= 0 and dominoes[i - 1] == "R":
                queue.append(i)

        # While there is a dominoe to be push
        while queue:

            # Find how many dominoe will be pushed in this round
            k = len(queue)

            # Process all dominoe
            for _ in range(k):

                # Pop a domino
                i = queue.popleft()

                # If a domino can't be pushed because there is a left pushed dominoe to its right and a right pushed dominoe to its left, skip it
                if (
                    i - 1 >= 0
                    and dominoes[i - 1] == "R"
                    and i + 1 < n
                    and dominoes[i + 1] == "L"
                ):
                    continue

                # Else, we can push the current dominoe. Save the dominoe and its new orientation into a list to be updated later
                update.append(
                    (i, "R" if i - 1 >= 0 and dominoes[i - 1] == "R" else "L")
                )

                # Find the next dominoe
                nextI = i + directions[update[-1][1]]

                # If the next dominoe hasn't been pushed, add it into the queue
                if 0 <= nextI < n and dominoes[nextI] == ".":
                    queue.append(nextI)

            # While there is a dominoe to be updated for this round
            while update:

                # Pop a dominoe from the list
                i, val = update.pop()

                # Update its orientation
                dominoes[i] = val

        return "".join(dominoes)

