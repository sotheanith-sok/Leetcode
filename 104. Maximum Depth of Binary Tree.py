"""
Problem:
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    
    Example 2:
    Input: root = [1,null,2]
    Output: 2

Solution:
    Start from root. Recursively find max depths of the left and the right subtrees and return the largest one. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # Find the max depth of a tree starting from a given node
        def depth(node):

            # If there is no node, return 0
            if not node:
                return 0

            # Else, return the largest max depth between max depths of the left and right subtrees plus 1
            return 1 + max(depth(node.left), depth(node.right))

        return depth(root)
