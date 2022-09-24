"""
Problem:
    Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

    A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

    Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]
    Explanation: There are two paths whose sum equals targetSum:
    5 + 4 + 11 + 2 = 22
    5 + 8 + 4 + 5 = 22
    
    Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: []
    
    Example 3:
    Input: root = [1,2], targetSum = 0
    Output: []

Solution:
    DFS through the tree and keep track of nodes from the root to a leaf. Once we reach a leaf, check if the sum of all nodes equal to the target. If yes, add such path to the result. Then, backtrack.

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
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:

        # DFS through the tree
        def dfs(node, s, path):

            # If there isn't a node, return empty list
            if not node:
                return []

            # Add current node into the sum and path
            s, path = s + node.val, path + [node.val]

            # If there is no child node
            if not node.left and not node.right:

                # Return the path if sum is equal to target sum else return empty list
                return [path] if s == targetSum else []

            # Else, go to child nodes
            return dfs(node.left, s, path) + dfs(node.right, s, path)

        return dfs(root, 0, [])

