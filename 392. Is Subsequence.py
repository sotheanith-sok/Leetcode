"""
Problem:
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

    Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Solution:
    Initialize a pointer at the starting of s. Iterate through all characters in t. If a character is the same as the character at the pointer, increment the pointer. When the pointer reach length of s, we have found a solution. Else, return False 

Complexity:
    Time: O(n) where n is the length of t 
    Space: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # If s is an empty string, it will always be a subsequent
        if len(s) == 0:
            return True

        # Else, if t is an empty string, return False as a non empty string can't be the subsequent of an empty string
        if len(t)==0:
            return False

        # Initialize the pointer
        i = 0

        # Iterate through all characters in t
        for c in t:

            # If the current character is the same the character at the pointer, increment the pointer
            if s[i]==c:
                i+=1

            # If the pointer reaches length of s, return True
            if i ==len(s):
                return True
        
        # Else, return False
        return False