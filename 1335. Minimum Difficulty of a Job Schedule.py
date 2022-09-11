"""
Problem:
    You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

    You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

    You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

    Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

    Example 1:
    Input: jobDifficulty = [6,5,4,3,2,1], d = 2
    Output: 7
    Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
    Second day you can finish the last job, total difficulty = 1.
    The difficulty of the schedule = 6 + 1 = 7 
    
    Example 2:
    Input: jobDifficulty = [9,9,9], d = 4
    Output: -1
    Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
    
    Example 3:
    Input: jobDifficulty = [1,1,1], d = 3
    Output: 3
    Explanation: The schedule is one job per day. total difficulty will be 3.

Solution:
    Solve this problem using top-down dp. Let dp be the function that return the minimum difficulty starting from i job and d day. Iterate through all jobs starting at ith job and pick subset of jobs as belonging to the d day. Then, call dp on the rest of job for the d+1 day. Sum the two values to find the minimum difficulty and return the least of them. If we are able to schedule at all jobs for all days, return 0. Else, return infinity.  

Complexity:
    Time: O(m**2n) where m and n is the number of jobs and days
    Space: O(mn)
"""

from functools import lru_cache
from math import inf


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:

        # Initialize the number of jobs and days
        m, n = len(jobDifficulty), d

        # Recursive function to find the minimum difficulty starting at i-th job and d-th day
        @lru_cache(None)
        def dp(i, d):

            # If we have no more job or used up all available days, return 0 if we able to schedule all jobs for all days. Else, return inf
            if i == m or d == n:
                return 0 if i == m and d == n else inf

            # Initialize variables to keep track of largest difficulty starting at ith job and the least minimum difficulty
            difficulty, minDifficulty = 0, inf

            # Itereate through all subset of jobs starting from i and ending from i,...,m
            for i in range(i, m):

                # Update the max difficulty among jobs for this day
                difficulty = max(difficulty, jobDifficulty[i])

                # Calculate the minimum difficulty if we were to schedule the remaining jobs for the next day
                minDifficulty = min(minDifficulty, difficulty + dp(i + 1, d + 1))

            # Return the least minimum difficulty
            return minDifficulty

        return dp(0, 0) if dp(0, 0) != inf else -1
