"""
Problem:
    You are given an array of integers distance.

    You start at point (0,0) on an X-Y plane and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

    Return true if your path crosses itself, and false if it does not.

    Example 1:
    Input: distance = [2,1,1,2]
    Output: true
    
    Example 2:
    Input: distance = [1,2,3,4]
    Output: false
    
    Example 3:
    Input: distance = [1,1,1,1]
    Output: true

Solution:
    Below are three configurations such that a series of lines will cross itself. The orentiation doesn't of lines does not matter. Thus, check if a series of lines match one of the three configurations. If yes, return True. Else, continue to the next line.


    Case 1                  Case 2                  Case 2
                c                       d                       e
       +----------------+      +----------------+      +----------------+
       |                |      |                |      |                |
       |                |      |                |      |                |
     b |                | d  c |                | e  d |                | f
       |                |      |                |      |                |    a
       +--------------->|      |                |      |                | <----+
                a       |      |                ^ a    |                |      | b
                               |                |      |                       |
                               +----------------+      +-----------------------+
                                        b                       c

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:

        # Initialize the latest 6 lines to 0
        a = b = c = d = e = f = 0

        for n in distance:
            f, e, d, c, b, a = e, d, c, b, a, n

            # Case 1: 4 lines configuration that can cross iself
            if d > 0 and c <= a and b <= d:
                return True

            # Case 2: 5 lines configuration that can cross iself
            if e > 0 and b == d and c <= a + e:
                return True

            # Case 3: 6 lines configuration that can cross iself
            if (
                f > 0
                and c >= a
                and c >= e
                and c <= a + e
                and d >= b
                and d >= f
                and d <= b + f
            ):
                return True
                
        return False

