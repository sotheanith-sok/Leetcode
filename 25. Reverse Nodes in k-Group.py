"""
Problem:
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

    k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.

    Example 1:

    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    
    Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Solution:
    Iterate through all nodes k group at a time. At the start of a group, we set the tail of the previous group to the current node. We are doing this because we don't have to reverse the last group if it contains less than k nodes. Then, build a reversed list nodes of a group by continue to set subsequent node as the head and keep track of the head and tail of the reversed nodes group. Once, we processed k nodes, we can set the tail of the previous group to the head of the reversed nodes group and update the previous group tail to the tail of the reversed nodes group. 

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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # Intialize the result and the current node to the head
        res = node = head

        # Initialize the index of the current node to 0
        i = 0

        # Initialize the head and tail of the reversed nodes group to None
        reversedHead, reversedTail = None, None

        # Initialize the tail of the previous group to None
        previousTail = None

        # Iterate through all nodes
        while node:

            # When we reach the first node in a group
            if i % k == 0:

                # If there is a previous group, connect its tail to the current node
                # This is the case when we have less than k nodes left
                if previousTail:
                    previousTail.next = node

                # Initialize the head and tail of the reversed nodes group
                reversedHead = reversedTail = ListNode(node.val)

            # Continue to reverse subsequent nodes
            else:
                reversedHead = ListNode(node.val, reversedHead)

            # If we are able to reach the last node in a reversed nodes group
            if i % k == k - 1:

                # If there is a previous group, connect its tail to the current node
                # This is the case when we have k nodes and thus, we should reverse this group
                if previousTail:
                    previousTail.next = reversedHead

                # Set the tail of the previous group to the tail of the reversed nodes group
                previousTail = reversedTail

            # Set the head of the first reversed nodes group as the result
            if i == k - 1:
                res = reversedHead

            # Continue to the next node
            i, node = i + 1, node.next

        return res
