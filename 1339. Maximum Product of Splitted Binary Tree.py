""" 
Problem:
    Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

    Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

    Note that you need to maximize the answer before taking the mod and not after taking it.

    Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: 110
    Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
    
    Example 2:
    Input: root = [1,null,2,3,4,null,null,5,6]
    Output: 90
    Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Solution:
    There are two steps to solve this problem. First, we will dfs through the tree and sum up all nodes. For step two, we will dfs through the tree again to find the result by partitioning the tree into two subtrees: a subtree of the current node and its children and a subtree of the remaining nodes. Using the pre computed total sum, we only have to calculate the sum of one subtree to find the sum of both subtrees. Then, we just have to save the largest product of the sum of both subtrees.   

Complexity:
    Time: O(n)
    Space: O(h)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        
        # Initialize the result and the total sum of all nodes 
        res, total = 0, 0 

        # DFS through all nodes to sum up all nodes and find the largest product
        def dfs(node):
            nonlocal res, total

            # If there is no node, return 0
            if not node:
                return 0 

            # Calculate the sum of the current node and its children
            nodesSum = node.val + dfs(node.left) + dfs(node.right)

            # Update the result
            # For the first pass, the result will remain 0 as the calculated product will always be negative because the total is 0 
            res = max(res, nodesSum * (total - nodesSum))

            # Return the sum
            return nodesSum

        # First pass: calculate the sum of all nodes
        total = dfs(root)

        # Second pass: find the largest product if we partition the tree into two subtrees
        dfs(root)

        return res % 1000000007
 