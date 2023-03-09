"""
Problem:
    Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

    Do not modify the linked list.

    Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
    
    Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.
    
    Example 3:
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

Solution:
    Solve this problem using Floyd's Cycle Finding Algorithm. Initialize two pointers: slow and fast to the head of the linked nodes where slow pointer moves 1 step at a time and fast pointer moves 2 steps at a time. Move both pointers forward until both of them meet or one of the pointer reaches the end of linked nodes. 

    If both pointers meet, there must be a cycle and thus, we can detect the starting node of such cycle by running the current slow pointer and another slow pointer starting from the head forward until they meet. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        # Initialize the slow and fast pointers to the head of the linked nodes
        slow = fast = head

        # Iterate until both pointers meet or one of the pointer reach the end of the linked nodes
        while slow and fast:
            slow = slow.next if slow else None
            fast = fast.next.next if fast and fast.next else None

            if slow == fast:
                break

        # If one of the pointer reaches the end of the linked nodes, there is no cycle
        if not slow or not fast:
            return None

        # Else, initialize a second slow pointer starting from the head
        slow2 = head

        # Iterate both slow pointers forward until they meet
        while slow != slow2:
            slow, slow2 = slow.next, slow2.next

        return slow
