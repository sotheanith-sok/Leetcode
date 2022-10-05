"""
Problem:
    Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

    Note that the root node is at depth 1.

    The adding rule is:

    Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
    cur's original left subtree should be the left subtree of the new left subtree root.
    cur's original right subtree should be the right subtree of the new right subtree root.
    If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
    
    Example1:
    Input: root = [4,2,6,3,1,5], val = 1, depth = 2
    Output: [4,1,1,2,null,null,6,3,1,5]
    
    Example 2:
    Input: root = [4,2,null,3,1], val = 1, depth = 3
    Output: [4,2,null,1,1,3,null,null,1]

Solution:
    DFS through the tree until we reach a desire depth. Then, add new nodes to the left and right child of the current node. Then, backtrack.

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
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:

        # Return a new node connect to the root if depth is 1
        if depth == 1:
            return TreeNode(val, root)

        # DFS through the tree
        def dfs(d, node):

            # If there isn't a node, return
            if not node:
                return

            # If we reach a desire depth
            if d == depth:

                # Add new nodes to the left and right child
                node.left, node.right = (
                    TreeNode(val, node.left),
                    TreeNode(val, None, node.right),
                )
                return

            # Go to the child node
            dfs(d + 1, node.left)
            dfs(d + 1, node.right)

        # Call dfs starting from the root
        dfs(2, root)

        return root
