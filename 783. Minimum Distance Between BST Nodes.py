"""
Problem:
    Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

    Example 1:
    Input: root = [4,2,6,1,3]
    Output: 1
    
    Example 2:
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

Solution:
    We can find the minimum difference between any two numbers in a sorted list of numbers by comparing  every pair of neighboring numbers. The same principle can be applied here since we have a binary search tree using inorder traversal (left -> current -> right). 

    DFS through the tree. For each node, visit its left child if there is one. Then, calculate the difference between the current node and the previously visited node and save their difference into the result. Then, visit the right child if there is one.

Complexity:
    Time: O(n)
    Space: O(n)
"""


from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        # Initialize the previously visited node and result
        pNode, res = TreeNode(inf), inf

        # DFS through the binary search tree
        def dfs(node):
            nonlocal pNode, res

            # If there is a left child, visit it
            if node.left:
                dfs(node.left)

            # Then, calculate the difference between the current node and the previously visited node
            res = min(res, abs(pNode.val - node.val))

            # Update the previously visited node
            pNode = node

            # Visit the right child if there is one
            if node.right:
                dfs(node.right)

        # DFS starting from the root
        dfs(root)

        return res
