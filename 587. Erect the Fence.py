""" 
Problem:
    You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

    You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

    Return the coordinates of trees that are exactly located on the fence perimeter.

    

    Example 1:


    Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
    Example 2:


    Input: points = [[1,2],[2,2],[4,2]]
    Output: [[4,2],[2,2],[1,2]]

Solution:
    Solve this problem by using Graham Scan algorithm. There are two parts to the algorithm. 

    1. Orientation: we can find orientation of any three points by comparing the difference between the two slopes (P1->P2 vs P2->P3).

        All points lower than the left most points:
        > 1 : clockwise
        0   : collinear
        < 1 : counter-clockwise

        All points higher than the left most points:
        > 1 : counter-clockwise
        0   : collinear
        < 1 : clockwise

    2. Graham Scan: Start by sorting all points. Then, we will maintain two lists of all valid points for upper half and lower half as we move counter-clockwise from the left most point. 
    
    Iterate through all points. If there are at least two previous points, check the orientation of the three points. If the orientation concaved inward, remove a previous point from the list and check again. Three points are concaved inward if it has a clockwise orientation. Lastly, add the current point to both lists and continue. 

    Extra Read: 
    1. https://www.geeksforgeeks.org/orientation-3-ordered-points/
    2. https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
    3. https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/


Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:

        # Check the orientation a given three points
        def orientation(p1, p2, p3):
            # Slope1 - Slope2 = 
            # [(p2y - p1y) / (p2x - p1x)] - [(p3y - p2y) / (p3x - p2x)]
            # [(p2y - p1y) * (p3x - p2x)] - [(p3y - p2y) * (p2x - p1x)] 
            return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])

        # Sort all points
        points = sorted(trees)

        # Initialize the lower and upper half
        upper, lower = [], []

        # Iterate through all points
        for point in points:

            # Upper: Remove previous points if it concaved inward when form with the current point
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], point) < 0:
                upper.pop()

            # Lower: Remove previous points if it concaved inward when form with the current point
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], point) > 0:
                lower.pop()

            # Add the current points to both lists
            upper.append(point)
            lower.append(point)

        # Merge the two lists and remove duplicated points
        return [[x, y] for x, y in set((x, y) for x, y in upper + lower)]
