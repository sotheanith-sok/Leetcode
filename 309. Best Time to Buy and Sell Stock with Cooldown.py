""" 
Problem:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Example 1:
    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]
    
    Example 2:
    Input: prices = [1]
    Output: 0

Solution:
    Let dp be the function that return the max profit after an arbitrary i-th transactions. Thus, we can define dp as

        dp(i) = max(
            dp[i-1],
            prices[i] - prices[j] + dp[j-2] for j in range(i)
        )

        where
            dp[i-1]: 
                If we don't sell at i-th transaction

            prices[i] - prices[j] + dp[j-2] for j in range(i): 
                If we sell at i-th transaction and we must buy a stock at a j-th previous transaction. dp[j-2] to account for the cooldown.

    Optimization 1: Reduce the lookback to O(1) by maintain a varaible to keep track of the largest difference between "dp[j-2]" and "prices[j]"

    Optimization 2: Reduce dp cache to 3 profit varaibles: dp[i-2], dp[i-1], dp[i] == profit1, profit2, profit3

Complexity:
    Time: O(n)
    Space: O(1)
"""


from collections import defaultdict

# Solution 1: O(n**2) time
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # Find the number of prices and initialize the dp cache
        n, dp = len(prices), defaultdict(int)

        # Iterate through all prices starting from the second price
        for i in range(1, n):

            # Calculate the maximum profit ending at the current transaction
            dp[i] = max(
                dp[i - 1], max(prices[i] - prices[j] + dp[j - 2] for j in range(i))
            )
            
        return dp[n - 1]


# Solution 2: O(n) time
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # Find the number prices and initialize the dp cache and max differenc
        n, dp, maxDiff = len(prices), defaultdict(int), -prices[0]

        # Iterate through all prices starting from the second price
        for i in range(1, n):

            # Calculate the maximum profit ending at the current transaction
            dp[i] = max(dp[i - 1], maxDiff + prices[i])

            # Update the max difference for the next price
            maxDiff = max(maxDiff, dp[i - 2] - prices[i])

        return dp[n - 1]


# Solution 3: O(1) Space
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # Find the number of prices and initialize the max difference
        n, maxDiff = len(prices), -prices[0]
        
        # Initialize the three max profits ending at i-2, i-1, and i transactions
        profit1 = profit2 = profit3 = 0

        # Iterate through all prices starting from the second price
        for i in range(1, n):

            # Update the max profit ending at ith transaction
            profit3 = max(profit2, maxDiff + prices[i])

            # Update the max difference
            maxDiff = max(maxDiff, profit1 - prices[i])

            # Update the max profit ending at i-2 and i-1 transactions
            profit1, profit2 = profit2, profit3

        # Return the max profit ending at the last transaction
        return profit3
