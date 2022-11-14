""" 
Problem:
    You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    Return the max sliding window.

    Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation: 
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7
    
    Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Solution:
    Use monotonically decreasing queue to solve this problem. Start by adding the first k numbers into the queue. The first value in front of the queue will be the max of the first sliding window. Then, iterate through remaining numbers using two pointers. If the number at the left pointer is equal to the number in front of the queue, such number is no longer valid and thus, we remove it. Then, continue to remove number from the end of the queue until it is no longer greater than the number at the right pointer. Next, append such number into the queue and save the first number of the queue into the result. 

Complexity:
    Time: O(n)
    Space: O(k)
"""
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        # Find length of numbers
        n = len(nums)

        # Initialize the monotonically decreasing queue
        mono = deque()

        # Add the first k numbers into the queue
        for r in range(k):
            while mono and mono[-1] < nums[r]:
                mono.pop()
            mono.append(nums[r])

        # Initialize the result
        res = [mono[0]]

        # Initialize the left pointer
        l = 0

        # Iterate through remaining numbers using the right pointer
        for r in range(k, n):

            # Remove the number at the front of queue if it is no longer valid
            if nums[l] == mono[0]:
                mono.popleft()

            # Remove all numbers from the end of the queue that is less than the current number
            while mono and mono[-1] < nums[r]:
                mono.pop()

            # Add the current number into the queue
            mono.append(nums[r])

            # Add the max for this sliding window into the result
            res.append(mono[0])

            # Increment the left pointer
            l += 1

        return res
