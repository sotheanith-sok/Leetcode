"""
Problem:
    Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.

    

    Example 1:


    Input: head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
    Example 2:

    Input: head = [2,1], x = 2
    Output: [1,2]

Solution:
    Partition listnode into two listnodes where one is smaller than x and another one is greater than or equal to x

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
    def partition(self, head: ListNode, x: int) -> ListNode:

        # Initialize the head and current pointers to the two listnode
        lHead, lesser = None, None
        gHead, greater = None, None

        # Initialize the pointer to the current node
        node = head

        # Iterate through all nodes
        while node:

            # If the current node is less than x
            if node.val < x:

                # If this is the first node, update the head and current pointers of the lesser listnode to this node
                if not lesser:
                    lHead = lesser = ListNode(node.val)
                
                # Else, add this node to the end of the lesser listnode
                else:
                    lesser.next = ListNode(node.val)
                    lesser = lesser.next
                    
            # If the current node is greater than or equal to x
            else:

                # If this is the first node, update the head and current pointers of the greater listnode to this node
                if not greater:
                    gHead = greater = ListNode(node.val)
                
                # Else, add this node to the end of the less listnode
                else:
                    greater.next = ListNode(node.val)
                    greater = greater.next
            
            # Move to the next node
            node = node.next

        # If there is a lesser listnode
        if lHead:

            # Connect its end to the greater listnode
            lesser.next = gHead

            # Return the lesser listnode
            return lHead
        
        # Else, return the greater listnode
        else:
            return gHead
