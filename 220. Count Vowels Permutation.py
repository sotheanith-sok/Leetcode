"""
Problem:
    Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    Each vowel 'a' may only be followed by an 'e'.
    Each vowel 'e' may only be followed by an 'a' or an 'i'.
    Each vowel 'i' may not be followed by another 'i'.
    Each vowel 'o' may only be followed by an 'i' or a 'u'.
    Each vowel 'u' may only be followed by an 'a'.
    Since the answer may be too large, return it modulo 10^9 + 7.

    Example 1:
    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
    
    Example 2:
    Input: n = 2
    Output: 10
    Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
    
    Example 3: 
    Input: n = 5
    Output: 68

Solution:
    Top-down dp:
    Reduce the problem down to its sub-problem until n is 1. Return 1 when n is 1. Then, sum up counts returned by all sub-problems.
    
    Bottom-up dp:
    Initialize the counts of all vowels to 1. Iterate from 1 to n and add up the counts of vowels based on previous vowels counts.


Complexity:
    Time: O(n)
    Space: O(n) for top-down and O(1) for bottom-up

"""

# Top-down dp solution
from functools import lru_cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:

        # A mapper mapped characters to their next characters
        mapper = {
            "": ["a", "e", "i", "o", "u"],
            "a": "e",
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }

        @lru_cache(None)
        def dp(n, c):

            # If n == 1, we have reach base case and thus, return 1
            if n == 1:
                return 1

            # Initialize the total to 0
            total = 0

            # Recursively solve sub-problems until n is reduced to 1
            for char in mapper[c]:
                total = (total + dp(n - 1, char)) % 1000000007

            return total

        # Add 1 to n since we started with empty string instead of recursively called dp on each vowel
        return dp(n + 1, "")


# Bottom-up dp solution
class Solution:
    def countVowelPermutation(self, n: int) -> int:

        # Initialize all vowels counts to 1
        # This is n==1 case
        a, e, i, o, u = 1, 1, 1, 1, 1

        # Iterate from 2 to n
        for _ in range(2, n+1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

        # Return the sum of all counts of all vowels
        return (a + e + i + o + u) % 1000000007
