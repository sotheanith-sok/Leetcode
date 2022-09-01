"""
Problem:
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

    Return the number of good nodes in the binary tree.

    Example 1:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.
    
    Example 2:
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
    
    Example 3:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.

Solution:
    Use dfs to traverse the tree. A node is good if it larger than or equal to the largest node leading up to it. Recursively add all good nodes together.

Complexity:
    Time: O(n)
    Space: O(1)
"""

from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # DFS through the tree
        def dfs(node, maxVal):

            # If there isn't a node, return 0
            if not node:
                return 0

            # If the current node is greater than or equal to the largest previous node, add 1 to the number of good nodes of the left subtree and the right subtree
            return (
                int(node.val >= maxVal)
                + dfs(node.left, max(maxVal, node.val))
                + dfs(node.right, max(maxVal, node.val))
            )

        return dfs(root, -inf)
