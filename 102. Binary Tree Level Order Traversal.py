"""
Problem:
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    
    Example 2:
    Input: root = [1]
    Output: [[1]]
    
    Example 3:
    Input: root = []
    Output: []

Solution:
    Use BFS to traverse the tree level by level. Add node's val as we go through each level. 

Complexity:
    Time: O(n)
    Space: O(n)
"""
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:

        # Intialize the queue and a visited set
        queue = deque()
        visited = set()

        res = []

        # If there is a root node, add it to the queue
        if root:
            queue.append(root)
            visited.add(root)

        # Iterate until the queue is empty
        while queue:

            # Get the number of node at this level
            i = len(queue)

            # Create a list to store all values of nodes at this level
            partialRes = []

            # Iterate through all nodes at this level
            for _ in range(i):

                # Pop a node
                node = queue.popleft()

                # Add its value to the partial list
                partialRes.append(node.val)

                # Add its left child to the queue if it exists
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)

                # Add its right child to the queue if its exists
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)

            # Add the partial result to the result
            res.append(partialRes)

        return res
