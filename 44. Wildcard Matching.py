"""
Problem:
    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).

    Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    
    Example 2:
    Input: s = "aa", p = "*"
    Output: true
    Explanation: '*' matches any sequence.
    
    Example 3:
    Input: s = "cb", p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Solution:
    Solve this problem using backtracking. Let i and j be the current index of s and p. Let m and n be the length of s and p. 

    If i == m and j == n, we are able to match s to p.

    If i == m and j < n, check if the current character of p is a "*". If yes, match such character with an empty string.

    If i < m and j < n,
        If current characters at s and p is the same or the current character at p is "?", match the pair and increment i and j

        Else if the current character of p is "*", we need to check three cases:
            (i, j+1) : match "*" to an empty string
            (i+1, j) : match "*" to more than one character
            (i+1, j+1) : match "*" to a single character
    
    Else, return False

Complexity:
    Time: O(mn)
    Space: O(mn)
"""


# Top-down
from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Get lengths of s and p
        m, n = len(s), len(p)

        @lru_cache(None)
        def backtrack(i, j):

            # This is the base case and s can be matched to p
            if i == m and j == n:
                return True

            # If we reach the end of s and there is a next character of p
            if i == m and j < n:

                # Check if the next character is a "*"
                # If yes, match it with the empty string
                if p[j] == "*" and backtrack(i, j + 1):
                    return True

            # If we haven't reach the end of both s and p
            if i < m and j < n:

                # If the current character of p and s can be matched, pair them
                if p[j] == "?" or s[i] == p[j]:
                    return backtrack(i + 1, j + 1)

                # If the current character of p is a "*"
                if p[j] == "*":

                    # Check the three possible routes
                    # (i, j+1) : match "*" to an empty string
                    # (i+1, j) : match "*" to more than one character
                    # (i+1, j+1) : match "*" to a single character
                    if (
                        backtrack(i + 1, j)
                        or backtrack(i, j + 1)
                        or backtrack(i + 1, j + 1)
                    ):
                        return True

            # Return false if we can't satisfy above conditions
            return False

        return backtrack(0, 0)


# Bottom-up
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Get lengths of s and p
        m, n = len(s), len(p)

        # Initialize the cache
        cache = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        # 0th index will represent an empty string
        # Thus, empty string s can be match with empty string p
        cache[0][0] = True

        # Update the first row or when s is empty
        # A character in the pattern can only be match with an empty s if it is a "*" and the previous character is also matchable with an empty s
        for j in range(n):
            cache[0][j + 1] = p[j] == "*" and cache[0][j]

        # Iterate through all combinations
        for i in range(m):
            for j in range(n):

                # If characters at i and j can be pair, check there is a route leading up to the current character
                if s[i] == p[j] or p[j] == "?":
                    cache[i + 1][j + 1] = True and cache[i][j]

                # If the current character at j is a "*",
                # Check if there is a round that lead up to the current character
                # (i, j-1) : match "*" to an empty string
                # (i-1, j) : match "*" to more than one character
                # (i-1, j-1) : match "*" to a single character
                if p[j] == "*":
                    cache[i + 1][j + 1] = (
                        cache[i + 1][j] or cache[i][j + 1] or cache[i][j]
                    )

        return cache[m][n]
