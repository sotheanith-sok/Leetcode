"""
Problem:
    You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

    The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

    Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

    Example 1:
    Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
    Output: [3,3,7]
    Explanation:
    1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
    2) 1 XOR 2 = 3.
    3) 5 XOR 2 = 7.
    
    Example 2:
    Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
    Output: [15,-1,5]

Solution:
    Use trie to store bit representation of all numbers. Instead of querying the trie while ensuring that each number won't exceed the limit, we should only add valid numbers to the trie. Start by sorting the queries based on limits and nums. Then, while the last value in nums is less than the limit, add the number to the trie. Finally, query the trie for a number that when xor with the current target will result in the largest number. 

    Instead of finding the term that can be xor with the current target to produce the largest number, we will instead finding the largest number. Initally, the result is 0. At every bit position, if there exists a bit in the trie that is opposite of the bit of the current target, we update the result bit to 1 because two opposite bits will xor to 1. Else, don't do anything as bits are already 0. 

Complexity:
    Time: O(nlogn + mlogm) where n is length of nums and m is the length of queries
    Space: O(n)
"""


class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        # An implementation of the trie
        class Trie:
            def __init__(self) -> None:

                # We won't use TrieNode -> hashmap -> TrieNodes structure to improve the speed.
                # Instead use hashmap -> hashmap -> hashmap
                self.root = {}

            def insert(self, n):

                # Add a number into the trie
                # Intialize the first node
                node = self.root

                # Each number will be represented with 32 bits
                for i in range(31, -1, -1):

                    # Extract a bit at ith place
                    bit = (n >> i) & 1

                    # If such bit doesn't exist in node
                    if bit not in node:

                        # Add it
                        node[bit] = {}

                    # Continue to the next node
                    node = node[bit]

            def query(self, n):
                # Query for the largest xor result

                # If the root node is empty, return -1
                if not self.root:
                    return -1

                # Set the current node to the root node
                node = self.root

                # Intialize the result
                res = 0

                # Iterate through all bits
                for i in range(31, -1, -1):

                    # Extract the bit at ith place
                    bit = (n >> i) & 1

                    # If an opposite of such bit exists in the node
                    if 1 - bit in node:
                        
                        # Update the result bit to 1 because two opposite bits will xor to 1
                        res |= 1 << i

                        # Move to the opposite node
                        node = node[1 - bit]

                    # Else, move to the similar node
                    else:
                        node = node[bit]

                return res

        # Sort queries based on the limit. Keep track of the original indices
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])

        # Sort numbers
        nums.sort()

        # Initailize the trie
        root = Trie()

        # Pointer to j
        j = 0

        # Intialize the result
        res = [-1] * len(queries)

        # Iterate through all queries
        for pos, (target, limit) in queries:

            # Add all numbers that is than the current limit
            while j < len(nums) and nums[j] <= limit:
                root.insert(nums[j])
                j += 1

            # Query the trie for the largest xor result
            res[pos] = root.query(target)

        return res
