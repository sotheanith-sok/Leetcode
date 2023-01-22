"""
Problem:
    Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

    Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]
    
    Example 2:
    Input: s = "a"
    Output: [["a"]]
    
Solution:
    We can solve this problem using backtracking. Iterate through the string and partition it into palindrome terms. At each iteration, we will continue to expand the term until it is palindrome and then, we will save such term into the partition. Repeat the process until we used all characters of a given string.  

Complexity:
    Time: O(n 2**n)
    Space: O(2**n)
"""


from functools import lru_cache


class Solution:
    def partition(self, s: str) -> list[list[str]]:

        # Check if a given string is a palindrome
        @lru_cache(None)
        def isPalindrome(s):

            # Initialize the left and right pointers
            l, r = 0, len(s) - 1

            # Iterate until the left and right pointers meet
            while l < r:

                # If characters at both pointers are different, the given string is not a palindrome
                if s[l] != s[r]:
                    return False

                # Update both pointers
                l, r = l + 1, r - 1

            # Else, a given string is a palindrome
            return True

        # Find the length of a given string
        n = len(s)

        # Initialize the result
        res = []

        # Recursively partition a given string into multiple palindrome terms
        def backtrack(i, par):

            # If we used all characters in the string, we have found a valid partition
            if i == n:
                res.append(list(par))
                return

            # Find the next palindrome term
            for j in range(i + 1, n + 1):

                term = s[i:j]

                # If the current term is a palindrome, pick it and find the next term
                if isPalindrome(term):
                    par.append(term)
                    backtrack(j, par)
                    par.pop()

        backtrack(0, [])

        return res
