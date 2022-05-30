"""
Problem:
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Solution (Basic Arithmetic):
    Create a result listnode, a pointer that points to the end of such list, and a carry variable. Keep iterating until reaching the end of list1 and list2 and the carry is 0. At each iteration, sum the value of list1, list2, and carry. Append the ones digit to the end of the result list and save the remaining digits to the carry variable. Update all relevant pointers and return the result listnode at the end of the loop.  

Complexity:
    Time: O(max(m,n)) where m is len(list1) and n is len(list2)
    Space: O(max(m,n)) where m is len(list1) and n is len(list2)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> list[ListNode]:

        # Create result listnode, a pointer, and a variable to store the carry value.
        res = ListNode()
        ptr = res
        carry = 0

        # Iterate until the end of l1 and l2 and carry is 0
        while l1 or l2 or carry:

            # Performe arithmetic.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # Store the summation in the end of res listnode and the carry varaible.
            ptr.next, carry = ListNode(total % 10), total//10

            # Update l1, l2, and the pointer
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            ptr = ptr.next

        # Return result's next since the first node in result always 0.
        return res.next
