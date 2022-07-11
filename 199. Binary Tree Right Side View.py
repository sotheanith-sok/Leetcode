"""
Problem:
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    Example 1:

    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
    
    Example 2:
    Input: root = [1,null,3]
    Output: [1,3]

    Example 3:
    Input: root = []
    Output: []

Solution:
    Use breadth-first search to traverse the tree. Append the last node at each level to the result. 

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
    def rightSideView(self, root: TreeNode) -> list[int]:

        # Initialize the queue and the visit set
        queue, visit = deque(), set()

        # Add the first node into the queue and the set if it exists
        if root:
            queue.append(root)
            visit.add(root)

        # Initialize the result
        res = []

        # Iterate until the queue is empty
        while queue:

            # Find the number of nodes at this level
            n = len(queue)

            # Iterate through all nodes at this level
            for i in range(n):

                # Pop a node
                node = queue.popleft()

                # If we reach the last node, add its value to the result
                if i == n - 1:
                    res.append(node.val)

                # If there is a left child, add it to the queue and mark it as visited
                if node.left and node.left not in visit:
                    queue.append(node.left)
                    visit.add(node.left)

                # If there is a right child, add it to the queue and mark it as visited
                if node.right and node.right not in visit:
                    queue.append(node.right)
                    visit.add(node.right)

        return res

