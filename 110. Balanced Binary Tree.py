"""
Problem:
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

    Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

    Example 3:
    Input: root = []
    Output: true

Solution:
    DFS through the tree. At each node, check if the depth of the left subtree are at most 1 difference than the depth of the right subtree. If not, save False as the result. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        # Initialize the result to True
        res = True

        # DFS through the tree
        def dfs(node, i):
            nonlocal res

            # If there isn't a node, return previous depth
            if not node:
                return i - 1

            # Check depths of the left and right subtrees
            left, right = dfs(node.left, i + 1), dfs(node.right, i + 1)

            # If they are more than 1 difference, save False to the result
            if abs(right - left) > 1:
                res = False

            # Return the max depth of both subtrees
            return max(left, right)

        dfs(root, 0)

        return res
