"""
Problem:
    You are given a 0-indexed integer array nums and an integer k.

    You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

    You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

    Return the maximum score you can get.

    Example 1:
    Input: nums = [1,-1,-2,4,-7,3], k = 2
    Output: 7
    Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
    
    Example 2:
    Input: nums = [10,-5,-2,4,0,3], k = 3
    Output: 17
    Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
    
    Example 3:
    Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
    Output: 0

Solution:
    Iterate through all numbers. Fore each number, we find the maximum score among k previous number and add the current number score. This will be the maximum score to reach this number from 0. Repeat until we reach the n-1. 

    Solution 1: Solve this problem using top-down dynamic programming approach.
        This solution doesnt work because the count of numbers can be large such that it surpass the recursion depth.
    
    Solution 2: Solve this problem using bottom-up dynamic programming approach.
        This solution avoid the recursion problem but it is still slow due to the need to check k previous numbers.

    Solution 3: Use a monotonically decreasing queue to store the maximum score of k previous numbers.
        To start, we will add the first index and its number into the queue. Then, we will iterate through the remaining numbers. At each iteration, we check the index on top of the queue for it it is more than k away from the current index. If yes, pop such index. Then, we find the maximum score of the current index by summing the current score with the score on top of the queue (Since the queue is monotonically decreasing, the index on top is the largest previous score). Lastly, add the current index and its maximized score into the queue.    


Complexity:
    Time: O(n)
    Space: O(n) or O(1) if we do inplace replacement into nums
"""

from collections import deque

# Top-down dynamic programming approach
class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:

        # Find the size of nums
        n = len(nums)

        # Create the cache and add the last number into it
        cache = {n - 1: nums[n - 1]}

        # Traverse numbers
        def dfs(i):

            # If the current number isn't cached
            if i not in cache:

                # Calculate its score recursively and add it to the cache
                cache[i] = nums[i] + max(
                    [dfs(j) for j in range(i + 1, min(n, i + 1 + k))]
                )

            # Return cached maximum score of the current number
            return cache[i]

        return dfs(0)


# Bottom-up dynamic programming approach
class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:

        # Find the size of nums
        n = len(nums)

        # Initialize the cache and add the first number into it
        cache = {0: nums[0]}

        # Iterate through the remaining numbers
        for i in range(1, n):

            # Calculate the maximum score to reach the current number by find the maximum score to reach k previous numbers and add its max with the current score
            cache[i] = nums[i] + max(
                [cache[j] for j in range(max(0, i - k), i, 1)], default=0
            )

        # Return the cached score of the final numbers
        return cache[n - 1]


# Bottom-up dynamic programming approach with k optimized out using monotonically decreasing queue
class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:

        # Find the size of nums
        n = len(nums)

        # Intialize the cache and add in the first number.
        cache = {0: nums[0]}

        # Add the first index and its number into the queue. It will be the largest maximum score initally since we only have a number
        queue = deque([(0, nums[0])])

        # Iterate through the remaining numbers
        for i in range(1, n):

            # If the largest maximum score is more than k away from the current number, pop it
            while queue and queue[0][0] < i - k:
                queue.popleft()

            # Calculate the maximum score to reach the current number by taking its score and add it with the largest maximum score on top of the queue
            cache[i] = nums[i] + queue[0][1]

            # Pop any maximum score of previous numbers if they are less than the current number maximum score
            while queue and queue[-1][1] < cache[i]:
                queue.pop()

            # Add the current number maximum score into the queue
            queue.append((i, cache[i]))

        return cache[n - 1]

