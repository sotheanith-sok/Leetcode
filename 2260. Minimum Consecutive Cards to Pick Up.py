""" 
Problem:
    You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

    Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

    Example 1:
    Input: cards = [3,4,2,3,4,7]
    Output: 4
    Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
    
    Example 2:
    Input: cards = [1,0,5,3]
    Output: -1
    Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.

Solution:
    Use a sliding window to solve this problem. Initalize the left and the right pointers to keep track of the window and a set to keep track of seen card. Iterate through all cards using the right pointer. If we saw such card before, shrink the window by increment the left pointer until the condition no longer true. Save the smallest window and continue to the next number.

Complexity:
    Time: O(n)
    Space: O(n)
"""
from math import inf


class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:

        # Initialize the a set to store seen cards
        seen = set()

        # Initialize the left pointer
        l = 0

        # Initialize the res to infinity
        res = inf

        # Get the number of cards
        N = len(cards)

        # Iterate through all cards
        for r in range(N):

            # If we have seen a card at the right pointer before, shrink the window
            while cards[r] in seen:
                res = min(res, r - l + 1)
                seen.remove(cards[l])
                l += 1

            # Mark the card at the right window as seen
            seen.add(cards[r])

        return res if res != inf else -1

