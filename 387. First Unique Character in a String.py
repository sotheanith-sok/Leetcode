"""
Problem:
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

    Example 1:
    Input: s = "leetcode"
    Output: 0
    
    Example 2:
    Input: s = "loveleetcode"
    Output: 2
    
    Example 3:
    Input: s = "aabb"
    Output: -1

Solution:
    Iterate through all characters and keep track of each character counts in an ordered dictionary and the first occurrence of each character in a normal dictionary. Then, iterate through the ordered dictionary and find the first character that has a count of 1. If there is one, find the first occurence of such character and return the index. Else, return -1.  

Complexity:
    Time: O(n)
    Space: O(1)
"""

from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Initialize an ordered dict to store counts of all characters and a dict to store first occurrence of each character
        counts, first = OrderedDict(), {}

        # Iterate through all characters
        for i, c in enumerate(s):

            # Update the current character count 
            counts[c] = counts[c] + 1 if c in counts else 1

            # If this is the first time we see such character, save its index
            if c not in first:
                first[c] = i

        # Iterate through all chracters in the ordered dict and find a character that has its count of 1. If there is one, return its first occurrence. 
        for c, count in counts.items():
            if count == 1:
                return first[c]

        # Else, return -1
        return -1

