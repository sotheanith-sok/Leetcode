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
    Use dfs to solve this problem. At every iteration, we add the node's value to the total and we check if this node is a leaf node and the current total is equal to the targetSum. If yes, we have found a solution and return True. Else, we call a dfs on its children and return True if its children dfs return True. If not, this isn't a right path and thus, we subtract the node's value from the total and return False.  
Complexity:
    Time: O(n**2)
    Space: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        # If we didn't give any tree, return False
        if not root:
            return False

        # Accumulator
        total = 0

        # Perform DFS
        def dfs(node):

            # Add the value of a node to the total
            nonlocal total
            total = total + node.val

            # If we reach a leaf node and the total is equal to targetSum, return True
            if not node.left and not node.right and total == targetSum:
                return True

            # Else, visit its left child if it has one.
            if node and node.left:
                if dfs(node.left):
                    return True

            # Else, visit its right child if it has one.
            if node and node.right:
                if dfs(node.right):
                    return True

            # If we haven't found the solution by this point, this isn't a correct path and thus, we reverse the add.
            total = total - node.val

            # Return false and backtrack.
            return False

        return dfs(root)

