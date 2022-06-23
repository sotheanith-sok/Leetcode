""" 
Problem:
    Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

    Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.
    Notes:

    You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
    

    Example 1:
    Input
    ["MyStack", "push", "push", "top", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 2, 2, false]

    Explanation
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top(); // return 2
    myStack.pop(); // return 2
    myStack.empty(); // return False

Solution:
    Use deque to solve this problem. The push and empty functions will run in O(1). The top and pop functions will run O(n) because we have to shift the last value from the queue into the front before we can peek or pop from the queue. 
Complexity:
    Time: O(n)
    Space: O(n)
"""
from collections import deque


class MyStack:
    def __init__(self):
        # Intialize the queue
        self.queue = deque()

    def push(self, x: int) -> None:
        # Append the value to the end of the queue.
        self.queue.append(x)

    def pop(self) -> int:

        # Shift the last value from the queue into the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        # Pop and return the first value in the queue.
        return self.queue.popleft()

    def top(self) -> int:

        # Shift the last value from the end of the queue to the front.
        for i in range(len(self.queue)):
            item = self.queue.popleft()

            self.queue.append(item)

            # Return the top of the queue after we shift n times.
            if i == len(self.queue) - 1:
                return item

    def empty(self) -> bool:
        # Check if a queue is empty by its length.
        return len(self.queue) == 0
