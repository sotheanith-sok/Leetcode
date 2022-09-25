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
    Use a list of size k to store all numbers. Use two pointers: front and rear that point to the first and last numbers of the queue and two variables to maintain the current and max size of the queue. 

    1. enQueue
        If the current size is equal to the max size, return False. Else, increment the rear pointer and current size by 1. Then, save the number at the rear pointer. Last but not least, move the front pointer to the rear pointer if this is the first number in the queue. 
        
    2. deQueue
        If the current size is 0, return False, Else, increment the front pointer and decrement the current size by 1.

    3. Front
        Return the number at the front pointer

    4. Rear
        Return the number at the rear pointer

    5. isEmpty
        Check if the current size is 0

    6. isFull
        Check if the current size is equal to max size

Complexity:
    Time: O(1)
    Space: O(k)

"""


class MyCircularQueue:
    def __init__(self, k: int):

        # Initialize the list of size k to store all numbers in the queue
        self.list = [0] * k

        # Initialize two variables to keep track of the current and max size of the queue
        self.size, self.max = 0, k

        # Initialize two pointers to keep track of numbers at the front and rear of the queue
        self.front, self.rear = -1, -1

    def enQueue(self, value: int) -> bool:

        # If the queue is full, return False
        if self.size == self.max:
            return False

        # Increment the rear pointer and the current size by 1
        self.rear, self.size = (self.rear + 1) % self.max, self.size + 1

        # Save the number at the rear pointer
        self.list[self.rear] = value

        # If this is the first number in the queue, move the front pointer to the rear pointer
        if self.size == 1:
            self.front = self.rear
        return True

    def deQueue(self) -> bool:

        # If the queue is empty, return False
        if self.size == 0:
            return False

        # Increment the front pointer and decrement the current size by 1
        self.front, self.size = (self.front + 1) % self.max, self.size - 1

        return True

    def Front(self) -> int:

        # Return the number at the front pointer if the queue isn't empty, Else, return -1
        return self.list[self.front] if self.size != 0 else -1

    def Rear(self) -> int:

        # Return the number at the rear pointer if the queue isn't empty. Else, return -1
        return self.list[self.rear] if self.size != 0 else -1

    def isEmpty(self) -> bool:

        # Return true if the current size is 0
        return self.size == 0

    def isFull(self) -> bool:

        # Return true if the current size is equal to the max size
        return self.size == self.max
