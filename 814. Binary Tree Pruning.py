"""
Problem:
    Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

    A subtree of a node node is node plus every node that is a descendant of node.

    Example 1:
    Input: root = [1,null,0,0,1]
    Output: [1,null,0,null,1]
    Explanation: 
    Only the red nodes satisfy the property "every subtree not containing a 1".
    The diagram on the right represents the answer.
    
    Example 2:
    Input: root = [1,0,1,0,0,0,1]
    Output: [1,null,1,null,1]
    
    Example 3:
    Input: root = [1,1,0,1,1,0,1,0]
    Output: [1,1,0,1,1,null,1]

Solution:
    Use dfs to traverse the tree. A dfs on a node will return such node if there exists a one in the subtree starting from such node. Ie node's value == 1 or there is a left subtree or there is a right subtree. 

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
    def pruneTree(self, root: TreeNode) -> TreeNode:

        # Use DFS to traverse the tree
        def dfs(node):

            # If there is no node, return None
            if not node:
                return None

            # Check for 1 in the left and right subtrees. DFS will return None if there isn't a 1 in such subtree.
            node.left, node.right = dfs(node.left), dfs(node.right)

            # Return the node is its value is 1 or if there is a subtree
            return node if (node.val == 1 or node.left or node.right) else None

        return dfs(root)

