""" 
Problem:
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.

    Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: You will start at index 1.
    - Pay 15 and climb two steps to reach the top.
    The total cost is 15.
    
    Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: You will start at index 0.
    - Pay 1 and climb two steps to reach index 2.
    - Pay 1 and climb two steps to reach index 4.
    - Pay 1 and climb two steps to reach index 6.
    - Pay 1 and climb one step to reach index 7.
    - Pay 1 and climb two steps to reach index 9.
    - Pay 1 and climb one step to reach the top.
    The total cost is 6.

Solution:
    We will solve this problem using a bottom-up dynamic programming approach with caching and monotonic increasing queue. The monotonic increasing queue is used to optimize the look back from O(k) (2 in this case) to O(1). 
    
    Start by adding the first two numbers into the cache and the queue. Ensure that the cost at the front of the queue is the lesser of the two. Next add a "0" to the end of the list. This will be the roof. Then, iterate through all indices from 2 to n-1. At each index, we will ensure that the minimized partial cost in front of the queue is at most k away from the current index. Then, we sum the cost of the current index with the minimized partial cost in front of the queue and cache it as the minimized partial cost of reaching the current index. Lastly, add the current index and its cached minimized partial cost into the queue while maintaining its order. Finally, return the cached minimized partial cost at n-1 as the result.

    Credit: https://leetcode.com/problems/jump-game-vi/discuss/1260737/Optimizations-from-Brute-Force-to-Dynamic-Programming-w-Explanation      

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import deque


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        # Add the roof to store the cost of reaching it
        cost.append(0)

        # Find the number of steps
        n = len(cost)

        # Add the first two steps into the cache
        cache = {0: cost[0], 1: cost[1]}

        # Add both steps (index, cost) into the queue. Ensure that the smaller one go in first
        queue = (
            deque([(0, cost[0]), (1, cost[1])])
            if cost[0] < cost[1]
            else deque([(1, cost[1]), (0, cost[0])])
        )

        # Iterate through all steps
        for i in range(2, n):

            # Pop the minimized partial cost in front the queue that is more than 2 away
            while queue[0][0] < i - 2:
                queue.popleft()

            # Calculate the minimized partial cost to reach the current index
            cache[i] = cost[i] + queue[0][1]

            # Pop any minimized partial costs that are larger than the current minimized partial cost from the end of the queue. There is no point to keeping them as we found a smaller minimized partial cost.
            while queue and queue[-1][1] > cache[i]:
                queue.pop()

            # Add the current index and its minimized partial cost into the queue
            queue.append((i, cache[i]))

        return cache[n - 1]

