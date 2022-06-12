""" 
Problem:
    Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

    One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

    Implementation the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.
    You must solve the problem without using the built-in queue data structure in your programming language. 

    Example 1:
    Input
    ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
    [null, true, true, true, false, 3, true, true, true, 4]
    Explanation
    MyCircularQueue myCircularQueue = new MyCircularQueue(3);
    myCircularQueue.enQueue(1); // return True
    myCircularQueue.enQueue(2); // return True
    myCircularQueue.enQueue(3); // return True
    myCircularQueue.enQueue(4); // return False
    myCircularQueue.Rear();     // return 3
    myCircularQueue.isFull();   // return True
    myCircularQueue.deQueue();  // return True
    myCircularQueue.enQueue(4); // return True
    myCircularQueue.Rear();     // return 4

Solution:
    You can use either a list or a linked nodes for solving this problem. The general idea is that you have two pointers where one is pointing to the start of the queue and another one is pointing to the end of the queue. If you use a list, None can be used to indicate empty spots and the max size is enforced by the size of the list. If you use a linked nodes, you have to keep track of the current count and the max size. enQueue will increment the start pointer and deQueue will decrement the end pointer.   

Complexity:
    Time: O(1)
    Space: O(n)

"""

# List Solution
class MyCircularQueue:
    def __init__(self, k: int):
        # Initialize varaibles and a list of none
        self.max, self.list, self.start, self.end = k, [None] * k, 0, 0

    def enQueue(self, value: int) -> bool:

        # If the end pointer is pointing to an empty slot, add the value there and move the end pointer to the next slot.
        if self.list[self.end] == None:
            self.list[self.end] = value
            self.end = (self.end + 1) % self.max
            return True
        return False

    def deQueue(self) -> bool:

        # If the start pointer is pointer to a non empty slot, set it to empty and move the start pointer to the next slot. 
        if self.list[self.start] != None:
            self.list[self.start] = None
            self.start = (self.start + 1) % self.max
            return True
        return False

    def Front(self) -> int:
        # If there is a value at the start pointer, return it
        return self.list[self.start] if self.list[self.start] != None else -1

    def Rear(self) -> int:
        # If there is a value at the end pointer, return it
        return self.list[self.end - 1] if self.list[self.end - 1] != None else -1

    def isEmpty(self) -> bool:
        # If the start and the end pointers are pointing to empty slots, the list is empty
        return self.list[self.start] == self.list[self.end] == None

    def isFull(self) -> bool:
        # If the start and the end pointers are pointing to non empty slots, the list is full
        return self.list[self.start] != None and self.list[self.end] != None


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):

        self.count, self.max, self.start, self.end = 0,k, None, None

    def enQueue(self, value: int) -> bool:
        # If the count hasn't reach the max
        if self.count < self.max:

            # If the queue is empty, set the start and the end pointers to a new node. 
            if self.count == 0:
                self.end = Node(value)
                self.start = self.end

            # Else, add a new node to the end of the link nodes. 
            else:
                self.end.next = Node(value)
                self.end = self.end.next

            # Increment the count
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:

        # If there is at least one node in the linked nodes,
        if self.count > 0:

            # Set the start pointer to the next node
            self.start = self.start.next

            # Decrement the count
            self.count -= 1

            # If the count reach 0, set the end pointer to None. 
            self.end = None if self.count == 0 else self.end
            return True

        return False

    def Front(self) -> int:
        # If there is a node at the start pointer, return its value.
        return self.start.val if self.start else -1

    def Rear(self) -> int:
        # If there is a  node at the end pointer, return its value.
        return self.end.val if self.end else -1

    def isEmpty(self) -> bool:
        # Queue is empty when the count is 0
        return self.count == 0

    def isFull(self) -> bool:
        # Queue is full when the count reaches max. 
        return self.count == self.max

