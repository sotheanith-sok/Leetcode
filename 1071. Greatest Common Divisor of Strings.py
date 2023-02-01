"""
Problem:
    For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

    Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"
    
    Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"
    
    Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Solution:
    There must be a common string that is divisible by str1 and str2 if the concatenation of both strings (both ways) are equal to each other. Then, we can find such string by finding a GCD of both strings using their lengths.

    Example:
    str1        str2        GCD     res
    ABABABAB    AB          2       AB
    ABABABAB    ABAB        4       ABAB
    ABABABAB    ABABAB      2       AB
    ABABABAB    ABABABAB    8       ABABABAB



Complexity:
    Time:
    Space:
"""


from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Get lengths of both strings
        m, n = len(str1), len(str2)

        # Return the largest string that is divisible by both strings
        return str1[: gcd(m, n)] if str1 + str2 == str2 + str1 else ""
