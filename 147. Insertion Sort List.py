""" 
Problem:
    Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

    The steps of the insertion sort algorithm:

    Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
    It repeats until no input elements remain.
    The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

    Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]
    
    Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Solution:
    In order to navigate the linked nodes efficiently, we will use two pointers to keep track of the start and the end of the linked nodes. We will iterate through all nodes and add each of them to a linked nodes. There are three base cases to consider for any given node. If the start pointer points to None, we know that there isn't a node in the linked node and thus, we create a new node and update the start and end pointers to point to it. If the current node is less the starting node, we will insert it to the beginning of the linked nodes and update the start pointer. If the current node is larger than the ending node, we will insert it at the end of the linked nodes and update the end pointer. Else, we will iterate through all nodes in the linked nodes from the start pointer until we find a node where it is less than the current node while it points to a node that is larger than the current node and we insert the current node between them. Repeat the process for all nodes. 

Complexity:
    Time: O(n**2)
    Space: O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Start and end pointers of the linked nodes.
        start, end = None, None

        # Iterate through all given nodes
        while head:

            # Store the current node.
            node = head

            # Update the head to the next node.
            head = head.next

            # If there isn't a node in the linked nodes, add the current node to it.
            if not start:
                start = end = ListNode(node.val)
                continue

            # If the current node is less than the starting node, add the current node to the beginning of the linked nodes.
            if start.val >= node.val:
                start = ListNode(node.val, start)
                continue

            # If the current node is larger than the ending node, add the current node to the end of the linked nodes.
            if end.val <= node.val:
                end.next = ListNode(node.val)
                end = end.next
                continue

            # Else, we will have to do a sequential search for a place to insert the current node.
            # Start from the starting node 
            node2 = start

            # Find a node that is less than the current node and its next node is larger than the current node, insert the current node between them. 
            while node2 and node2.next:
                if node2.val <= node.val <= node2.next.val:
                    node2.next = ListNode(node.val, node2.next)
                    break
                node2 = node2.next

        return start
