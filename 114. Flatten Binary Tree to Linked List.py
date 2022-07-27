"""
Problem:
    Given the root of a binary tree, flatten the tree into a "linked list":

    The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    The "linked list" should be in the same order as a pre-order traversal of the binary tree.
    
    Example 1:
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]
    
    Example 2:
    Input: root = []
    Output: []
    
    Example 3:
    Input: root = [0]
    Output: [0]

Solution:
    Traverse through the tree and return the last node. For any given node, find the last node from the left subtree and the last node from the right subtree. There are a few cases to consider. If the last node of the left subtree and the righ subtree are None, we know that the current node is the last node and thus, we return it. If there are last nodes from the left subtree and the right subtree, connect them and return the last node from the right subtree. If there is only one last node from either subtree, move all nodes to the right side and return respective last node. 

Complexity:
    Time: O(n)
    Space: O(1)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):

            # If there is no node, return None
            if not node:
                return None

            # Recursively check for last nodes from the left and the right subtree.
            lastLeft, lastRight = dfs(node.left), dfs(node.right)

            # If there is no last node, return the current node
            if lastLeft == lastRight == None:
                return node

            # If there are last nodes from both subtree
            if lastLeft and lastRight:

                # Connect the last node from the left subtree to the first node in the right subtree
                lastLeft.right = node.right

                # Move all nodes to the right subtree
                node.left, node.right = None, node.left

                # Return the last node from the right subtree
                return lastRight
            
            # If there is only a last node from the left subtree
            if lastLeft:

                # Move all nodes to the right subtree
                node.left, node.right = None, node.left

                # Return the last node from the left subtree
                return lastLeft
            
            # Else, if there is only last node from the right subtree, return the last node from such subtree
            return lastRight

        # Call dfs on the root
        dfs(root)
        
        return root





                

