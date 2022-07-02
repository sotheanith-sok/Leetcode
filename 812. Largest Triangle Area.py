""" 
Problem:
    Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

    Example 1:
    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2.00000
    Explanation: The five points are shown in the above figure. The red triangle is the largest.
    
    Example 2:
    Input: points = [[1,0],[0,0],[0,1]]
    Output: 0.50000

Solution:
    Pick three points and find its area using Heron's Formula.

Complexity:
    Time: O(n**3)
    Space: O(1)
"""


from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        res = 0

        # Pick three points
        for a, b, c in combinations(points, 3):

            # Calculate sides
            ab = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
            bc = ((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2) ** 0.5
            ac = ((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) ** 0.5

            # Calculate the area
            semiPerimeter = (ab + bc + ac) / 2

            # Try catch to avoid negative sqrt due to floating
            try:
                area = (
                    semiPerimeter
                    * (semiPerimeter - ab)
                    * (semiPerimeter - bc)
                    * (semiPerimeter - ac)
                ) ** 0.5
                res = max(res, float(area))
            except:
                pass

        return res

