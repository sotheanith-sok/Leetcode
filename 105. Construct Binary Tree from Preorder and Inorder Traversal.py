"""
Problem:
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

    Example 1:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
    
    Example 2:
    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

Solution:
    Find the root of any subtree by getting the first value in the preorder list. Then, split the preorder and inorder lists into the left partition and the right partition. Finally, recursively build a tree from those partition. 

    Preorder: root, left, right
    Inorder: left, root, right

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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        
        def dfs(preorder, inorder):

            # Return none if there is no node
            if not inorder:
                return None

            # Return the node if only one node is given
            if len(inorder) == 1:
                return TreeNode(inorder[0])

            # Find the root of this tree
            root = preorder[0]

            # Find the index of such node in the inorder list
            iRoot = inorder.index(root)

            # Split the inorder list into two parition
            lInorder = inorder[:iRoot]
            rInorder = inorder[iRoot + 1 :]

            # Split the preorder list into two partition
            lPreoder = preorder[1 : iRoot + 1]
            rPreorder = preorder[iRoot + 1 :]

            # Recursively build the rest of the tree
            return TreeNode(root, dfs(lPreoder, lInorder), dfs(rPreorder, rInorder))

        return dfs(preorder, inorder)

