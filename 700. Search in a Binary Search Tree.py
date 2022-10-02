"""
Problem:
    You are given the root of a binary search tree (BST) and an integer val.

    Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

    Example 1:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]
    
    Example 2:
    Input: root = [4,2,7,1,3], val = 5
    Output: []

Solution:
    Iterate through the tree until you find a node equal to value. If there isn't once, return null.

Complexity:
    Time: O(logn)
    Space:O(1)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        # Initialize the current node
        node = root

        # While there is a current node
        while node:

            # If the current node is equal to the value, end the search
            if node.val == val:
                break

            # Else search the left or right subtree
            node = node.left if node.val > val else node.right

        return node
