"""
Problem:
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false
    
    Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false
    
    Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Solution:
    Count all characters and their frequencies of ransomeNote and magazine. For each character in the ransomNote, check if we have such character in the magazine and at the correct frequency. If yes, return True. Else, return False.

Complexity:
    Time: O(m + n) where m and n are the length of ransomNote and magazine
    Space: O(m + n)
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Count characters in the ransomeNote and magazine
        ransomNote, magazine = Counter(ransomNote), Counter(magazine)

        # Check if all characters in the ransomNote contain in magazine
        for c in ransomNote:

            # If not, return False
            if c not in magazine or ransomNote[c] > magazine[c]:
                return False

        # Else, return True
        return True
