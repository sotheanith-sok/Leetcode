"""
Problem:
    Given the root of a binary tree, invert the tree, and return its root.

    Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    
    Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]
    Example 3:
    Input: root = []
    Output: []

Solution:
    DFS through the tree. At each node, invert its left subtree and its right subtree. Then, swap the head of the two subtrees.  

Complexity:
    Time: O(n)
    Space: O(1)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):

            # If there is a node
            if node:

                # Invert the left subtree and the right subtree
                left, right = invert(node.left), invert(node.right)

                # Swap the head of the left subtree with the head of the right subtree
                node.left, node.right = right, left

            return node

        return invert(root)
