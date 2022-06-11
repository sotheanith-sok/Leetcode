"""
Problem:
    Given the head of a linked list, rotate the list to the right by k places.

    Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
    
    Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

Solution:
    Convert the linked list to a list and performs the shifting. Then, convert the resulting list back to a linked list.
Complexity:
    Time: O(n)
    Space: O(n)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # Extract all values from a list nodes into a list
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next

        # Shift each value in the list by k steps.
        N = len(values)
        res = [0] * N
        for i, v in enumerate(values):
            new_i = (i + k) % N
            res[new_i] = v

        # Create a new list nodes from the new order.
        head = ListNode()
        node = head
        for v in res:
            node.next = ListNode(v)
            node = node.next

        # Return the result.
        return head.next

