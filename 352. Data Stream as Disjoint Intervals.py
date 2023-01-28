""" 
Problem:
    Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

    Implement the SummaryRanges class:

    SummaryRanges() Initializes the object with an empty stream.
    void addNum(int value) Adds the integer value to the stream.
    int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
    

    Example 1:
    Input
    ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
    [[], [1], [], [3], [], [7], [], [2], [], [6], []]
    Output
    [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

    Explanation
    SummaryRanges summaryRanges = new SummaryRanges();
    summaryRanges.addNum(1);      // arr = [1]
    summaryRanges.getIntervals(); // return [[1, 1]]
    summaryRanges.addNum(3);      // arr = [1, 3]
    summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
    summaryRanges.addNum(7);      // arr = [1, 3, 7]
    summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
    summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
    summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
    summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

Solution:
    Maintain a list of intervals. For each new interval, inside it into the list of intervals. Then, iterate through the list of intervals and merge any connected intervals. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from bisect import insort_left


class SummaryRanges:
    def __init__(self):

        # Initialize the list of intervals
        self.intervals = []

    def addNum(self, value: int) -> None:

        # Insert the current value as its own interval into the list of intervals
        insort_left(self.intervals, [value, value], key=lambda x: x[0])

        # Start merging any connected intervals
        # Find the number of intervals
        n = len(self.intervals)

        # Initialize the two pointers
        left, right = 0, 1

        # Iterate until the second pointer reaches the end of the list of interval
        while right < n:

            # If both pointers point to the same interval, increment the right pointer
            if left == right:
                right += 1
                continue

            # If the left interval is empty, copy the right interval into it
            if self.intervals[left][1] == None:
                self.intervals[left] = self.intervals[right]
                self.intervals[right] = [None, None]
                right += 1
                continue

            # If the left interval isn't connected to the right interval, increment the left pointer
            if self.intervals[left][1] < self.intervals[right][0] - 1:
                left += 1
                continue

            # Else, merge the left and right intervals together and mark the right interval as empty
            self.intervals[left][0], self.intervals[left][1] = min(
                self.intervals[left][0], self.intervals[right][0]
            ), max(self.intervals[left][1], self.intervals[right][1])
            self.intervals[right][0], self.intervals[right][1] = None, None
            right += 1

        # Remove all empty intervals from the list
        while self.intervals and self.intervals[-1][0] == None:
            self.intervals.pop()

    def getIntervals(self) -> list[list[int]]:
        return self.intervals
