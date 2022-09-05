"""
Problem:
    Given an n-ary tree, return the level order traversal of its nodes' values.

    Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

    Example 1:
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [[1],[3,2,4],[5,6]]

    Example 2:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Solution:
    Traverse the tree using BFS and add values of all nodes at a level to the result.

Complexity:
    Time: O(n)
    Space: O(n)
"""


from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:

        # If there is no root, return empty list
        if not root:
            return []

        # Intialize the queue and result
        res, queue =[], deque([root])

        # Iterate until the queue is empty
        while queue:

            # Find how many nodes at this level
            n = len(queue)

            # Intialize a list to store all values of nodes at this level
            vals = []

            # Go through all nodes
            for _ in range(n):

                # Pop a node from the queue
                node = queue.popleft()

                # Add such node value onto the list
                vals.append(node.val)

                # If the current node has children
                if node.children:

                    # Add them to the queue
                    queue.extend(node.children)

            # Add values to the result
            res.append(vals)

        return res
