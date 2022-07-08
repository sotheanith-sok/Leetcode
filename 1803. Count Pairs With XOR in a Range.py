""" 
Problem:
    Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

    A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

    Example 1:
    Input: nums = [1,4,2,7], low = 2, high = 6
    Output: 6
    Explanation: All nice pairs (i, j) are as follows:
        - (0, 1): nums[0] XOR nums[1] = 5 
        - (0, 2): nums[0] XOR nums[2] = 3
        - (0, 3): nums[0] XOR nums[3] = 6
        - (1, 2): nums[1] XOR nums[2] = 6
        - (1, 3): nums[1] XOR nums[3] = 3
        - (2, 3): nums[2] XOR nums[3] = 5
    
    Example 2:
    Input: nums = [9,8,4,2,1], low = 5, high = 14
    Output: 8
    Explanation: All nice pairs (i, j) are as follows:
    ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
        - (0, 3): nums[0] XOR nums[3] = 11
        - (0, 4): nums[0] XOR nums[4] = 8
        - (1, 2): nums[1] XOR nums[2] = 12
        - (1, 3): nums[1] XOR nums[3] = 10
        - (1, 4): nums[1] XOR nums[4] = 9
        - (2, 3): nums[2] XOR nums[3] = 6
        - (2, 4): nums[2] XOR nums[4] = 5

Solution:
    Use a trie tree to store the binary representation of numbers and their counts. The height of the tree will be determine by the number of digit requires to represent the largest number. Then, to check how many pairs can be match up with a number such their XOR is less than a limit, we begin by traversing the tree. Let limitBit, targetBit represent the bit of the limit and the target at a certain height. If a limitBit is 1, we know that any subtree that XOR with the targetBit to produce a result of 0 can be pair with the target. 
        ie. 
            target:     1001...
            limit:      0101...
            targetBit:   0
            limitBit:    1 
            -> 
            subtree     10... 
                will be can be pair with the target
    
    Then, we traverse to the next node based on the targetBit XOR with limitBit.

    Full Explanation and Graph here: https://leetcode.com/problems/count-pairs-with-xor-in-a-range/discuss/1122495/C%2B%2B-with-picture 

Complexity:
    Time: O(n)
    Space: O(n)
"""


from math import log, floor
from collections import Counter


class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:

        # Implementation of trie node
        class TrieNode:
            def __init__(self, height=16) -> None:

                # Map to keep track of children counts
                self.counts = {}

                # Map to keep track of children
                self.children = {}

                # A digit to determine the heigh of the trie
                self.height = height

            def add(self, num, count):
                # Add a number to the trie node

                # Initialize the current node
                node = self

                # Go through entire trie height
                for i in range(self.height, -1, -1):

                    # Extract the i bits from the number
                    numBit = (num & (1 << i)) >> i

                    # If this bit is a children, update the count
                    if numBit in node.children:
                        node.counts[numBit] += count

                    # Else, initialize a new child
                    else:
                        node.counts[numBit] = count
                        node.children[numBit] = TrieNode()

                    # Move to the next node
                    node = node.children[numBit]

            def pair(self, num, limit):
                # Search how many numbers can be XOR with a given number such that its result is less than the limit

                # Initialzie a varaiable to keep track of pairs.
                pairs = 0

                # Initialize the starting node
                node = self

                # Traverse the entire trie height
                for i in range(self.height, -1, -1):

                    # Extract the ith bit from the number
                    numBit = (num & (1 << i)) >> i

                    # Extract the ith bit from the limit
                    limitBit = (limit & (1 << i)) >> i

                    # If the limitBit is 1, find the subtree that can be XOR with the numBit to produce a 0. aka 0 subtree for the 0 numBit and 1 subtree for the 1 numBit.
                    if limitBit == 1 and numBit in node.children:
                        pairs += node.counts[numBit]

                    # Continue to the next node if possible
                    if numBit ^ limitBit in node.children:
                        node = node.children[numBit ^ limitBit]
                    else:
                        break

                return pairs

        # Count the numbers
        count = Counter(nums)

        # Determine the largest bits necessary to store the largest value
        digit = floor(log(max(max(count), low, high), 2)) + 1

        # Initialize the trie node
        root = TrieNode(digit)

        # Intialize the result
        res = 0

        # Iterate through all numbers
        for n in count:

            # Find the number of pairs can be match with the current number such that its result is between the high and the low.
            res += (root.pair(n, high + 1) - root.pair(n, low)) * count[n]

            # Add the current number to the trie
            root.add(n, count[n])

        return res

