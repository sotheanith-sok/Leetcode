"""
Problem:
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Example 1:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.
    
    Example 2:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
    
    Example 3:
    Input: root = [2,1], p = 2, q = 1
    Output: 2

Solution:
    Traverse through the tree using dfs. For each node, if it is between p and q, it is a common ancestor of those nodes and thus, we return it. Else, if the current node is less than p and q, search the right subtree. Else, search the left subtree.  

Complexity:
    Time: O(logn)
    Space: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        # Find the small and large node of p and q
        small, large = (p.val, q.val) if p.val < q.val else (q.val, p.val)

        # DFS through the tree
        def dfs(node):

            # If the current node is between p and q, return such node
            # = is used to include the case where p is a child of q or q is a child of p
            if small <= node.val <= large:
                return node

            # Else if the current node is less than p and q, search the right subtree
            elif node.val < small < large:
                return dfs(node.right)

            # Else, search the left subtree
            else:
                return dfs(node.left)

        return dfs(root)

