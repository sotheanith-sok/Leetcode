"""
Problem:
    Given two strings s and t, return the number of distinct subsequences of s which equals t.

    A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

    The test cases are generated so that the answer fits on a 32-bit signed integer.

    Example 1:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation:
    As shown below, there are 3 ways you can generate "rabbit" from S.
    rabbbit
    rabbbit
    rabbbit
    
    Example 2:
    Input: s = "babgbag", t = "bag"
    Output: 5
    Explanation:
    As shown below, there are 5 ways you can generate "bag" from S.
    babgbag
    babgbag
    babgbag
    babgbag
    babgbag

Solution:
    Let i and j contain indices point to the last character of substrings started from 0 and end at such indices of s and t respectively. 
    
    If j points to an empty substring, we know that we can always form at least 1 subsequences regardless of where i is. 

        ie i = "abcde"  j=""
        You can always convert i to j by removing all characters
    
    However, if j points to a non-empty substring and i points to an empty substring, we know that it is impossible to form any subsequences. 

        ie. i = "", j="abc"
        You can never convert i to j by removing characters.
      
    These two will be our basecases.

    Then, for some arbitrary (i, j), the number of subsequences can be formed at such indices is the number of subsequences can be formed without using the last character of i  plus the number of subsequences can be formed by using the last character
        ie. seq(i, j) = seq(i-1, j) + seq(i-1, j-1) if s[i] == t[j] else 0 

    Ex. s = "babgbag", t = "bag"
            _   b   a   g
        _   1   0   0   0
        b   1   1   0   0
        a   1   1   1   0
        b   1   2   1   0
        g   1   2   1   1
        b   1   3   1   1
        a   1   3   4   1
        g   1   3   4   5


Complexity:
    Time: O(mn)
    Space: O(mn)
"""


# Top-down
from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # Recursively calculate the number of subsequences
        @lru_cache(None)
        def dp(i, j):

            # If j points to an empty string, return 1
            if j == 0:
                return 1

            # Else, if i points to an empty string, return 0
            if i == 0:
                return 0

            # Recursively calculate the number of subsequences leading to the current i and j
            return dp(i - 1, j) + (dp(i - 1, j - 1) if s[i - 1] == t[j - 1] else 0)

        return dp(len(s), len(t))


# Bottom-up
from itertools import product


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # Find the length of s and t
        m, n = len(s), len(t)

        # Initialize the cache
        cache = [[1] + [0 for _ in range(n)] for _ in range(m + 1)]

        # Fill the cache
        for i, j in product(range(m), range(n)):

            # Calculate the number of subsequences using previous calculations
            cache[i + 1][j + 1] = cache[i][j + 1] + (cache[i][j] if s[i] == t[j] else 0)

        return cache[m][n]

