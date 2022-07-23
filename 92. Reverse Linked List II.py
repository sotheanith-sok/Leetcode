"""
Problem:
    Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

    Example 1:

    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
    Example 2:

    Input: head = [5], left = 1, right = 1
    Output: [5]

Solution:
    Iterate through all nodes and keep track of nodes before the left, at the left, at the right, and after the right. Nodes at the left and right will be the head and tail of the reversed ListNode. Reverse nodes between left and right by setting subsequent node as the head. Lastly, connect the node before the left to the head of reversed ListNode and the tail of the reversed ListNode to the node after the right.   

Complexity:
    Time: O(n)
    Space: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        # Pointers to keep track of the head and tail of the reversed ListNode
        rHead, rTail = None, None

        # Pointers to keep track of nodes that come before and after the reversed ListNode
        before, after = None, None

        # Initialize a variable to keep track of node's index
        i = 1

        # Initialize a variable to keep track of the current node
        node = head

        # Iterate until there isn't anymore node or we reach right + 1
        while node and i <= right + 1:

            # Save the node before the reversed ListNode when we see it
            if i == left - 1:
                before = node

            # Save the node after the reversed ListNode when we see it
            if i == right + 1:
                after = node

            # Set the current node as a new head
            if left <= i <= right:
                rHead = ListNode(node.val, rHead)

            # Save the first node in the reversed ListNode as the tail
            if i == left:
                rTail = rHead

            # Move to the next node
            node, i = node.next, i + 1

        # If we found a node before the head of the reversed ListNode
        if before:

            # Point that node to the head
            before.next = rHead

        # Else, set the head as the new overall head
        else:
            head = rHead

        # If we found a node located after the tail of the reversed ListNode, link the tail of reversed ListNode with it
        if after:
            rTail.next = after

        return head

