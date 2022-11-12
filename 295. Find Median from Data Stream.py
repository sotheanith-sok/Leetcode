""" 
Problem:
    The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
    
    Example 1:
    Input
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
    Output
    [null, null, null, 1.5, null, 2.0]

    Explanation
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0

Solution:
    Use two heaps to solve this problem. Divide incoming numbers into two partition. Use maxHeap to store all numbers in the left partition and minHeap to store all numbers in the right parition. 
    
    Then, we will add a new number to the lesser(size) of the two heaps and swap their first values until the first value of the minHeap is greater than or equal to the first value of the maxHeap. 

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


import heapq


class MedianFinder:
    def __init__(self):

        # Keep track of if we have odd or even numbers so far
        self.isOdd = False

        # Initialize the two heaps
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:

        # Flip the odd flag
        self.isOdd = not self.isOdd

        # Add the current number to the lesser (size wise) of the two heaps
        if len(self.maxHeap) <= len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # Swap the first values of both heaps if the first value of maxHeap is greater than the first value of the minHeap
        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            maxNum, minNum = -heapq.heappop(self.maxHeap), heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -minNum)
            heapq.heappush(self.minHeap, maxNum)

    def findMedian(self) -> float:

        # Return the first value of the maxHeap if we have odd numbers else return the sum of both first value divided by 2
        return (
            -self.maxHeap[0] if self.isOdd else (-self.maxHeap[0] + self.minHeap[0]) / 2
        )
