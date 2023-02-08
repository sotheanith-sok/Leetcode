"""
Problem:
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n
    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
    Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2

Solution:
    Start from 0th node and BFS through the graph until we reach the final node. Return the number of step required to reach such node.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import deque


class Solution:
    def jump(self, nums: list[int]) -> int:

        # Find the number of nodes
        n = len(nums)

        # Initialize the queue and a set to keep track of visited nodes
        queue, visited = deque([0]), set([0])

        # Initialize the number of step
        step = 0

        # Iterate until the queue is empty
        while queue:

            # Find the number of nodes visitable at this step
            k = len(queue)

            # Process all nodes at this step
            for _ in range(k):

                # Pop a node
                node = queue.popleft()

                # If we reached the final node, return the number of step
                if node == n - 1:
                    return step

                # Add all unvisited next nodes into the queue
                for nextNode in range(node + 1, node + nums[node] + 1):

                    if nextNode in visited:
                        continue

                    queue.append(nextNode)
                    visited.add(nextNode)

            # Increment the number of step
            step += 1
