"""
Problem:
    Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

    Implement the Solution class:

    Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
    int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
    
    Example 1:
    Input
    ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
    [[[1, 2, 3]], [], [], [], [], []]
    Output
    [null, 1, 3, 2, 2, 3]
    Explanation
    Solution solution = new Solution([1, 2, 3]);
    solution.getRandom(); // return 1
    solution.getRandom(); // return 3
    solution.getRandom(); // return 2
    solution.getRandom(); // return 2
    solution.getRandom(); // return 3
    // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.

Solution:
    Assume that there are infinite nodes in the linked nodes. We will solve this problem using reservoir sampling. Start by initializing a reservoir list of fixed size k and populate such with the first kth nodes. Then, for every random call, we will replace a random node in the reservior with a node from the linked node and return a random node from the reservior.

Complexity:
    Time: O(k) where k is the reservior size
    Space: O(k)
"""

import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):

        # Initialize the reservior and two pointers pointing to the head and the current node of the linked node
        self.reservoir, self.node, self.head = [], head, head

        # Add the first kth nodes into the reservior
        while self.node and len(self.reservoir) < 100:
            self.reservoir.append(self.node.val)
            self.node = self.node.next

        # If there isn't enough node to fill the reservior, reset the current pointer back to the head
        if not self.node:
            self.node = self.head

    def getRandom(self) -> int:

        # Replace a random node in the reservior with the current node of the linked node
        self.reservoir[random.randint(0, len(self.reservoir) - 1)] = self.node.val
        self.node = self.node.next if self.node.next else self.head

        # Return a random node from the reservior
        return self.reservoir[random.randint(0, len(self.reservoir) - 1)]
