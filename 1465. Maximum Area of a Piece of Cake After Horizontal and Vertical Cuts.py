""" 
Problem:
    You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

    horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
    verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
    Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

    Example 1:
    Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
    Output: 4 
    Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
    
    Example 2:
    Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
    Output: 6
    Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
    
    Example 3:
    Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
    Output: 9

Solution:
    In order to find the the largest area of a rectangle, we have to find the largest width and height. Sort the horizontal cuts and append the height to the end the list. Find the largest distance given values in the horizontal cuts as the range. Repeat the process for the vertical cuts. Return the area calculate from the largest width and height as the result.  

Complexity:
    Time: O(max(mlogm, nlongn)) where m is the size of the horitonztal cuts and n is the size of the vertical cuts.
    Space: O(1)
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:

        # Sort the cuts
        horizontalCuts.sort()
        verticalCuts.sort()

        # Append width and height to the cut
        verticalCuts.append(w)
        horizontalCuts.append(h)

        # Find the largest height
        largestHeight, prevHeight = 0, 0
        for curHeight in horizontalCuts:
            largestHeight, prevHeight = max(largestHeight, curHeight - prevHeight), curHeight

        # Find the largest width
        largestWidth, prevWidth = 0, 0
        for curWidth in verticalCuts:
            largestWidth, prevWidth = max(largestWidth, curWidth - prevWidth), curWidth

        return int((largestHeight * largestWidth) % 1000000007)

