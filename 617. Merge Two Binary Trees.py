"""
Problem:
    You are given two binary trees root1 and root2.

    Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

    Return the merged tree.

    Note: The merging process must start from the root nodes of both trees.

    Example 1:
    Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
    Output: [3,4,5,5,4,null,7]
    
    Example 2:
    Input: root1 = [1], root2 = [1,2]
    Output: [2,2]

Solution: 
    DFS through both trees at the same. Let node1 and node2 be the current node of tree1 and tree2 respetively. 
    
    If there is only one node, return such node as there is no merging necessary 
    
    If there is node1 and node2, add values of node2 onto node1 and merge the left and right subtrees and set both subtrees as the child of node1. Lastly, return node1.

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
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        # DFS through both trees and merge their nodes
        def merge(node1, node2):

            # If there is only one node, return such node
            if not node1 or not node2:
                return node1 if node1 else node2

            # Else, merge node2 with node1
            # Add values of node2 onto node1
            node1.val += node2.val

            # Merge both subtrees and set them as the child of node1
            node1.left, node1.right = (
                merge(node1.left, node2.left),
                merge(node1.right, node2.right),
            )

            # Return node1
            return node1

        return merge(root1, root2)
