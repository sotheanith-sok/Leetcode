"""
Problem:
    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

    Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

    Example 2:
    Input: head = []
    Output: []

    Example 3:
    Input: head = [1]
    Output: [1]

Solution:
    Swap every even nodes with their next nodes. If there isn't a next node after the last even node, connect it to the tail. 

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
    def swapPairs(self, head: ListNode) -> ListNode:

        # Initialize the current node to the head of the given listnode
        node = head

        # Initialize the head and tail of the result listnode
        head = tail = ListNode()

        # Initialize the index of the listnode
        i = 0

        # Iterate until the current node is None
        while node:

            # If the current node is an even node
            if i % 2 == 0:

                # If there is a next node after the current node
                if node.next:

                    # Swap them and append the pair to the end of the result listnode
                    tail.next = ListNode(node.next.val, ListNode(node.val))

                    # Move the tail to the last node
                    tail = tail.next.next

                # Else
                else:

                    # Append the last node to the end of the result listnode
                    tail.next = ListNode(node.val)

                    # Move the tail to the last node
                    tail = tail.next

            # Move to the next node
            i, node = i + 1, node.next

        return head.next
