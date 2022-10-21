"""
Problem:
    Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

    For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

    Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

    Example 1:
    Input: pizza = ["A..","AAA","..."], k = 3
    Output: 3 
    Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
    
    Example 2:
    Input: pizza = ["A..","AA.","..."], k = 3
    Output: 1
    
    Example 3:
    Input: pizza = ["A..","A..","..."], k = 1
    Output: 1

Solution:
    Calculate prefix sum so that we can find how many apple in any submatrix in O(1). Then, we can solve this problem using top-down dp. 
    
    Start with an entire pizza and we will cut horizontally and vertically. For each cut, we will check if a given piece has at least one apple. If yes, we will continue to cut the leftover. Else, we stop because this way of cutting is not invalid. Once we make k-1 cut, check if the leftover has at least 1 apple. If yes, we found found a valid way of cutting. Return the sum of all valid ways of cutting. 

Complexity:
    Time: O(kmn)
    Space: O(kmn)
"""


from collections import defaultdict
from functools import lru_cache
from itertools import product


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:

        # Find the last row and col
        maxRow, maxCol = len(pizza) - 1, len(pizza[0]) - 1

        # Calcualate the prefix sum of apples
        prefix = defaultdict(int)
        for row, col in product(range(maxRow + 1), range(maxCol + 1)):
            prefix[(row, col)] = (
                prefix[(row - 1, col)]
                + prefix[(row, col - 1)]
                - prefix[(row - 1, col - 1)]
                + int(pizza[row][col] == "A")
            )

        # Check if a given submatrix has at least 1 apple
        @lru_cache(None)
        def isValid(minRow, maxRow, minCol, maxCol):
            return (
                prefix[(maxRow, maxCol)]
                - prefix[(minRow - 1, maxCol)]
                - prefix[(maxRow, minCol - 1)]
                + prefix[(minRow - 1, minCol - 1)]
            ) > 0

        # Top-down DP: Recursively cutting the apple
        @lru_cache(None)
        def cut(k, minRow, minCol):

            # If we have 0 cut remaining, check if the left over has at least 1 apple
            if k == 0:

                # Return 1 if yes else 0
                return 1 if isValid(minRow, maxRow, minCol, maxCol) else 0

            # Initialize a variable to store all ways we can cut the pizza
            ways = 0

            # Case 1: Horizontal cuts
            for row in range(minRow, maxRow):

                # Check if the top part of the pizza is valid
                if isValid(minRow, row, minCol, maxCol):

                    # If yes, continue to cut the bottom part of the pizza
                    ways += cut(k - 1, row + 1, minCol)

            # Case 2: Vertical cuts
            for col in range(minCol, maxCol):

                # Check if the left part of the pizza is valid
                if isValid(minRow, maxRow, minCol, col):

                    # If yes, continue to cut the right part of the pizza
                    ways += cut(k - 1, minRow, col + 1)

            return ways

        return cut(k - 1, 0, 0) % (10 ** 9 + 7)

