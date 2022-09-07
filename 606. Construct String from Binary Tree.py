"""
Problem:
    Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

    Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

    Example 1:
    Input: root = [1,2,3,4]
    Output: "1(2(4))(3)"
    Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
    
    Example 2:
    Input: root = [1,2,3,null,4]
    Output: "1(2()(4))(3)"
    Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

Solution:
    Use dfs to traverse the tree. If there is no node, returm empty string. For each node, call dfs on its left child if the node has at least one child and call dfs on its right child if the node has the right child.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# String Concatenation
class Solution:
    def tree2str(self, root: TreeNode) -> str:

        # DFS through the tree
        def dfs(node):

            # If there is no node, return empty string
            if not node:
                return ""

            # Return node value concatenate with strings return from its left child and right child
            return (
                str(node.val)
                + (("(" + dfs(node.left) + ")") if node.left or node.right else "")
                + (("(" + dfs(node.right) + ")") if node.right else "")
            )

        return dfs(root)


# List Join
class Solution:
    def tree2str(self, root: TreeNode) -> str:

        # Initialize the result
        res = []

        # DFS through the tree
        def dfs(node):

            # If there is no node, do nothing
            if not node:
                return

            # Add current node value to the result
            res.append(str(node.val))

            # If the current node has a child, go to the left child
            if node.left or node.right:
                res.append("(")
                dfs(node.left)
                res.append(")")

            # If the current node has a right child, go to such child
            if node.right:
                res.append("(")
                dfs(node.right)
                res.append(")")

        # Call dfs starting from the root
        dfs(root)

        # Joins all characters into a string
        return "".join(res)
