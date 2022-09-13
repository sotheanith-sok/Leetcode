"""
Problem:
    A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

    Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

    The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

    The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

    Return the number of minutes needed to inform all the employees about the urgent news.

    Example 1:
    Input: n = 1, headID = 0, manager = [-1], informTime = [0]
    Output: 0
    Explanation: The head of the company is the only employee in the company.

    Example 2:
    Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
    Output: 1
    Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
    The tree structure of the employees in the company is shown.

Solution:
    Doing top-down approach by calculating the maximum cost starting from the head of the company requires us to build an adjacency list which cost O(n). Let avoid doing this by working from the bottom-up.

    The cost to inform an employee is the cost for his manager to inform him + the cost to inform his manager. If an employee doesn't have a manager, return 0 as the cost to inform him. 

    Iterate through all employees and return the higest cost. Since we are starting from each employee up to the head of the company, use caching to avoid repeated works. 

Complexity:
    Time: O(n)
    Space: O(n)
"""
from functools import lru_cache


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: list[int], informTime: list[int]
    ) -> int:

        # Recursively calculate the cost to inform an employee
        @lru_cache(None)
        def cost(employee):
            # If an employee doesn't have a manager, return 0 as the cost to inform such employee
            if manager[employee] == -1:
                return 0

            # Else, calculate the cost to inform such employee as the cost for his manager to inform him + the cost to inform his manager
            return informTime[manager[employee]] + cost(manager[employee])

        # Return the largest cost
        return max(cost(i) for i in range(n))
