"""
Problem:
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true
    
    Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false
    
    Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Solution:
    DFS through both tree at the same time. Let node1 and node2 be the current node in p and q tree respectively. If there is no node 1 and there is no node2, return True. Else if there is no node1 or there is no node2 or node1!=node2, return False. Lastly, dfs through left children and right children of node1 and node2.  

Complexity:
    Time: O(n) where n is the maximum number of nodes between p and q tree
    Space: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # DFS through both trees
        def dfs(node1, node2):

            # If there is no node1 and there is no node2, return True
            if not node1 and not node2:
                return True

            # If there is no node1 or there is no node2 or node1!=node2, return False
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # Else, check both child of node1 and node2
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(p, q)

