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
    We can solve this problem using a dynamic programing approach. Start by doubling k since each transaction composes of buying and selling. A maximum profit of prices ending at ith price using k transaction is equal to the largest of maximum profits of prices ending at 0th price to (i-1)th price and using k-1 transaction plus price at ith. Do note that price is negative when k is odd (buying) and positive when k is even (selling). If k == 0, we return 0 since we did not do any transaction. Else if i < 0, return -inf because there is no price. 

    1.  Top-down dp
        Let dp be a function that return the maximum profit of prices ending at ith price and using k transaction. We can solve this function using the following recursive formula.

        dp(i, k) = (1 if k is event else -1) * price[i] + max(dp(prev, k-1)) 
        where prev in (0,..,i-1) and base case of dp(i, k=0) == 0 and dp(i < 0, k > 0) == -inf

        Using the above formula, call dp on all possible i and k and return the largest maxmum profit.

        Unfortunately, this approach will cause a TLE because we have to perfom i-1 lookback for every dp call. 

    2.  Bottom-up dp
        Let m and n be the length of possible prices and k respectively. Use a m x n cache to store maximum profits for all possible i and k. In order to avoid i-1 lookback everytime we calcualte a maximum profit for some arbitrary i and k, we will use a list of n length to store maximum profit from 0,...,i-1 for all k. Using the following formula to fill in the cache.

        cache[i,k] = (1 if k is event else -1) * price[i] * max(k-1) where max = [0, -inf, ..., -inf]

        Return the largest maximum profit.

    Ex: k = 4, prices = [1,2,4,2,5,7,2,4,9,0]

            0        1       2       3       4       5       6       7       8
    -1  _   0       -inf    -inf    -inf    -inf    -inf    -inf    -inf    -inf
    0   1   0       -1      -inf    -inf    -inf    -inf    -inf    -inf    -inf      
    1   2   0       -2       1      -inf    -inf    -inf    -inf    -inf    -inf
    2   4   0       -4       3      -3      -inf    -inf    -inf    -inf    -inf
    3   2   0       -2       1       1      -1      -inf    -inf    -inf    -inf
    4   5   0       -5       4      -2       6      -6      -inf    -inf    -inf
    5   7   0       -7       6      -3       8      -1       1      -inf    -inf
    6   2   0       -2       1       4       3       6       1      -1      -inf
    7   4   0       -4       3       2       8       4       10     -3       3
    8   9   0       -9       8      -3       13     -1       15      1       8
    9   0   0        0      -1       8       4       13      6       15      1

    res = 15

Complexity:
    Time: O(m**2n) for top-down dp and O(mn) for bottom-up dp where m is length of prices and n == 2k
    Space: O(mn)
"""

from functools import lru_cache
from itertools import product
from math import inf

# Top-down dp
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        # If there is no price or we can't do any transaction, return 0
        if k == 0 or not prices:
            return 0

        # Recursive function to calculate maximum profit of prices ending at ith price and using k transaction
        @lru_cache(None)
        def dp(i, k):

            # Base cases:
            # If k == 0, return 0
            # Elif i < 0, return -inf
            if i < 0 or k == 0:
                return 0 if k == 0 else -inf

            # Calculate maximum profit by taking the largest maximum profit ending all previous prices and using k-1 transaction plus the current price
            return (
                max(dp(prev, k - 1) for prev in range(i - 1, -2, -1))
                + (1 if k % 2 == 0 else -1) * prices[i]
            )

        # Intialize the length of prices and all possible k
        m, n = len(prices), k * 2

        # Find the largest maximum price among all possible i and k
        return max(dp(i, k) for i, k in product(range(m), range(n + 1)))

from itertools import product
from math import inf

# Bottom-up dp
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        # If there is no price or we can't do any transaction, return 0
        if k == 0 or not prices:
            return 0

        # Intialize the length of prices and transaction
        m, n = len(prices), k * 2

        # Intialize a list to keep track of largest maximum profits for all possible transactions
        maxProfits = [0] + [-inf] * n

        # Initialize the cache
        cache = {}

        # Iterate through all possible prices and transactions
        for i, k in product(range(m), range(1, n + 1)):

            # Calcualte the maximum profit ending at the ith price and using k transaction
            cache[(i, k)] = (1 if k % 2 == 0 else -1) * prices[i] + maxProfits[k - 1]

            # Update the largest maximum profit using k transaction
            maxProfits[k] = max(maxProfits[k], cache[(i, k)])

        # Return the largest maximum profit lower bound at 0
        return max(0, max(cache.values()))



