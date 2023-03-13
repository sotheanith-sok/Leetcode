"""
Problem:

    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    Example 1:

    Input: root = [1,2,2,3,4,4,3]
    Output: true

    Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

Solution:
    Starting from the root, dfs through the left subtree using inorder traversal (left -> root -> right) and the right subtree using postorder traversal (right-> root-> left) and compare encountered nodes. Return true if all nodes are equal. Else, return Falses

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
    def isSymmetric(self, root: TreeNode) -> bool:

        # Check if two given trees are symmetrical
        def symmetric(node1, node2):

            # If both nodes are null, return True
            if not node1 and not node2:
                return True

            # Else, if both nodes exists, compare encountered nodes where we traverse the left tree using inorder traversal and the right tree using post order traversal
            if (
                (node1 and node2)
                and symmetric(node1.left, node2.right)
                and node1.val == node2.val
                and symmetric(node1.right, node2.left)
            ):
                return True

            # Else, we have detect an asymmetric
            return False

        return symmetric(root.left, root.right)
