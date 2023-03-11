"""
Problem:
    Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
    height-balanced binary search tree.

    Example 1:
    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
    
    Example 2:
    Input: head = []
    Output: []

Solution:
    Convert the linked list into a array of values. Then, recursively build a balanced binary search tree by spliting the array into two equal partitions, one for each subtree.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        # Convert the linked list into an array of values
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # Recursively build a balanced binary search tree by splitting the array of values into two equal partitions
        def BST(l, r):

            # If there is a single value left, return the leaf node
            if l >= r:
                return TreeNode(values[l]) if l == r else None

            # Else, partition the array of values into two equal partitions
            mid = (r - l) // 2 + l

            # Set the middle value as a root node and left and right partition as their respective subtrees
            return TreeNode(values[mid], BST(l, mid - 1), BST(mid + 1, r))

        return BST(0, len(values) - 1)
