"""
Problem:
    Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
    

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [3.00000,14.50000,11.00000]
    Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
    Hence return [3, 14.5, 11].
    
    Example 2:
    Input: root = [3,9,20,15,7]
    Output: [3.00000,14.50000,11.00000]

Solution:
    Use bfs to traverse all nodes at each level. For each level, sum up all nodes and average the result based on the number of nodes.

Complexity:
    Time: O(n)
    Space: O(n)
"""


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:

        # Initialize the result and queue
        res, queue = [], deque([root])

        # Iterate until the queue is empty
        while queue:

            # Find the number of nodes at this level
            n = len(queue)

            # Initialize a variable to accumulate all nodes values
            acc = 0

            # Iterate through all nodes
            for _ in range(n):

                # Pop a node
                node = queue.popleft()

                # Add the node value to the accumulator
                acc += node.val

                # If there is a left child, add such node to the queue
                if node.left:
                    queue.append(node.left)

                # If there is a right child, add such node to the queue
                if node.right:
                    queue.append(node.right)

            # Average the accumulator by the number of nodes and append the average to the result
            res.append(acc / n)

        return res
