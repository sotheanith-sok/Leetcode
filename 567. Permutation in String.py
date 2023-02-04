""" 
Problem:
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.

    Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
    
    Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

Solution:
    Since we want to check if a permuation of s1 is in s2 (we don't care about order), we will count characters in s1. Then, we will use a sliding window of size s1 and slide it over s2. If a substring of s2 has the same characters count as s1, we have found the solution.  

Complexity:
    Time: O(n) where n is the length of s2
    Space: O(m) where m is the length of s1
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Count chracters in s1
        target = Counter(s1)

        # Initialize some varaibles for cleaner code.
        m, n = len(s1), len(s2)

        # Initialize the current count of a sliding window and the left pointer.
        cur, l = {}, 0

        # The right pointer will iterate through all characters in s2
        for r in range(n):
            charL, charR = s2[l], s2[r]

            # Increment the character at the right pointer in the current count
            cur[charR] = cur[charR] + 1 if charR in cur else 1

            # If the size of the window exceed the length of s1
            if r - l + 1 > m:

                # Shrink the window by increment the left pointer.
                cur[charL], l = cur[charL] - 1, l + 1
                if cur[charL] == 0:
                    cur.pop(charL)

            # Check if the current count is the same as the s1 count.
            if cur == target:
                return True

        return False

