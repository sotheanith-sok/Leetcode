""" 
Problem:
    Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

    As a reminder, a binary search tree is a tree that satisfies these constraints:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    
    Example 1:
    Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
    
    Example 2:
    Input: root = [0,null,1]
    Output: [1,null,1]

Solution (Depth First Search):
    Performe a depth first search on the tree and for every given node, sum up the right subtree, update the root, and sum up the left subtree. Then, return the total from the left subtree. 

Complexity:
    Time: O(n)
    Space: O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dps(node, total):

            # If there is no node, return the total
            if not node:
                return total

            # If there is a right node, perform dps on it and return the sum
            if node.right:
                total = dps(node.right, total)

            # Add the sum from the right subtree with the current node
            node.val = total + node.val
            total = node.val

            # Sum up the left subtree
            if node.left:
                total = dps(node.left, total)

            # Return the sum from the left subtree
            return total

        dps(root, 0)
        return root
