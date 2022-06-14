""" 
Problem:
    Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

    An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
    

    Example 1:
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

    Example 2:
    Input: arr = [1,2,3,4,5], k = 4, x = -1
    Output: [1,2,3,4]

Solution:
    Since we know that the given array is sorted, we can conclude that the distances among all numbers are decreasing as we get closer to the target and increasing as we move pass the target. Thus, we can use a queue to store the k least distance to target. Iterate through all numbers in the array. We start by filling the queue with the first k numbers from the array. Afterward, we check if the distance of the first element in the queue to the target is larger than the current number. If yes, we remove the first element in the queue and append the current number onto the end of the queue. Return the queue.   

Complexity:
    Time: O(n)
    Space: O(k)

"""
from collections import deque


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:

        # Use a deque since we are popping from the front.
        queue = deque()

        # Iterate through all numbers in the arr
        for num in arr:

            # Add the first k numbers into the queue.
            if len(queue) < k:
                queue.append(num)
                continue

            # If the distance of the first element is larger than the distance of the current element, pop the first element of the queue and append the current element to queue.
            if abs(queue[0] - x) > abs(num - x):
                queue.popleft()
                queue.append(num)

        return queue
