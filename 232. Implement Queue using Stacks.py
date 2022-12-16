""" 
Problem:
    Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:

    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.
    Notes:

    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
    

    Example 1:
    Input
    ["MyQueue", "push", "push", "peek", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 1, 1, false]

    Explanation
    MyQueue myQueue = new MyQueue();
    myQueue.push(1); // queue is: [1]
    myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek(); // return 1
    myQueue.pop(); // return 1, queue is [2]
    myQueue.empty(); // return false

Solution:
    Use two stacks to solve this problem. The first stack will contain newly added elements and the second stack will contain part of previously added element but in a reverse order. Then, everytime we call pop/peek and the second stack is empty, we will transfer all elements from the first into the second stack.

Complexity:
    Time: O(1)
    Space: O(n)
"""


class MyQueue:
    def __init__(self):
        # Initialize the two stacks
        self.first, self.second = [], []

    def push(self, x: int) -> None:
        # Append an element onto the first stack
        self.first.append(x)

    def pop(self) -> int:
        # If the second stack is empty, transfer all elements from the first stack into it
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())

        # Pop from the second stack
        return self.second.pop()

    def peek(self) -> int:
        # If the second stack is empty, transfer all elements from the first stack into it
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())

        # Peek from the second stack
        return self.second[-1]

    def empty(self) -> bool:
        # Check if both stacks are empty
        return not self.first and not self.second
