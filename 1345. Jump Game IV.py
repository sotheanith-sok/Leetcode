"""
Problem:
    Given an array of integers arr, you are initially positioned at the first index of the array.

    In one step you can jump from index i to index:

    i + 1 where: i + 1 < arr.length.
    i - 1 where: i - 1 >= 0.
    j where: arr[i] == arr[j] and i != j.
    Return the minimum number of steps to reach the last index of the array.

    Notice that you can not jump outside of the array at any time.

    Example 1:
    Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
    Output: 3
    Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
    
    Example 2:
    Input: arr = [7]
    Output: 0
    Explanation: Start index is the last index. You do not need to jump.
    
    Example 3:
    Input: arr = [7,6,9,6,9,6,9,7]
    Output: 1
    Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Solution:
    Start by building an adjacency list mapping node's value to a list of nodes contain such values. Then, starting from 0th node, find the shortest path to reach the n-1th node using BFS. For some arbitrary ith node, next visitable nodes are i-1th node, i+1th node, and all non-visited nodes that have the same values. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:

        # Find the number of nodes
        n = len(arr)

        # Build an adjacency list mapping each value to a list of nodes contain such value
        adj = defaultdict(list)
        for node, num in enumerate(arr):
            adj[num].append(node)

        # Start BFS to find the shortest path from 0th node to n-1th node
        # Initialize a queue to store next visitable node, a set to keep track of visited nodes, and a step counter
        queue, visited, step = deque([0]), set([0]), 0

        # Iterate until the queue is empty
        while queue:

            # Find the number of visitable nodes at this step
            k = len(queue)

            # Visit all nodes
            for _ in range(k):

                # Pop a node from the queue
                node, num = queue[0], arr[queue.popleft()]

                # If we reach the n-1th node, return the step
                if node == n - 1:
                    return step

                # Else, add all next visitable nodes into the queue
                for nextNode in [node + 1, node - 1] + (
                    adj.pop(num) if num in adj else []
                ):

                    if not (0 <= nextNode < n) or nextNode in visited:
                        continue

                    queue.append(nextNode)
                    visited.add(nextNode)

            # Increment the step count
            step += 1
