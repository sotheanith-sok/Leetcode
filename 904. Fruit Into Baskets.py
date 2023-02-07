"""
Problem:
    You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
    Given the integer array fruits, return the maximum number of fruits you can pick.

    
    Example 1:
    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.
    
    Example 2:
    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
    If we had started at the first tree, we would only pick from trees [0,1].
    
    Example 3:
    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].
    If we had started at the first tree, we would only pick from trees [1,2].

Solution:
    Maintain a sliding window that represent fruits in the basket. Iterate through all fruits. At each iteration, if we can't add a fruit into the basket, shrink the window until we can. Then, add the current fruit into the basket. Return the largest number of fruits. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        # Find the number of fruits
        n = len(fruits)

        # Initalize the basket and result
        basket, res = defaultdict(int), 0

        # Initialize the left and right pointer
        l, r = 0, 0

        # Iterate through all fruits
        while r < n:

            # If the current fruit can't be added to the basket, remove fruits from the left pointer until we can
            if fruits[r] not in basket and len(basket) == 2:

                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])

                l += 1
                
                continue

            # Add the current fruit into the basket
            basket[fruits[r]] += 1

            # Update the result
            res = max(res, sum(basket.values()))

            r += 1

        return res
