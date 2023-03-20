"""
Problem:
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

    Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true
    
    Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

Solution:
    Iterate through all beds in the flowerbed and plant as much flower as possible. Return true if we planted all flowers. Else, return false.

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        # Get the number of beds
        m = len(flowerbed)

        # Plant as many flowers as possible starting from the left
        for i in range(m):

            # If there is no flower remaining to be plant, end the planting
            if n == 0:
                break

            # If we can't plant a flower at the current bed, skip it
            if (
                flowerbed[i] == 1
                or (i - 1 >= 0 and flowerbed[i - 1]) == 1
                or (i + 1 < m and flowerbed[i + 1] == 1)
            ):
                continue

            # Else, plant a flower
            flowerbed[i] = 1

            # Decrement the number of remaining flowers to be plant
            n -= 1

        return n == 0
