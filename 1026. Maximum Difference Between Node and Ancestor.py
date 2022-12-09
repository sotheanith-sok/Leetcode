""" 
Problem:
    Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

    A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

    Example 1:
    Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
    Output: 7
    Explanation: We have various ancestor-node differences, some of which are given below :
    |8 - 3| = 5
    |3 - 7| = 4
    |8 - 1| = 7
    |10 - 13| = 3
    Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
    
    Example 2:
    Input: root = [1,null,2,null,0,3]
    Output: 3

Solution:
    Traverse the tree using DFS. We can find the maximum difference between a node and its ancestor nodes by maintaining a minimum and a maximum values of such ancestor nodes. Then, we continue to check the left and right subtrees and return the largest difference. 

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
    def maxAncestorDiff(self, root: TreeNode) -> int:

        # Find the maximum difference between a node and its ancestors
        def dfs(node, low, high):

            # If there is no node, return 0
            if not node:
                return 0

            # Find the max difference among:
            # 1. Current node vs the minimum node among its ancestors
            # 2. Current node vs the maximum node among its ancestors
            # 3. Maximum difference from the left subtree
            # 4 Maximum difference from the right subtree
            return max(
                abs(node.val - low),
                abs(node.val - high),
                dfs(node.left, min(node.val, low), max(node.val, high)),
                dfs(node.right, min(node.val, low), max(node.val, high)),
            )

        return dfs(root, root.val, root.val)
