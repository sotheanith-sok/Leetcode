"""
Problem:
    A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

    You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

    Implement the MyCalendarThree class:

    MyCalendarThree() Initializes the object.
    int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
    
    Example 1:
    Input
    ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
    [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    Output
    [null, 1, 1, 2, 3, 3, 3]

    Explanation
    MyCalendarThree myCalendarThree = new MyCalendarThree();
    myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
    myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
    myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
    myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
    myCalendarThree.book(5, 10); // return 3
    myCalendarThree.book(25, 55); // return 3

Solution:
    Solve this problem with bruteforce. Since python doesn't have sorted map, we will use a list to maintain timelines and dict to store what changes occured at each time (+1 for start and -1 for end). Everytime, there is a new booking, count changes and return the largest changes. 

Complexity:
    Time: O(n**2) where O(n) is the number of booking and O(n) for insertion into sorted list
    Space: O(n)
"""

from bisect import insort
from collections import defaultdict


class MyCalendarThree:
    def __init__(self):

        # A sorted list of time step
        self.timelines = []

        # A dict to store changes occured at each time step
        self.changes = defaultdict(int)

    def book(self, start: int, end: int) -> int:

        # Insert start and end time into the timeline
        if start not in self.changes:
            insort(self.timelines, start)

        if end not in self.changes:
            insort(self.timelines, end)

        # Update changes occured at both times
        self.changes[start], self.changes[end] = (
            self.changes[start] + 1,
            self.changes[end] - 1,
        )

        # Iterate through all time step and find the maximum overlap
        res, count = 0, 0
        for event in self.timelines:
            count += self.changes[event]
            res = max(res, count)

        return res

