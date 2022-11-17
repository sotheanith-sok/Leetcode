""" 
Problem:
    Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

    The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

    The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

    Example 1:
    Rectangle Area
    Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
    Output: 45
    
    Example 2:
    Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
    Output: 16

Solution:
    Find the overlap area and subtract it from the sum of both rectangle area.

Complexity:
    Time: O(1)
    Space: O(1)
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        # Calculate overlapping area
        overlap = (
            0
            if ay1 >= by2 or by1 >= ay2 or bx1 >= ax2 or ax1 >= bx2
            else (min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1))
        )

        # Calculate areas of both rectangles
        areaA, areaB = (ay2 - ay1) * (ax2 - ax1), (by2 - by1) * (bx2 - bx1)

        return areaA + areaB - overlap
