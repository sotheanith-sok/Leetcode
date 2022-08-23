"""
Problem:
    Given the head of a singly linked list, return true if it is a palindrome.

    Example 1:
    Input: head = [1,2,2,1]
    Output: true

    Example 2:
    Input: head = [1,2]
    Output: false

Solution:
    Use a slow and a fast pointers to find the mid point. The slow pointer will be pointed at the middle node when the fast pointer reaches the end of the list. As we iterate, reverse the first half of the list by pointer the node at the slow pointer to the previous node. Lastly, compare the reversed first half with the second half of the list. If any pairs of values aren't equal, return False. Else, return True. 

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
    def isPalindrome(self, head: ListNode) -> bool:

        # Initialize the head of the reversed listnodes
        rHead = None

        # Initiaze the slow and fast pointers
        slow = fast = head

        # Iterate until the fast pointer reaches the end of the listnodes
        while fast and fast.next:

            # Move the fast pointer forward
            fast = fast.next.next

            # Reverse nodes at the slow pointer by pointer them to their previous nodes
            # You can do "rHead, rHead.next, slow = slow, rHead, slow.next" too
            prev = rHead
            rHead = slow
            slow = slow.next
            rHead.next = prev

        # If we have odd numbers of nodes, move the slow pointer forward
        if fast:
            slow = slow.next

        # Compare the reversed first half with the second half of the listnodes
        while rHead and slow:

            # If a pair of nodes have different values, return False
            if rHead.val != slow.val:
                return False

            # Move the two pointers forward
            rHead, slow = rHead.next, slow.next

        # Else, return True
        return True

