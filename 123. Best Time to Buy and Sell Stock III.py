""" 
Problem:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete at most two transactions.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
    
    Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
    
    Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

Solution:
    Remember that we can make multiple transactions at the same day as long as we hold at most one stock. For every price, we will calculate two cases.

    1. For the first buy, we can keep track of the minimum price and subtract it with the current price. Then, we store the largest difference which will be the profit from the first buy.

    2. For the second buy, we will do the same but we also consider the profit of the first buy. The cost of the second buy is the minimum price subtract the profit from the first buy. Then, we will maximum the profit similarly to the first case. 
    Cost of second buy will always be the same as cost of the first buy unless the profit of the first sell is able to offset the cost of the second buy to be lesser than the cost of first buy. This ensure that we won't make the second buy unless it is profitable.

    Ex: arr = [1, 100, 2, 25]
        price   cost1   profit1     cost2   profit2
        1       1       0           1       0
        100     1       99          1       99
        2       1       99          -97     99
        25      1       99          -97     122
        
Complexity:
    Time: O(n)
    Space: O(1)
"""
from math import inf


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # Initialize the cost of first and second buy
        firstCost, secondCost = inf, inf

        # Initialize the profit of first and second sell
        firstProfit, secondProfit = 0, 0

        # Iterate through all prices
        for price in prices:

            # Update the cost of the first buy
            firstCost = min(firstCost, price)

            # Update the profit on the first sell
            firstProfit = max(firstProfit, price - firstCost)

            # Update the cost of the second buy inluding the profit of the first sell
            # Cost of second buy will always be the same as cost of the first buy unless the profit of the first sell is able to offset the cost of the second buy to be lesser than the cost of first buy.
            # This ensure that we won't make the second buy unless it is profitable.
            secondCost = min(secondCost, price - firstProfit)

            # Update the profit of the second sell
            secondProfit = max(secondProfit, price - secondCost)

        return secondProfit


