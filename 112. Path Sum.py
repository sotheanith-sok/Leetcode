""" 
Problem:
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

    A leaf is a node with no children.

    Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Explanation: The root-to-leaf path with the target sum is shown.

    Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: false
    Explanation: There two root-to-leaf paths in the tree:
    (1 --> 2): The sum is 3.
    (1 --> 3): The sum is 4.
    There is no root-to-leaf path with sum = 5.

    Example 3:
    Input: root = [], targetSum = 0
    Output: false
    Explanation: Since the tree is empty, there are no root-to-leaf paths.

Solution:
    Use dfs to traverse the graph. Add values of all nodes in a path together. When, we reach a leaf node, check if the current sum is equal to the target sum. If yes, return True. Else, backtrack and search other paths.  
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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        # DFS to sum up all node values along a path
        def dfs(node, previousSum):

            # If there isn't a node, return False
            if not node:
                return False

            # Calculate the current sum
            currentSum = node.val + previousSum

            # If we reach a leaf node, check if the current sum equal to the target sum
            if not node.left and not node.right:
                return True if targetSum == currentSum else False

            # Check all paths to see if there is a current sum equal to the target sum. If yes, return True  and end the search
            if (node.left and dfs(node.left, currentSum)) or (
                node.right and dfs(node.right, currentSum)
            ):
                return True

            # Return False if we can't find one
            return False

        return dfs(root, 0)
