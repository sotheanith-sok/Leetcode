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

        # Base case
        if not root:
            return []

        # Intialize the stack, res, and visit
        stack, res, visit = [], [], set()

        # Iterative DFS
        # Add the root to the stack
        stack.append(root)

        # Iterate until the stack is empty
        while stack:

            # Add all subsequence left children to the stack. 
            while stack[-1].left and stack[-1].left not in visit:
                stack.append(stack[-1].left)

            # Pop the node for the stack, mark it as visited, and save its value in the result list.
            node = stack.pop()
            visit.add(node)
            res.append(node.val)

            # If such node has a right child, add it to the stack.
            if node.right and node.right not in visit:
                stack.append(node.right)

        return res


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        # Base case
        if not root:
            return []

        # Initialize res and visit
        res, visit = [], set()

        # Recurisve dfs
        def dfs(node):

            # Process all of the left children nodes first
            while node.left and node.left not in visit:
                dfs(node.left)

            # Mark a node as visited and save its value.
            visit.add(node)
            res.append(node.val)

            # If the node has a right child, process that one. 
            if node.right and node.right not in visit:
                dfs(node.right)

        dfs(root)
        return res