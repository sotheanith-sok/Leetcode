"""
Problem:
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    
    Example 2:
    Input: head = [1], n = 1
    Output: []
    
    Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Solution:
    Iterate through all nodes and save them into a list. Then, remove the target node. 

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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # Save all nodes into a list
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        # Find which node is the target
        n = len(nodes) - n

        # If the target is the 0th node, return the remaining node
        if n == 0:
            return nodes[1] if len(nodes) > 1 else None

        # Else, connect the node before the target to the node after the target
        nodes[n - 1].next = nodes[n + 1] if n + 1 < len(nodes) else None

        return nodes[0]
