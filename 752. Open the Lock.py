""" 
Problem:
    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

    Example 1:
    Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
    Output: 6
    Explanation: 
    A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
    Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
    because the wheels of the lock become stuck after the display becomes the dead end "0102".
    
    Example 2:
    Input: deadends = ["8888"], target = "0009"
    Output: 1
    Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
    
    Example 3:
    Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
    Output: -1
    Explanation: We cannot reach the target without getting stuck.

Solution:
    Use BFS to solve this problem. Each number has 8 possible next moves (+1/-1 for every slots). Noted that if "0000" is given as a deadend or we can't reach the target, return -1. 

Complexity:
    Time: O(10**4)
    Space: O(10**4)
"""


from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:

        # Add all deadends to the visited set
        visited = set(deadends)

        # If the starting num is a deadend, return -1
        if "0000" in visited:
            return -1

        # Initialize our queue and add the starting num to it.
        queue = deque()
        queue.append("0000")
        visited.add(queue[0])

        # A helper array for easier calculation of next possible nums.
        helper = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1), (3, 1), (3, -1)]

        # We start with 0 move
        move = 0

        while queue:

            # Find how many nums we have to process for this level.
            n = len(queue)

            # Iterate through all nums
            for _ in range(n):

                # Pop a num
                nums = queue.popleft()

                # If the current num is the target, return the number of move
                if nums == target:
                    return move

                # Else, add all next possible nums to the queue
                for i, op in helper:
                    new_num = nums[:i] + str((int(nums[i]) + op) % 10) + nums[i + 1 :]
                    if new_num not in visited:
                        queue.append(new_num)
                        visited.add(new_num)

            # Increment the move if we can't find the target.
            move += 1

        return -1

