""" 
Problem:
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.
    
    Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Solution:
    Use Floyd's Tortoise and Hare Algorithm algorithm to solve this problem. Run two pointers through the listnode where a slow pointer moves one step at time and a fast pointer moves two steps at a time. The slow pointer will reach the middle node when the fast pointer reach the last node. Return the corresponding middle node based on if there is an odd or even nodes in the list. 

Complexity:
    Time: O(n)
    Space: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        # Initialize the slow and fast pointers
        slow = fast = head

        # Move both pointers through the list nodes
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        # Return the corresponding middle node 
        return slow if not fast.next else slow.next
        