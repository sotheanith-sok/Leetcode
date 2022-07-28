"""
Problem:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:

    Input: s = "rat", t = "car"
    Output: false

Solution:
    Count characters and their frequencies in both strings. If they are the same, return True. Else, return False. 

Complexity:
    Time: O(m + n) where m is the length of s and n is the lenght of t
    Space: O(1)
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

