"""
Problem:
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
    
    Example 2:
    Input: lists = []
    Output: []
    
    Example 3:
    Input: lists = [[]]
    Output: []

Solution:
    Use a min heap to keep track of ListNodes with the lowest value at the head. While the heap isn't empty. Pop a ListNode and add its head into the result. Then, move such ListNode head to the next node. If the ListNode head isn't pointing to a None, add it back to the heap. 

Complexity:
    Time: O(nlogn) where n is the number of nodes
    Space: O(n)
"""
# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:

        # Add all ListNodes based on their head values and their indices. You can't add ListNode into the heap since it doesn't implement any comparable. 
        heap = [(node.val, i) for i, node in enumerate(lists) if node]

        # Heapify the heap
        heapq.heapify(heap)

        # Initialize the result
        res = ListNode()

        # Initialize the end pointer of the result
        end = res

        # While the heap isn't empty
        while heap:

            # Pop a ListNode
            val, i = heapq.heappop(heap)

            # Add its head value as a new node to the end of the result
            end.next = ListNode(val)

            # Move the end pointer to the last node in the result
            end = end.next

            # Move the current ListNode head to the next node
            lists[i] = lists[i].next

            # If such head isn't pointing to none, add the ListNode back into the heap
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        return res.next

