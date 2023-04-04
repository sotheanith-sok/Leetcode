"""
Problem:
    Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

    Return the minimum number of substrings in such a partition.

    Note that each character should belong to exactly one substring in a partition.

    Example 1:
    Input: s = "abacaba"
    Output: 4
    Explanation:
    Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
    It can be shown that 4 is the minimum number of substrings needed.
    
    Example 2:
    Input: s = "ssssss"
    Output: 6
    Explanation:
    The only valid partition is ("s","s","s","s","s","s").

Solution:
    Iterate through characters in s and keep track of observed characters. If the current character existed in the current partition, we have to start a new partition. Return the number of partitions.

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def partitionString(self, s: str) -> int:

        # Initialize the result and a set to keep track of exisiting characters
        res, existed = 0, set()

        # Iterate through all characters
        for c in s:

            # If the current character existed in the current partition, we have to start a new partition
            if c in existed:

                # Increment the result
                res += 1

                # Clear the existing characters of the current partition
                existed.clear()

            # Mark the current character as existed
            existed.add(c)

        # Return the number of partition
        return res + int(len(existed) > 0)
