"""
Problem:
    Given the root of a binary tree, return all duplicate subtrees.

    For each kind of duplicate subtrees, you only need to return the root node of any one of them.

    Two trees are duplicate if they have the same structure with the same node values.

    Example 1:
    Input: root = [1,2,3,4,null,2,4,null,null,4]
    Output: [[2,4],[4]]
    
    Example 2:
    Input: root = [2,1,1]
    Output: [[1]]
    
    Example 3:
    Input: root = [2,2,2,3,null,3,null]
    Output: [[2,3],[3]]

Solution:
    DFS through the tree and summarize each subtree structure including the root node and its two subtrees. Return a node from each subtree if we observe such subtree structure occurred more than once. 

    Subtree structure can be represented with nested tuples which will take linear time to summarize such structure or with integers mapping which will take constant time to summarize the structure.

    Ex: Let root = [1,2,3,4,null,2,4,null,null,4] and tuple structure = (node val, left subtree structure, right subtree structure)

    1. Nested Tuple Representation
        (4, None, None) = [4,4,4]
        (2, (4, None, None), None) = [2, 2]
        (3, (2, (4, None, None), None), (4, None, None)) = [3]
        (1, (2, (4, None, None), None),  (3, (2, (4, None, None), None), (4, None, None))) = [4]

    2. Integers Mapping Representation
        (4, None, None) = 0 = [4,4,4]
        (2, 0, None) = 1 = [2, 2]
        (3, 1, 0) = 2 = [3]
        (1, 1, 2) = 3 = [1]
    

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:

        # Initialize a dict to store all observed subtree structure
        trees = defaultdict(list)

        # Initialize a dict to map subtree structure to integers
        treesId = defaultdict()
        treesId.default_factory = treesId.__len__

        # DFS through the tree and summarize each subtree structure including the root node and its two subtrees
        def summarize(node):

            # If there is a node
            if node:

                # Calculate the subtree summary
                id = treesId[(node.val, summarize(node.left), summarize(node.right))]

                # Store the current root node based on the summary
                trees[id].append(node)

                # Return the summary
                return id

        # Start summarize all subtree structures starting from the root node
        summarize(root)

        # Return a node from each subtree if we observe such subtree structure occurred more than once 
        return [nodes[0] for nodes in trees.values() if len(nodes) > 1]
