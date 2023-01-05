""" 
Problem:
    There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

    Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

    Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

    Example 1:
    Input: points = [[10,16],[2,8],[1,6],[7,12]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
    - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
    - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
    
    Example 2:
    Input: points = [[1,2],[3,4],[5,6],[7,8]]
    Output: 4
    Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
    
    Example 3:
    Input: points = [[1,2],[2,3],[3,4],[4,5]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
    - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
    - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Solution:
    We will try to find the maximum number of intervals that are not overlapping. Start by sorting all points based on the starting index. 
    
    Then, iterate through all points. If the current interval ends before the previous interval, we want to pick the current interval instead of the previous interval. Else if the current interval ends after the previous interval, we can skip it. Lastly, if there is no overlap between the current and previous intervals, we want to keep both. 

Complexity:
    Time: O(nlong)
    Space:O(1)

"""


from math import inf


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:

        # Sort all intervals based on the starting index
        points.sort()

        # Initialize variables to keep track of the ending of the previous interval and the number of non-overlapping intervals
        ending, res = -inf, 0

        # Iterate through all intervals
        for start, end in points:

            # If the current interval ends before the previous interval, we will pick the current interval and unpick the previous interval
            if ending > end:
                ending = end
                continue

            # Else, if the current interval ends after the previous interval, we will skip the current interval
            if start <= ending:
                continue

            # Lastly, if there is no overlap between the current and previous intervals, we will pick the current interval
            ending = end
            res += 1

        return res
