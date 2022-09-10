"""
Problem:
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

    Find the maximum profit you can achieve. You may complete at most k transactions.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Example 1:
    Input: k = 2, prices = [2,4,1]
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
    
    Example 2:
    Input: k = 2, prices = [3,2,6,5,0,3]
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Solution:
    Solve this problem using dynamic programming. Since each transaction consits of a selling and buying phase, we will double the number of transactions by 2. Then, a maxProfit for prices up to some arbitrary price and using some arbitrary transaction is the maximum between the maxProfit if we were to perform the last transaction on such price vs the maxProfit if we were to perform the last transaction on one of the previous price.

    ie maxProfit(i,k) = max(maxProfit(i-1,k), maxProfit(i-1, k-1) + price[i]) 
    where we return 0 if k==0 and -inf if i < 0.

    Ex: k = 4, prices = [1,2,4,2,5,7,2,4,9,0]

            0        1       2       3       4       5       6       7       8
    -1  _   0       -inf    -inf    -inf    -inf    -inf    -inf    -inf    -inf
    0   1   0       -1      -inf    -inf    -inf    -inf    -inf    -inf    -inf      
    1   2   0       -1       1      -inf    -inf    -inf    -inf    -inf    -inf
    2   4   0       -1       3      -3      -inf    -inf    -inf    -inf    -inf
    3   2   0       -1       3       1      -1      -inf    -inf    -inf    -inf
    4   5   0       -1       4       1       6      -6      -inf    -inf    -inf
    5   7   0       -1       6       1       8      -1       1      -inf    -inf
    6   2   0       -1       6       4       8       6       1      -1      -inf
    7   4   0       -1       6       4       8       6       10     -1       3
    8   9   0       -1       8       4       13      6       15      1       8
    9   0   0        0       8       8       13      13      15      15      8

    res = 15

Complexity:
    Time: O(mn)  where m and n are numbers of prices and transactions
    Space: O(mn)
"""

from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import inf

# Top-down dp
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        # If there is no price or we can't perform any transaction, return 0
        if k == 0 or not prices:
            return 0

        # Intialize the number of prices and transactions
        m, n = len(prices), k * 2

        # A recrusive function to calculate maxProfit using prices up to ith price and using kth transaction
        @lru_cache(None)
        def maxProfit(i, k):

            # Basecase
            if i < 0 or k == 0:
                return 0 if k == 0 else -inf

            # Return the max between maxProfits if we were to perform kth transaction on ith price vs other prices
            return max(
                maxProfit(i - 1, k),
                maxProfit(i - 1, k - 1) + (1 if k % 2 == 0 else -1) * prices[i],
            )

        # Return the largest maxProfit
        return max(maxProfit(i, k) for i, k in product(range(m), range(n + 1)))


# Bottom-up dp
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        # If there is no price or we can't do any transaction, return 0
        if k == 0 or not prices:
            return 0

        # Intialize the number of prices and transactions
        m, n = len(prices), k * 2

        # Intialize the cache to keep track of all maxProfits
        maxProfits = defaultdict(int)
        for k in range(1, n + 1):
            maxProfits[(-1, k)] = -inf

        # Calculate maxProfits for all possible i and k
        for i, k in product(range(m), range(1, n + 1)):
            maxProfits[(i, k)] = max(
                maxProfits[(i - 1, k)],
                maxProfits[(i - 1, k - 1)] + (1 if k % 2 == 0 else -1) * prices[i],
            )

        # Return the largest maxProfit
        return max(maxProfits.values())

