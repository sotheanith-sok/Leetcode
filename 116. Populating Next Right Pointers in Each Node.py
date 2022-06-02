""" 
Problem:
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

    struct Node {
        int val;
        Node *left;
        Node *right;
        Node *next;
    }

    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL. 

    Example 1:
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]
    Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
    
    Example 2:
    Input: root = []
    Output: []

Solution:
    1. BFS - Add the root node to the queue. Until the queue is empty, calculate the size of the queue which indicates the how many nodes in each level. At each iteration, pop a certain amount of nodes from the queue up until the queue size. For each node, if there is a previous node, link previous node to the current node. Append the left and right child nodes to the queue if existed.  

    2. O(1) Space - Inspire by the BFS solution, we will use two pointers: one for the current node and another for the node at the start of the next level. We will iterate through all nodes in a level using the current node pointer and for each node, we will connect its children and connect its right child to the left child of the next node if it existed. Then, we update the current pointer to the next node. If there is no next node, we will set the current pointer to start of next level node pointer and update the node to the start of next level node pointer to its left child. Repeat until the current or the start of next level node is null. 
Complexity:
    1. Time: O(n), Space: O(n)
    2. Time: O(n), Space: O(1)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Solution 1 - BFS
class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":

        # Create the queue for BFS
        queue = []
        queue.append(root)

        # Loop until queue is empty
        while queue:

            # Calculate how many node in this level
            size = len(queue)
            prev = None

            # Remove all nodes from a level
            for _ in range(size):

                # If there is a previous node, link it to the current node.
                node = queue.pop(0)
                if prev:
                    prev.next = node
                prev = node

                # Add left and right child nodes to the queue.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


# Solution 2 - Optimal Solution
class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        # Current node
        current_node = root

        # Use this pointer to keep track of the node at the  start of the next level.
        start_next_level_node = root.left if root else None

        # While we are one level above the last level
        while start_next_level_node:

            # Connect the left and right children of the current node
            if current_node.right:
                current_node.left.next = current_node.right

            # Connect the right children of the current node to the left children of the next node
            if current_node.right and current_node.next:
                current_node.right.next = current_node.next.left

            # Set the current node to the next node
            current_node = current_node.next

            # If there is no next node, set the current node to the node at the start of the next leve. Update the pointer to the node at the start of next level. 
            if not current_node:
                current_node = start_next_level_node
                start_next_level_node = current_node.left

        return root