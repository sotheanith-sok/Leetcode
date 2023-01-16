"""
Problem:
    You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
    
    Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Solution:
    Insert the new interval into the list of intervals while maintaining its sorted order. Then, iterate through the list of intervals and continue merge all overlapping intervals. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from bisect import insort


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:

        # Insert the new interval into the list of intervals while maintaining its sorted order
        insort(intervals, newInterval, key=lambda val: val[0])

        # Initialize the stack to keep track of valid intervals
        stack = []

        # Iterate through all intervals
        for start, end in intervals:

            # If there is a previous inteval in the stack and it is overlapping with the current interval
            while stack and stack[-1][0] <= start <= stack[-1][1]:

                # Pop the previous interval from the stack
                pStart, pEnd = stack.pop()

                # Merge the previous interval with the current interval
                start, end = min(pStart, start), max(pEnd, end)

            # Add the current interval onto the stack
            stack.append([start, end])

        return stack
