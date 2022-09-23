"""
Problem:
    You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

    If isLefti == 1, then childi is the left child of parenti.
    If isLefti == 0, then childi is the right child of parenti.
    Construct the binary tree described by descriptions and return its root.

    The test cases will be generated such that the binary tree is valid.

    Example 1:
    Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    Output: [50,20,80,15,17,19]
    Explanation: The root node is the node with value 50 since it has no parent.
    The resulting binary tree is shown in the diagram.
    
    Example 2:
    Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
    Output: [1,2,null,null,3,4]
    Explanation: The root node is the node with value 1 since it has no parent.
    The resulting binary tree is shown in the diagram.

Solution:
    Use two sets to keep track of nodes that are a potential root node and nodes that have a parent. Use a dict to map values to nodes. Iterate through all descriptions. At each iteration, link the child node with the parent node. Then, mark the child node as having parent and unmark it as a potential root node. Next, if the parent node does not have a parent, mark it as a potential root node. Lastly, there should only one potential root node left after iterating through all description. 

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
    def createBinaryTree(self, descriptions: list[list[int]]):

        # A dict mapped values to nodes
        nodes = defaultdict(TreeNode)

        # A set to keep track of nodes are a potential root node
        roots = set()

        # A set to keep track of nodes that have a parent
        hasParent = set()

        # Iterate thorugh all descriptions
        for parent, child, isLeft in descriptions:

            # Intialize both nodes with their values
            nodes[parent].val, nodes[child].val = parent, child

            # Link the child node to its parent node
            nodes[parent].left, nodes[parent].right = (
                (nodes[child], nodes[parent].right)
                if isLeft
                else (nodes[parent].left, nodes[child])
            )

            # Mark the child node as having a parent
            hasParent.add(child)

            # Unmark the child node as a potential root node
            roots.discard(child)

            # If the parent node has no parent, mark it as a potential root node
            if parent not in hasParent:
                roots.add(parent)

        # Return the root node
        return nodes[roots.pop()]

