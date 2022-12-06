""" 
Problem:
    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should remain as it was in the input.

    You must solve the problem in O(1) extra space complexity and O(n) time complexity.

    Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]
    
    Example 2:
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]

Solution:
    Iterate through all nodes and split them into odd listNodes and even listNodes. Then, connect the tail of odd listNodes with the head of even listNodes. Lastly, return the head of the odd listNodes.

Complexity:
    Time: O(n)
    Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        # Initialize the head and tail of the odd listNodes with a dummy node
        oddHead = oddTail = ListNode()

        # Initialize the head and tail of the even listNodes with a dummy node
        evenHead = evenTail = ListNode()

        # Initialize the current node
        node = head

        # While there is a current node
        while node:

            # Connect the current node and the next node to the tail of both listNodes
            # Then, move the current node forward
            oddTail.next, evenTail.next, node = (
                node,
                node.next,
                node.next.next if node.next else None,
            )

            # Move the tail of both listNodes to their respective last nodes
            oddTail, evenTail = (
                oddTail.next if oddTail else oddTail,
                evenTail.next if evenTail else evenTail,
            )

        # Connect the tail of the odd listNodes with the head of the even listNodes
        oddTail.next = evenHead.next

        # Return the head of the odd listNodes
        return oddHead.next
