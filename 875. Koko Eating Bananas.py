"""
Problem:
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.

    Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4
    
    Example 2:
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30
    
    Example 3:
    Input: piles = [30,11,23,4,20], h = 6
    Output: 23

Solution:
    Koko, a living relative of Harambe, wants to eat all bananas before her zoo keeper return. However, there is a risk of her choking if she eats too fast and thus, we will use binary search to find the slowest speed she has to eat to consume all bananas before her zoo keeper return. 
    
    If her zoo keeper takes infinity hours to return, Koko can eat at the speed of 1 banana per hour and she will still complete her goal. 

    If her zoo keep takes a minimum hours to return, Koko would have to eat each pile in 1 hour and thus, her highest speed is the largest pile.   

Complexity:
    Time: O(nlogn)
    Space: O(1)
"""

from math import ceil, inf


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        # Initialize the lower and upper bound of Koko's speed
        lower, upper = 1, max(piles)

        # Initialize a variable to keep track of Koko's slowest speed
        slowestSpeed = inf

        # Iterate until the lower and upper bounds cross
        while lower <= upper:

            # Calculate the median speed
            speed = (upper - lower) // 2 + lower

            # Given such speed, calculate the amount of hours required for Koko to eat all bananas
            hoursTaken = sum(ceil(pile / speed) for pile in piles)

            # If Koko can eat all banana, try to find a slower speed
            if hoursTaken <= h:
                upper = speed - 1
                slowestSpeed = min(slowestSpeed, speed)

            # Else, Koko needs to eat faster
            else:
                lower = speed + 1

        return slowestSpeed
