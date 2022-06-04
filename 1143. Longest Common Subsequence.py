""" 
Problem:
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.


    Example 1:

    Input: text1 = "abcde", text2 = "ace" 
    Output: 3  
    Explanation: The longest common subsequence is "ace" and its length is 3.
    Example 2:

    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.
    Example 3:

    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.


Solution (Dynamic Programming):
    We will use a cache matrix of size m + 1 x n + 1 where m is the length of text1 and n is the length of text2. The base case is when text1 or text2 is empty. Thus, first row and coloumn will be zero. There are two cases to consider. When text1[m] == text2[n], we knows that the common subsequence is increasing by 1. Thus, we take a previous value diagonal to it and add one to it (it will propagate to all values to the bottom-right of it). Else, we just take the max of the value above and left of the current entry.

    Ex: Diagonal = "a, f" and "a, c" and text1[m] == text2[n] == "b" => we take the diagonal and add one to it.
        Left = "a, f" and "a, c, b and text[m] == "i" != text[n] == "b" => we take the max of left and top.
        Top = "a, f, i" and "a, c" and text[m] == "i" != text[n] == "b" => we take the max of left and top.

Complexity:
    Time: O(m * n)
    Space: O(m * n)

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Get length of text1 and text2
        m = len(text1) + 1
        n = len(text2) + 1

        # Create cache to stores sub problems
        cache = [[0 for _ in range(n)] for _ in range(m)]

        # Fill in the cache
        for i in range(m)[1:]:
            for j in range(n)[1:]:
                cache[i][j] = (
                    cache[i - 1][j - 1]
                    + 1  # Look diagonal and add one if text1[m] == text2[n]
                    if text1[i - 1] == text2[j - 1]
                    else max(
                        cache[i - 1][j], cache[i][j - 1]
                    )  # max of top and left entry
                )

        return cache[-1][-1]


