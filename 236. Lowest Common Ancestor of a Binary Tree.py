"""
Problem:
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
    
    Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    
    Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

Solution:
    We will dfs through the tree. At each node, we check if it is None, p, or q. If yes, we return such node. Then, there are two cases to consider. If the left and the right subtrees return nodes, we know that the current node is the common ancestor. Else, return the node that isn't None. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):

            # Base case: return a node if it is None, p, or q.
            if node in (None, p, q):
                return node

            # Recursively check the left and right subtree
            left, right = dfs(node.left), dfs(node.right)

            # Return this node if its left and right subtree return nodes. (Each node is in its own tree path)
            # Else, return node that return by either trees that isn't None. (Both nodes lie in the same path)
            return node if left and right else left or right

        return dfs(root)

        

