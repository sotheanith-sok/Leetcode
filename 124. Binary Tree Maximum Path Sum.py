"""
Problem:
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

    The path sum of a path is the sum of the node's values in the path.

    Given the root of a binary tree, return the maximum path sum of any non-empty path.

    Example 1:
    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
    
    Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Solution:
    For any given node, there are two path sum to consider

    1. Path sum composed of the current node as a root
        . left subtree -> node
        . right subtree -> node
        . node
        . left subtree -> node -> right subtree

    2. Path sum composed of the current node as a child
        . left subtree -> node
        . right subtree -> node
        . node

    The first path sum represents a case where a node acts as a root and thus, we only consider it and its subtree when we try to find the maxPathSum. 
    
    The second path sum represents when a node acts as a child node and thus, it will contribute to the maxPathSum calculation of its parent. 

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
    def maxPathSum(self, root: TreeNode) -> int:

        # Initialize the result to store the largest maxPathSum
        res = -inf

        # Calculate pathSum for any given node
        def pathSum(node):
            nonlocal res

            # If there isn't a node, return 0
            if not node:
                return 0

            # Calculate pathSum of the current node's left and right subtrees
            leftSum, rightSum = pathSum(node.left), pathSum(node.right)

            # Calculate the pathSum that current node and one of its subtree will contribute to the maxPathSum calculation of its parent
            pSum = max(node.val, node.val + leftSum, node.val + rightSum)

            # Calculate the maxPathSum where the tree composed of the current node and its subtrees only
            maxPSum = max(
                node.val,
                node.val + leftSum,
                node.val + rightSum,
                node.val + leftSum + rightSum,
            )

            # Save the current maxPathSum into the result if it is larger than the previous maxPathSum
            res = max(res, maxPSum)

            return pSum

        # Start pathSum calculation from the root
        pathSum(root)

        return res
