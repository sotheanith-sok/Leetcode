""" 
Problem:
    You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

    Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

    Example 1:
    Input: tasks = [2,2,3,3,2,4,4,4,4,4]
    Output: 4
    Explanation: To complete all the tasks, a possible plan is:
    - In the first round, you complete 3 tasks of difficulty level 2. 
    - In the second round, you complete 2 tasks of difficulty level 3. 
    - In the third round, you complete 3 tasks of difficulty level 4. 
    - In the fourth round, you complete 2 tasks of difficulty level 4.  
    It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
    
    Example 2:
    Input: tasks = [2,3,3]
    Output: -1
    Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.

Solution:
    Count all tasks based on their difficulties. Let c be the count of some arbitrary task. If c == 1, we have found an uncompletable task and thus, we return -1. Else, we will simply divide c by 3 to find the number of round. If c is not divisible by 3, we will add one to the result to compensate for an extra round of 2 tasks.

    Ex: c = 9   =>  x3  x3  x3      =>  3 rounds
        c = 10  =>  x3  x3  x2  x2  =>  4 rounds
        c = 11  =>  x3  x3  x3  x2  =>  4 rounds

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:

        # Count all tasks based on their difficulties
        counts = Counter(tasks).values()

        # Initialize the result
        res = 0

        # Itearate through all tasks
        for count in counts:

            # If the count of the current task is 1, we have found an uncompletable task
            if count == 1:
                return -1

            # Else, find the number of rounds to complete the current task
            res += count // 3 + int(count % 3 != 0)

        return res
