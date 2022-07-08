""" 
    There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

    A neighborhood is a maximal group of continuous houses that are painted with the same color.

    For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
    Given an array houses, an m x n matrix cost and an integer target where:

    houses[i]: is the color of the house i, and 0 if the house is not painted yet.
    cost[i][j]: is the cost of paint the house i with the color j + 1.
    Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

    Example 1:
    Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
    Output: 9
    Explanation: Paint houses of this way [1,2,2,1,1]
    This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
    Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
    
    Example 2:
    Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
    Output: 11
    Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
    This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
    Cost of paint the first and last house (10 + 1) = 11.
    
    Example 3:
    Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
    Output: -1
    Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.

Solution:
    Solve this problem using top-down dynamic programming approach. Starting from house 0, we check if we can paint such house. If yes, we will find costs of painting each color plus the cost of painting subsequence house(we recursive call here). Then, we take the minimum of all costs and return it. If no, we will skip to the subsequence house without painting. Cache the result using house, remaining neighborhood, and previous paint as the key.     

Complexity:
    Time: O(m*n)
    Space: O(m*n)
"""


from math import inf


class Solution:
    def minCost(
        self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int
    ) -> int:

        # Initialize the cache
        cache = {}

        # Perform DFS
        def dfs(i, r, pp):

            # Use index, remaining neighborhood, and the previous paint as the key
            key = (i, r, pp)

            # If we paint all houses or there is no remaining neighborhood or there isn't enough houses to form the remaining neighborhood,
            if i == len(houses) or r < 0 or len(houses) - i < r:

                # Return 0 if we painted all houses and succesfully form required neighborhood else infinity
                return 0 if i == len(houses) and r == 0 else inf

            # If this key isnt cached before
            if key not in cache:

                # If we have to paint this house
                if houses[i] == 0:

                    # Find the cost of painting this house using each color and recursively check subsequence houses
                    cache[key] = min(
                        [
                            cost[i][cp - 1] + dfs(i + 1, r - (pp != cp), cp)
                            for cp in range(1, len(cost[0]) + 1)
                        ]
                    )

                # Else, if we don't have to paint this house, move on to the next house
                else:
                    cache[key] = dfs(i + 1, r - (houses[i] != pp), houses[i])

            return cache[key]

        res = dfs(0, target, -1)

        return res if res != inf else -1

