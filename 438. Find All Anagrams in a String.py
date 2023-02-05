"""
Problem:
    Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    
    Example 2:
    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".

Solution:
    Maintain a sliding window of size equal to the p string. Slide the window over the s string and find all substrings that have the same characters and frequencies. 

Complexity:
    Time: O(m + n) where m and n are lengths of s and p strings respectively
    Space: O(1)
"""

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        # Find legnths of both strings
        m, n = len(s), len(p)

        # Initialize the counter for the sliding window and the anagram
        counts, anagram = Counter(), Counter(p)

        # Initialize the left and right pointers of the sliding window
        l, r = 0, 0

        # Initialize the result
        res = []

        # Expand the sliding window until it reaches the end of the s string
        while r < m:

            # If the size of the sliding window is larger than the p string, reduce its size
            if r - l >= n:
                counts[s[l]], l = counts[s[l]] - 1, l + 1
                continue

            # Add the latest character into the counter of the sliding window
            counts[s[r]] += 1

            # Compare the sliding window counter to the anagram counter
            if counts == anagram:
                res.append(l)

            # Increment the right pointer
            r += 1

        return res
