"""
Problem:
    You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

    The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
    
    Example 1:
    Input: head = [1,3,4,7,1,2,6]
    Output: [1,3,4,1,2,6]
    Explanation:
    The above figure represents the given linked list. The indices of the nodes are written below.
    Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
    We return the new list after removing this node. 
    
    Example 2:
    Input: head = [1,2,3,4]
    Output: [1,2,4]
    Explanation:
    The above figure represents the given linked list.
    For n = 4, node 2 with value 3 is the middle node, which is marked in red.
    
    Example 3:
    Input: head = [2,1]
    Output: [2]
    Explanation:
    The above figure represents the given linked list.
    For n = 2, node 1 with value 1 is the middle node, which is marked in red.
    Node 0 with value 2 is the only node remaining after removing node 1.

Solution:
    Run two pointers through the list of nodes with a slow pointer moving at 1 step and a  fast pointer moving at 2 step. When the fast pointer reached the end of the list, the slow pointer will reach the middle node. Then, there are two cases to consider here.

    1. If there are odd number of nodes in the list, we have to remove the node at slow pointer.
                  s         f
        1 -> 2 -> 3 -> 4 -> 5 

    2. If there are even number of nodes in the list, we have to remove the next node after the slow pointer. 
                  s         f
        1 -> 2 -> 3 -> 4 -> 5 -> 6


Complexity:
    Time: O(n)
    Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:

        # If there is a single node in the list, return None
        if not head.next:
            return None

        # Initialize three pointers: previous (point to a node before the slow pointer), slow, and fast
        prev, slow, fast = None, head, head

        # Iterate through all nodes
        while True:

            # Move all three pointers until the fast pointer reached the end of the list
            if fast.next and fast.next.next:
                prev, slow, fast = slow, slow.next, fast.next.next
                continue

            # Even case: Remove the next node after the slow pointer
            if fast.next:
                slow.next = slow.next.next

            # Odd case: Remove the node at the slow pointer
            else:
                prev.next = slow.next

            break

        return head

