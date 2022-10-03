"""
Problem:
    Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

    Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

    Return the minimum time Bob needs to make the rope colorful.

    Example 1:
    Input: colors = "abaac", neededTime = [1,2,3,4,5]
    Output: 3
    Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
    Bob can remove the blue balloon at index 2. This takes 3 seconds.
    There are no longer two consecutive balloons of the same color. Total time = 3.
    
    Example 2:
    Input: colors = "abc", neededTime = [1,2,3]
    Output: 0
    Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
    
    Example 3:
    Input: colors = "aabaa", neededTime = [1,2,3,4,1]
    Output: 2
    Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
    There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

Solution:
    We can be greedy here. Iterate through all ballons. If the current ballon is a different color than the previous ballon, keep it and continue to the next ballon. Else, if we take more time to remove the previous ballon than the current ballon, discard the current ballon. Else, discard the previous ballon. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:

        # Find the number of ballons
        n = len(colors)

        # Initialize a variable to store time needed and a pointer points to the previous ballon
        res, j = 0, 0

        # Iterate through all ballons
        for i in range(1, n):

            # If the current ballon is a different color than the previous ballon, keep it
            if colors[i] != colors[j]:

                # Set the previous ballon pointer to point to the current ballon
                j = i

                continue

            # Else, we need to remove either the current ballon or the previous ballon
            res += min(neededTime[i], neededTime[j])

            # Update the previous pointer to point to the ballon that we keep
            j = i if neededTime[i] > neededTime[j] else j

        return res
