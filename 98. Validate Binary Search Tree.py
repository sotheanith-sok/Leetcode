"""
Problem:
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    

    Example 1:
    Input: root = [2,1,3]
    Output: true
    
    Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Solution:
    Dfs through all nodes. For each node, check if its value is between a valid range. If a node is the left child, its range is between the min of its parent and its parent value. If a node is the right child, its range is between its parent value and the max range of its parent. 

Complexity:
    Time: O(n)
    Space: O(1)
"""

# Definition for a binary tree node.
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # Dfs through all nodes
        def dfs(node, min, max):

            return (
                (min < node.val < max) # Check if the current node value is valid
                and (not node.left or dfs(node.left, min, node.val)) # Check if its left subtree contains valid nodes
                and (not node.right or dfs(node.right, node.val, max)) # Check if its right subtree contains valid nodes
            )

        return dfs(root, -inf, inf)
