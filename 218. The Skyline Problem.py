"""
Problem:
    A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

    The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

    lefti is the x coordinate of the left edge of the ith building.
    righti is the x coordinate of the right edge of the ith building.
    heighti is the height of the ith building.
    You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

    The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

    Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

    Example 1:
    Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    Explanation:
    Figure A shows the buildings of the input.
    Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

    Example 2:
    Input: buildings = [[0,2,3],[2,5,3]]
    Output: [[0,3],[5,0]]

Solution:
    For all buildings, there are two potential points of max height changes: start and end. Thus, we will expand each building into (start, height, end) and (end, 0, _) and store (height, end) into a heap such that we can find max height in O(1). The first tuple represents when we add a height into the heap and the second tuple represents when we remove a height from the heap. Since heap can't be empty, we will initialize it with (0, inf). 

    Iterate through all buildings. At each iteration, remove tuples from the heap if it represents a buildings that end before the current start. Then, if the current height isn't 0, add the current height and the current end onto the heap. Lastly, if the current max height is different from the previous max height, append the current start and the current max height onto the res.  

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""

import heapq
from math import inf


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:

        # Expand buildings to account for the start and end of each building. We know a tuple is an end of a building if its height is 0
        buildings = sorted(
            [(start, -height, end) for start, end, height in buildings]
            + [(end, 0, None) for _, end, _ in buildings]
        )

        # Initialize heap and result
        heap, res = [(0, inf)], [(0, 0)]

        # Iterate through all buildings
        for start, height, end in buildings:

            # If there is a builing that end before the current start, remove it from the heap
            while start >= heap[0][1]:
                heapq.heappop(heap)

            # If the current height is greater than 0, add it along with the current end onto the heap
            if height:
                heapq.heappush(heap, (height, end))

            # Find the max height
            maxHeight = -heap[0][0]

            # If the current max height is different from the previous max height, add the current start and max height onto the result
            if maxHeight != res[-1][1]:
                res.append([start, maxHeight])

        return res[1:]
