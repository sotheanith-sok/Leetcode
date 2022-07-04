""" 
Problem:
    There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

    In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

    Your score is the sum of the points of the cards you have taken.

    Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

    

    Example 1:

    Input: cardPoints = [1,2,3,4,5,6,1], k = 3
    Output: 12
    Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
    Example 2:

    Input: cardPoints = [2,2,2], k = 2
    Output: 4
    Explanation: Regardless of which two cards you take, your score will always be 4.
    Example 3:

    Input: cardPoints = [9,7,7,9,7,7,9], k = 7
    Output: 55
    Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Solution:
    Initially, we assume that we pick all values from the left. If we pick all available value, we have found the answer. Else, we will start picking value from the right, undo the picked at the left, and keep track of the total. Return the largest total.  

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:

        # Get the number of cards
        N = len(cardPoints)

        # If we have to pick all cards, return the sum of all points
        if k == N:
            return sum(cardPoints)

        # Initialze the total and the result and set them to the sum of k cards from the left
        res = total = sum(cardPoints[:k])
        l = k - 1

        # Start picking cards from the right
        for r in range(N - 1, N - k - 1, -1):

            # Update the total
            total = total - cardPoints[l] + cardPoints[r]

            # Decrement the left pointer
            l -= 1

            # Update the result if the total is largest than the result
            res = max(res, total)

        return res

