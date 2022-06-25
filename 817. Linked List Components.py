""" 
Problem:
    You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

    Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

    Example 1:
    Input: head = [0,1,2,3], nums = [0,1,3]
    Output: 2
    Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
    
    Example 2:
    Input: head = [0,1,2,3,4], nums = [0,3,1,4]
    Output: 2
    Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Solution:
    We can use a variable to keep track of when we detect a connected component. Iterate thorugh all node. At each iteration, check if the current node is in nums. If yes and we haven't found a connected component, we increment the res by 1 and change "found" to True. Continue to interate through node until we found a node that isn't in nums and change "found" to False.  

Complexity:
    Time: O(n)
    Space: O(1)
"""
# Definition for singly-linked list.
class Listhead:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Listhead, nums: list[int]) -> int:

        # Change nums to a set for O(1) checking
        nums = set(nums)

        # Initalize a varaible to keep track of if we found a connected component and the number of connected components found
        found, res = False, 0

        # Iterate thorugh all nodes
        while head:

            # If we haven't found a connected component and the current node is in nums, increment the res by 1 and change found to true
            if not found and head.val in nums:
                res, found = res + 1, True

            # If we found a connected component and the current node isn't in nums, change found to false
            if found and head.val not in nums:
                found = False

            # Go to next node
            head = head.next

        return res

