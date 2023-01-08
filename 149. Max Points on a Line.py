""" 
Problem:
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

    Example 1:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3
    
    Example 2:
    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

Solution:
    We will solve this problem using bruteforce. 

    A line can be represent using the formula y = mx + b where m is the slope and b is the y-intercept. Thus, we can group all points together if all pairs of points form the same line based on m and b.

    Start by iterate through all possible pairs of points. For each pair, calculate the slope and y-intercept and add both points into their corresponding group. Lastly, return a line that has the most points. 

Complexity:
    Time: O(n**2)
    Space: O(n**2)
"""


from collections import defaultdict


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:

        # Given two points, find the slope and y-intercept
        def line(x1, y1, x2, y2):

            # Special case for a vertical line
            if x1 == x2:
                return x1, None

            # Special case for a horizontal line
            if y1 == y2:
                return None, y1

            # Calculate and return the slope and y-intercept
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1

            return m, b

        # Find the number of points and initialize a dict to keep track of all lines and their corresponding points
        n, counts = len(points), defaultdict(set)

        # Iterate through all possible pairs of points without duplication
        for i in range(n):
            for j in range(i + 1, n):

                # Find both components of each point
                x1, y1 = points[i]
                x2, y2 = points[j]

                # Calculate the slope and y-intercept
                m, b = line(x1, y1, x2, y2)

                # Add both points into the corresponding line
                counts[(m, b)].add((x1, y1))
                counts[(m, b)].add((x2, y2))

        # Return a line with the most points
        return 1 if not counts else len(max(counts.values(), key=len))
