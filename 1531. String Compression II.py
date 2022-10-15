"""
Problem:
    Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

    Notice that in this problem, we are not adding '1' after single characters.

    Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

    Find the minimum length of the run-length encoded version of s after deleting at most k characters.

    Example 1:
    Input: s = "aaabcccd", k = 2
    Output: 4
    Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
    
    Example 2:
    Input: s = "aabbaa", k = 2
    Output: 2
    Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
    
    Example 3:
    Input: s = "aaaaaaaaaaa", k = 0
    Output: 3
    Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.

Solution:
    Instead of considering k as the number of removal, think of k as the number of characters we can skip when counting s. 

    Let counts(k, i, j, c) be the function that return the minimum length of the run-length encoded version of s given
    k: the number of skip remaining
    i: pointer to the current character
    j: pointer to the previously picked character 
    c: the count of previously picked character


    1. If s[i] == s[j], we always pick the current character and it will increase the minimum length 
    only when c is 1, 9, and 99.

    Note: we don't consider skipping the current character here because skipping it is the same as if we were to skip the previous character. Thus, the second case will take care of it.

    Ex: b -> a -> a -> a        b -> a -> a -> a
        ✓    ✓   ✗    ✓       ✓    ✗    ✓   ✓

        b -> a -> a -> a        b -> a -> a -> a
        ✓    ✓   ✗    ✗       ✓    ✗    ✗   ✓

    2. If s[i] != s[j], we have to consider the case where we pick the current character and the case where we skip the current character. Then, we just pick the one that give the minimum length.
    
Complexity:
    Time: O(n2**k) 
    Space: O(kn**2)
"""


from functools import lru_cache
from math import inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        # Get length of s
        n = len(s)

        # Return the minimum length of the run-length encoded version of s
        # k: the number of skip remaining
        # i: pointer to the current character
        # j: pointer to the previously picked character
        # c: the count of previously picked character
        @lru_cache(None)
        def counts(k, i, j, c):

            # If we skip more than allowed, return infinity
            if k < 0:
                return inf

            # If we reach the end of s, return 0
            if i >= n:
                return 0

            # If the current character is the same as the previously picked character, we pick it and increment the minimum length if the count of previously picked character is at 1, 9, or 99
            if 0 <= j < n and s[i] == s[j]:

                return int(c == 1 or c == 9 or c == 99) + counts(k, i + 1, i, c + 1)

            # Else, take the minimum between picking the current character or skipping the current character
            return min(1 + counts(k, i + 1, i, 1), counts(k - 1, i + 1, j, c))

        return counts(k, 0, -1, 0)

