""" 
Problem:
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
    
    Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

Solution:
    Let dp be the function that return the max profit if we rob a series of houses ending at some arbitrary ith house. For each house, there are two options:
        1. Skip the previous house and rob the current house
        2. Rob the previous house and skip the current house
    Then, we just have to consider both options and return the largest profit

    So we can define dp as the following:
        maxProfit(i) = max(profit[i] + maxProfit(i-2), maxProfit(i-1))

Complexity:
    Time: O(n)
    Space: O(n)
"""


from functools import lru_cache


class Solution:
    def rob(self, nums: list[int]) -> int:

        # Get the number of houses
        n = len(nums)

        # DP function to return max profit after robbing a series of houses ending at an ith house
        @lru_cache(None)
        def maxProfit(i):

            # If the current house doesn't exist, return 0
            if i < 0:
                return 0

            # Return the max profit between robbing and not robbing the current house
            return max(nums[i] + maxProfit(i - 2), maxProfit(i - 1))

        return maxProfit(n - 1)
