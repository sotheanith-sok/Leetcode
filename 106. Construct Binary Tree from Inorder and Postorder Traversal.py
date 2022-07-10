"""
Problem:
    Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

    Example 1:
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]
    
    Example 2:
    Input: inorder = [-1], postorder = [-1]
    Output: [-1]

Solution:
    Inorder: left, root, right
    Postorder: left, right, root

    We will recursively build the tree from given inorder and postorder traversal. To start with, we know that the root node will be the last node in the postorder traversal. Then, we find the root node in the inorder traversal. Lastly, we will split both arrays into the left subarray and right subarray based on the root node and recursively build tree from those sub arrays.   
    

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
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        def build(inorder, postorder):

            # Base case
            # If we are given an empty array, we will return None
            if not inorder:
                return None

            # Else if we are given an array of a single value, return that value as a node
            elif len(inorder) == 1:
                return TreeNode(inorder[0])

            # Find the index of the root
            i = inorder.index(postorder[-1])

            # Split both arrays into two. One for the left subtree and one for the right subtree
            return TreeNode(
                inorder[i],
                build(inorder[0:i], postorder[0:i]),
                build(inorder[i + 1 :], postorder[i : len(postorder) - 1]),
            )

        return build(inorder, postorder)

