"""
Problem:
    Given a string s, return the longest palindromic substring in s.

    Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
    
    Example 2:
    Input: s = "cbbd"
    Output: "bb"

Solution:
    Iterate through all characters and use them as the starting point of a palindrome. There are two cases to consider. The first case is the odd case where the left and the right pointers are set to the character. The second case is the even case where the left pointer is set to the character and right pointer is set to the subsequent character. Save the longest possible palindrome.  

Complexity:
    Time: O(n**2)
    Space: O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find(l, r):
            # Find the longest palindrome from the two pointers

            # Keep expanding the window if pointers aren't out of bound and characters at both pointers are the same
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1

            return s[l + 1 : r]

        res = ""

        # Iterate through all characters
        for i in range(len(s)):

            # Save the largest possible palindrome
            res = max(res, find(i, i), find(i, i + 1), key=len)

        return res

