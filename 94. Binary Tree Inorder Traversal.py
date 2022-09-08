"""
Problem:
    Given the root of a binary tree, return the inorder traversal of its nodes' values.

    Example 1:


    Input: root = [1,null,2,3]
    Output: [1,3,2]
    Example 2:

    Input: root = []
    Output: []
    Example 3:

    Input: root = [1]
    Output: [1]

Solution:
    Since we want an inorder traversal (left -> root -> right), we will performs a dfs. For a given node, we will add its left child and subsequence left children onto the stack. Then, we pop a node and save its value into a result list. Then, if such node has right child, we add it to the stack and repeat the process. 

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
    def inorderTraversal(self, root: TreeNode) -> list[int]:

        # If there is no root node given, return empty list
        if not root:
            return []

        # Initialize the stack, visited set, and a result list
        stack, visited, res = [root], set([root]), []

        # Iterate until the stack is empty
        while stack:

            # If the current node at the top of the stack has a left child and we haven't visited such child yet, add it to the stack
            while stack[-1].left and stack[-1].left not in visited:
                visited.add(stack[-1].left)
                stack.append(stack[-1].left)

            # Pop a node and add its value to the result
            node = stack.pop()
            res.append(node.val)

            # If the current node has a right child and we haven't visit such child yet, add such child to the stack
            if node.right and node.right not in visited:
                visited.add(node.right)
                stack.append(node.right)

        return res

