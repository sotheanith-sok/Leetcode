""" 
Problem:
    Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

    Example 1:
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
    
    Example 2:
    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
    Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Solution:
    DFS through the tree while maintain the range of tree. If there is no node or the current range of the tree isn't between the target range, return 0. Else, add the current node (if it is in the target range) with the sum of the left and right subtrees. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        # Sum up all nodes while maintain a range of such tree
        def dfs(node, cLow, cHigh):

            # If there isn't a node or the current tree is range outside the target range, return 0
            if not node or cHigh < low or cLow > high:
                return 0

            # Else, sum up a given node (if it is in the target range) with the sum from the left and the right subtree
            return (
                node.val * int(low <= node.val <= high)
                + dfs(node.left, cLow, node.val)
                + dfs(node.right, node.val, cHigh)
            )

        return dfs(root, -inf, inf)
