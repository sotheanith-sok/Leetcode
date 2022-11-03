""" 
Problem:
    You are given an array of strings words. Each element of words consists of two lowercase English letters.

    Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

    Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

    A palindrome is a string that reads the same forward and backward.

    Example 1:
    Input: words = ["lc","cl","gg"]
    Output: 6
    Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
    Note that "clgglc" is another longest palindrome that can be created.
    
    Example 2:
    Input: words = ["ab","ty","yt","lc","cl","ab"]
    Output: 8
    Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
    Note that "lcyttycl" is another longest palindrome that can be created.
    
    Example 3:
    Input: words = ["cc","ll","xx"]
    Output: 2
    Explanation: One longest palindrome is "cc", of length 2.
    Note that "ll" is another longest palindrome that can be created, and so is "xx".

Solution:
    Try to pair all occurence of a word with all occruence of the reversed of such word. There are two cases to consider.
    1. If word != reversed(word), the resulted pairs are equal to the minimum occurrence between both words.
    2. If word == reversed(word), the resulted pairs are equal to the occurrence of word divided by 2.
    Additional, an occurence of such case can be use as the center too.


Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:

        # Count words and their occurence
        counts = Counter(words)

        # Initialize a result and a variable keep track of the center
        res, center = 0, False

        # Iterate through all words
        for word in counts:

            # Find its reversed
            rWord = word[::-1]

            # If there isn't a reversed word, skip the current word
            if rWord not in counts:
                continue

            # Calculate the number of pars
            pairs = (
                min(counts[word], counts[rWord]) if word != rWord else counts[word] // 2
            )

            # Update the result
            res += 4 * pairs

            # Decrement the count of both words
            counts[word] -= pairs
            counts[rWord] -= pairs

            # Check if the current word can be used as the center
            if not center and word == rWord and counts[word] == 1:
                center = True
                counts[word] -= 1

        # Return the result
        return res + (2 if center else 0)
