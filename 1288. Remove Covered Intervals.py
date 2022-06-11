""" 
Problem:
    Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

    The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

    Return the number of remaining intervals.

    Example 1:
    Input: intervals = [[1,4],[3,6],[2,8]]
    Output: 2
    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
    
    Example 2:
    Input: intervals = [[1,4],[2,3]]
    Output: 1

Solution:
    Sort intervals by the start (increasing order) and then, the end(decreasing order). By sorting like this, a larger intervals will come first for any given start. Then, we will iterate through the sorted intervals and check if the current interval is overlapped by the the previous interval. If it isn't, we add it to the result.  

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:

        # Sort intervals by start (increasing order) and end (decreasing order)
        intervals.sort(key=lambda x: (x[0], -x[1]))

        # Add the first interval to the result
        res = [intervals[0]]

        # Iterate through all intervals
        for l, r in intervals[1:]:
            prev_l, prev_r = res[-1]

            # If the current interval isn't cover by the previous interval
            # Note: Since l>=prev_l, we can just check the right only
            if r > prev_r:

                # Add it to the result
                res.append([l, r])

        return len(res)

