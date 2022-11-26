""" 
Problem:
    We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

    You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

    If you choose a job that ends at time X you will be able to start another job that starts at time X.

    Example 1:
    Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
    Output: 120
    Explanation: The subset chosen is the first and fourth job. 
    Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
    
    Example 2:
    Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
    Output: 150
    Explanation: The subset chosen is the first, fourth and fifth job. 
    Profit obtained 150 = 20 + 70 + 60.
    
    Example 3:
    Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
    Output: 6

Solution:
    Use bottom-up dp to solve this problem. 
    
    Start by initializing a dp cache of tuples of (endTime, maxProfitUpToSuchTime). 
    
    Then, sort all jobs by the ending time. 
    
    Next, iterate through all jobs. For each job, try to find a previous job in the cache that end before the start of the current job and has the largest profit (Use binary search here). 
    
    Then, check if performing the current job can contribute to such profit so that the outcoming max profit is greater than the previous max profit. If yes, add such ending time and new max profit into the cache.    

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


from bisect import bisect_right
from math import inf


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        
        # Sort all jobs by the ending time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda job: job[1])

        # Initialize the dp cache
        dp = [(0, 0)]

        # Iterate through all jobs
        for start, end, profit in jobs:

            # Use binary search to find a previous job that end before the start of the current job and has the largest profit 
            i = bisect_right(dp, (start, inf)) - 1

            # If performing the current job contributes to the maximum possible profit
            if dp[i][1] + profit > dp[-1][1]:

                # Add the current jobs and new max profit into the cache
                dp.append((end, dp[i][1] + profit))

        return dp[-1][1]
