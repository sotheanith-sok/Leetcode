"""
Problem:
    You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

    A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

    The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

    Implement the MyCalendar class:

    MyCalendar() Initializes the calendar object.
    boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
    
    Example 1:
    Input
    ["MyCalendar", "book", "book", "book"]
    [[], [10, 20], [15, 25], [20, 30]]
    Output
    [null, true, false, true]
    Explanation
    MyCalendar myCalendar = new MyCalendar();
    myCalendar.book(10, 20); // return True
    myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
    myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

Solution:
    To check if two ranges are overlapped, we can check if the sum of both ranges fit between the min of starts and the max of ends. i.e. 

    max(a1,b1) - min(a0,b0) >= (a1-a0) + (b1-b0)

    |-----|         (a0,a1) => (0, 5)  => 5
          |-----|   (b0,b1) => (5, 10) => 5
    |-----------|   max(a1,b1) - min(a0,b0) => 10-0 =>  10 => No overlap

    |-----|         (a0,a1) => (0, 5)  => 5
        |-----|     (b0,b1) => (4, 9)  => 5
    |---------|     max(a1,b1) - min(a0,b0) => 9-0 => 9 => Overlapped
    
    In order to improve the speed of searching through previous bookings, we will store all bookings as a node in a binary tree. Then, we can recursively add a node as long as it doesn't overlap with any previous nodes and return True. Else, we just return False. 

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


# Defintion of a node
class Node:
    def __init__(self, start, end) -> None:

        # The start and end of this node range
        self.start, self.end = start, end

        # Pointers to the left and right child
        self.left, self.right = None, None

class MyCalendar:
    def __init__(self):

        # Initialize the root node to None
        self.roots = None

    def book(self, start: int, end: int) -> bool:

        # If there isn't a root node, add the current booking as the root node
        if not self.roots:
            self.roots = Node(start, end)
            return True

        # Else, recursively add a booking into the tree
        def add(node, start, end):

            # If the range of the current booking is less than the range of the current node
            if start < end <= node.start < node.end:

                # Check if the current node has a left child.
                if node.left:
                    
                    # If yes, move to such child
                    return add(node.left, start, end)

                # Else, add the current booking as the left child of the current node
                else:
                    node.left = Node(start, end)
                    return True

            # Else, if the range of the current booking is greater than the range of the current node
            elif node.start < node.end <= start < end:

                # Check if the current node has a right child.
                if node.right:

                    # If yes, move to such child
                    return add(node.right, start, end)

                # Else, add the current booking as the right child of the current node
                else:
                    node.right = Node(start, end)
                    return True
            
            # Else, there is a overlap
            return False

        return add(self.roots, start, end)

