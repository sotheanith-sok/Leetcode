""" 
Problem:
    A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

    Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

    If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

    Example 1:
    Input: stones = [0,1,3,5,6,8,12,17]
    Output: true
    Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
    
    Example 2:
    Input: stones = [0,1,2,3,4,8,9,11]
    Output: false
    Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

Solution:
    We can solve this problem using top-down dp. To start, we will check if we can reach the 2nd stone using 1 unit of jump. If yes, we continue to dp algorithm. 

    Let dp(stone, step) be the function that check if a frog started at a given 'stone' and reached such stone using 'step' unit can reach the final stone. 

    Then, for each iteration of dp, we just keep moving the frog forward using k-1, k, and k+1 step. 
    
    The largest possible step would be the distance between the first and last stone since any larger step will land the frog in water. 

Complexity:
    Time: O(nk) where n is the number of stones and k is the distance between the first and last stones
    Space: O(nk)
"""


from functools import lru_cache


class Solution:
    def canCross(self, stones: list[int]) -> bool:

        # Check if a frog can jump to the second stone
        if stones[1] - stones[0] > 1:
            return False

        # Initialize the start and end stone
        start, end = stones[1], stones[-1]

        # Convert stones to a set for O(1) check
        stones = set(stones)

        # Start dp
        @lru_cache(None)
        def dp(stone, step):

            # If we reached the last stone, return True
            if stone == end:
                return True

            # Else, move the frog forward using the three steps size
            for nextStep in [step - 1, step, step + 1]:
                nextStone = stone + nextStep

                # If a frog is moving forward and the next step is a stone
                # Check if such move will land the frog at the last stone
                # If yes, return True
                if nextStep > 0 and nextStone in stones and dp(nextStone, nextStep):
                    return True

            # Return False if we can't reach the last stone
            return False

        return dp(start, 1)