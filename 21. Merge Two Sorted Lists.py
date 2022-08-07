"""
Problem
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    
    Example 2:
    Input: list1 = [], list2 = []
    Output: []
    Example 3:

    Input: list1 = [], list2 = [0]
    Output: [0]

Solution:
    Iterate through both listnodes and add nodes with the smallest value to the tail of the the result listnode. Continue until one of the listnodes reaches the end. Finally, append the remaining nodes of the listnode that hasn't reach the end to the result listnode.  

Complexity:
    Time: O(m + n) where m and n are lengths of list1 and list2
    Space: O(1)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        # Initialize the result listnode
        head = tail = ListNode()

        # Iterate until one of the listnodes reaches the end
        while list1 and list2:

            # If a node of the first listnode is less than or equal to a node of the second listnode
            if list1.val <= list2.val:

                # Add such node to the tail of the result listnode
                tail.next = ListNode(list1.val)

                # Update tail of the result listnode and the head of the first listnode
                tail, list1 = tail.next, list1.next

            # Else if a node of the first listnode is greater than a node of the second listnode
            else:

                # Add such node to the tail of the result listnode
                tail.next = ListNode(list2.val)

                # Update tail of the result listnode and the head of the second listnode
                tail, list2 = tail.next, list2.next

        # Append the remaining nodes to the end of the result listnode
        tail.next = list1 if list1 else list2

        return head.next
