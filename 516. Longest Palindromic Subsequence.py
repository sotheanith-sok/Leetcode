"""
Problem:

    Given a string s, find the longest palindromic subsequence's length in s.

    A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

    

    Example 1:

    Input: s = "bbbab"
    Output: 4
    Explanation: One possible longest palindromic subsequence is "bbbb".
    Example 2:

    Input: s = "cbbd"
    Output: 2
    Explanation: One possible longest palindromic subsequence is "bb".
 
Solution:
    Solve this problem using dynamic programming. Let dp be the function that return the longest palindrome for a given sequence starting from some arbitrary i-th index and ending at some arbitrary j-th index. We can define dp as
        dp(i, j) =  0                           if i > j            
                                                (Invalid sequence)
                 
                 =  1                           if i == j           
                                                (Sequence of length 1 is always a palindrome)
                 
                 =  2 + dp(i+1, j-1)            if s[i] == s[j]     
                                                (Starting and ending characters are equal and thus we add 2 to the longest palindrome between such character)
                 
                 =  max(dp(i+1, j), dp(i, j-1)) if s[i] != s[j]     
                                                (Take the maximum between the longest plaindrome skipping starting and ending characters)


Complexity:
    Time: O(n**2)
    Space: O(n**2)
"""


from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # Find the length of the given string
        n = len(s)

        # Find the longest palindrome
        @lru_cache(None)
        def dp(i, j):

            # Case 1: Invalid sequence
            if i > j:
                return 0

            # Case 2: Sequence of length 1 is always a palindrome
            if i == j:
                return 1

            # Case 3: Starting and ending characters are equal and thus we add 2 to the longest palindrome between such character
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)

            # Case 4: Take the maximum between the longest plaindrome skipping starting and ending characters
            return max(dp(i + 1, j), dp(i, j - 1))

        return dp(0, n - 1)
