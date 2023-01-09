""" 
Problem:
    Given the root of a binary tree, return the preorder traversal of its nodes' values.

    Example 1:
    Input: root = [1,null,2,3]
    Output: [1,2,3]
    
    Example 2:
    Input: root = []
    Output: []
    
    Example 3:
    Input: root = [1]
    Output: [1]

Solution:
    DFS through the tree and add all nodes' values into the result. For any given node, we will add its value into the result before we visit the left and the right subtree. 

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
    def preorderTraversal(self, root: TreeNode) -> list[int]:

        # If there is no root node, return empty list
        if not root:
            return []

        # Initialize the stack and result
        stack, res = [root], []

        # Iterate until the stack is empty
        while stack:

            # Pop a node from the stack
            node = stack.pop()

            # Add such node value into the result
            res.append(node.val)

            # Add the right child first onto the stack if there is one because we want to visit it after visited the left child node
            if node.right:
                stack.append(node.right)

            # Add the left child onto the stack if there is one
            if node.left:
                stack.append(node.left)

        return res
