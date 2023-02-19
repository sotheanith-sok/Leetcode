"""
Problem:
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

    Example 2:
    Input: root = [1]
    Output: [[1]]
    
    Example 3:
    Input: root = []
    Output: []

Solution:
    BFS through the tree and append a list of values at each level into the result. Reverse all lists of values at odd level.  

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
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:

        # If there is no root node, return empty result
        if not root:
            return []

        # Initialize the result and the queue and level for BFS
        res, queue, level = [], deque([root]), 0

        # Iterate until the queue is empty
        while queue:

            # Find the number of nodes at this level and initialize the partial result
            k, pRes = len(queue), []

            # Process all nodes at this level
            for _ in range(k):

                # Pop a node from the queue
                node = queue.popleft()

                # Append the node's value into the partial result
                pRes.append(node.val)

                # Add the current node left child into the queue if there is one
                if node.left:
                    queue.append(node.left)

                # Add the current ndoe right child into the queue if there is one
                if node.right:
                    queue.append(node.right)

            # Reverse the partial result if the current level is odd and add it into the result
            res.append(pRes if level % 2 == 0 else pRes[::-1])

            # Increment the level
            level += 1

        return res
