""" 
Problem:
    Given the root of a complete binary tree, return the number of the nodes in the tree.

    According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

    Design an algorithm that runs in less than O(n) time complexity.

    Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: 6
    
    Example 2:
    Input: root = []
    Output: 0
    
    Example 3:
    Input: root = [1]
    Output: 1

Solution:
    Since we are working with complete binary tree, there are full nodes at all levels execept for the last level where nodes are packed to the left. There are two cases to consider:

    1. If the height of left side are equal to the height of the right side, then the tree are perfect. Thus, the number of nodes are 2**height - 1
    Ex: 
          1
      2       2
    3   3   3   3

    left == right == 3 => #s of nodes = 2**3 - 1 = 7 

    2. If the height of both sides are not equal, we have to check each side seperately and sum up the number of nodes. 

    Ex: 
          1
      2       2
    3   3   3   

    left == 3 != right == 2
    Thus, 
    #s of nodes = 1 + count(left) + count(right) 
                = 1 + 2**2 - 1 + (1 + count(right.left) + count(right.right)) 
                = 1 + 2**2 - 1 + (1 + 2**1-1 + 2**0-1) 
                = 1 + 3 + 1 + 1 
                = 6

Complexity:
    Time: O(logn)
    Space: O(logn)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:

        # Find the height of the left side
        def leftHeight(node):
            return 0 if not node else 1 + leftHeight(node.left)

        # Find the height of the right side
        def rightHeight(node):
            return 0 if not node else 1 + rightHeight(node.right)

        # Count the number of nodes in a tree starting from a given node
        def count(node):

            # If there is no node, return 0
            if not node:
                return 0

            # Find height of both sides
            left, right = leftHeight(node), rightHeight(node)

            # If they are equal, we have a perfect binary tree
            if left == right:
                return 2 ** (left) - 1

            # Else, count each subtree seperately
            return 1 + count(node.left) + count(node.right)

        return count(root)
