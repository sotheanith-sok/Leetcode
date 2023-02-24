"""
Problem:
    You are given an array nums of n positive integers.

    You can perform two types of operations on any element of the array any number of times:

    If the element is even, divide it by 2.
    For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
    If the element is odd, multiply it by 2.
    For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
    The deviation of the array is the maximum difference between any two elements in the array.

    Return the minimum deviation the array can have after performing some number of operations.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: 1
    Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
    
    Example 2:
    Input: nums = [4,1,5,20,3]
    Output: 3
    Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
    
    Example 3:
    Input: nums = [2,10,8]
    Output: 3

Solution:
    A number can be reduce as long as it is an even number and increase as long as it is a odd number. Thus, we will attempt to reduce the deviation from both directions and return the minimum deviation.

    Start by attempting to reduce the deviation from the left by continue to multiply the smallest number by 2 as long as it is a odd number. Use a min heap to quickly find the smallest number and a variable to keep track of the largest number. 

    Then, we will attempt to reduce the deviation from the right by continue to divide the largest number by 2 as long as it is an even number. Use a max heap to quickly find the largest number and a variable to store the smallest number. 


Complexity:
    Time: O(nlogn)
    Space: O(n)
"""

import heapq


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:

        # Attempt the left side reduction of the deviation
        # Initialize the min heap and a variable to store the largest number
        minHeap, maxNum = nums, max(nums)
        heapq.heapify(minHeap)

        # Store the initial deviation
        res = abs(minHeap[0] - maxNum)

        # Continue to perform the left side reduction by multiplying the smallest number by 2 as long as it is a odd number
        while minHeap[0] % 2 != 0:
            maxNum = max(maxNum, minHeap[0] * 2)
            heapq.heapreplace(minHeap, minHeap[0] * 2)
            res = min(res, abs(minHeap[0] - maxNum))


        # Attempt the right side reduction of the deviation
        # Initialize the max heap  and a variable to store the smallest number
        maxHeap, minNum = [-num for num in minHeap], min(minHeap)
        heapq.heapify(maxHeap)

        # Store the initial deviation
        res = min(res, abs(-maxHeap[0] - minNum))

        # Continue to perform the right side reduction by dividing the largest number by 2 as long as it is an even number
        while maxHeap[0] % 2 == 0:
            minNum = min(minNum, -maxHeap[0] // 2)
            heapq.heapreplace(maxHeap, maxHeap[0] // 2)
            res = min(res, abs(-maxHeap[0] - minNum))

        return res
