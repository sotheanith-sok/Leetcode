"""
Problem:
    Given the root of a binary tree, determine if it is a complete binary tree.

    In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

    Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: true
    Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
    
    Example 2:
    Input: root = [1,2,3,4,5,null,7]
    Output: false
    Explanation: The node with value 7 isn't as far left as possible.

Solution:
    BFS through the tree. For each level, if there exists a node after a missing node, a tree must be incomplete. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:

        # Initialize the BFS queue and a flag to keep track if we have found a missing node
        queue, missing = deque([root]), False

        # Iterate until the queue is empty
        while queue:

            # Get the number of nodes at this level
            k = len(queue)

            # Process all nodes at this level
            for _ in range(k):

                # Pop a node from the queue
                node = queue.popleft()

                # If the current node doesn't have a left child, set the missing node flag to true
                if not node.left:
                    missing = True

                # Else, if we detect a missing node previously, we know that the tree must be incomplete
                elif missing:
                    return False

                # Else, add the left child node into the queue
                else:
                    queue.append(node.left)

                # If the current node doesn't have a right child, set the missing node flag to true
                if not node.right:
                    missing = True

                # Else, if we detect a missing node previously, we know that the tree must be incomplete
                elif missing:
                    return False

                # Else, add the left child node into the queue
                else:
                    queue.append(node.right)

        return True
