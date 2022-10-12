"""
Problem:
    Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

    Example 1:
    Input: root = [5,3,6,2,4,null,7], k = 9
    Output: true
    
    Example 2:
    Input: root = [5,3,6,2,4,null,7], k = 28
    Output: false

Solution:
    Maintain a set of visited node. DFS through the tree. At each node, check if there exists a previously visited node where both nodes sum is equal to the target. If yes, return True. Else, mark the node as visited and visit child of such node.  

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
    def findTarget(self, root: TreeNode, k: int) -> bool:

        # A set of visited nodes
        visited = set()

        # DFS through the tree
        def dfs(node):

            # If there isn't a node, return False
            if not node:
                return False

            # Check if there exists a previously visited node where both node sum to the target
            # If yes, return True
            if k - node.val in visited:
                return True

            # Mark the node as visited
            visited.add(node.val)

            # Check the left and right child of the current node
            # If we found a solution in one of the child node, return True
            if dfs(node.left) or dfs(node.right):
                return True

            # Else, return False
            return False

        return dfs(root)

