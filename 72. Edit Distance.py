""" 
Problem:
    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

    You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

    Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
    
    Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')

Solution:
    This is a classic dynamic programming problem. We will use a 2d-cache so that we can avoid repeating our previous works. The base case for this problem is when one or more words are empty and thus, the first row will be 0,1,...m-1 where m is the length of word2 and the first column will be 0,1,...,n-1 where n is the length of word1. Let up be the previous deletion operation, left be the previous insertion operation, and diagonal be the previous replacement operation. Other entries in the cache matrix can be fill by examine cells to its left, diagonal, and top and we pick the minimum + 1. Do note that if two characters are the same, we will perform any opertion and thus, we will default to the previous replacement opertion without adding 1. 

Complexity:
    Time: O(n*m) where n is the length of word1 and m is the length of word2.
    Space: O(n*m)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # Generate the cache matrix
        len1, len2 = len(word1) + 1, len(word2) + 1

        cache = [[0 for _ in range(len2)] for _ in range(len1)]

        # Create base case for empty words
        # This is case where word1 is empty or insertion only
        cache[0][:] = range(len2)

        # This is a case where word2 is empty or deletion only
        for n in range(len1):
            cache[n][0] = n

        # Fill in the remaining entries in the cache.
        for n in range(len1)[1:]:
            for m in range(len2)[1:]:

                # If it is the same characters, we will not do anything
                if word1[n - 1] == word2[m - 1]:
                    cache[n][m] = cache[n - 1][m - 1]

                # Else, we pick the minimum from previous steps and add one to it
                else:
                    cache[n][m] = 1 + min(
                        cache[n - 1][m], cache[n][m - 1], cache[n - 1][m - 1]
                    )

        return cache[len1 - 1][len2 - 1]
