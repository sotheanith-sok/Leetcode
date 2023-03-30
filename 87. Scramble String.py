"""
Problem:
    We can scramble a string s to get a string t using the following algorithm:

    If the length of the string is 1, stop.
    If the length of the string is > 1, do the following:
    Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
    Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
    Apply step 1 recursively on each of the two substrings x and y.
    Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

    Example 1:
    Input: s1 = "great", s2 = "rgeat"
    Output: true
    Explanation: One possible scenario applied on s1 is:
    "great" --> "gr/eat" // divide at random index.
    "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
    "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
    "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
    "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
    "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
    The algorithm stops now, and the result string is "rgeat" which is s2.
    As one possible scenario led s1 to be scrambled to s2, we return true.
    
    Example 2:
    Input: s1 = "abcde", s2 = "caebd"
    Output: false
    
    Example 3:
    Input: s1 = "a", s2 = "a"
    Output: true

Solution:
    Split word2 into two partitions multiple times until we found a path of scrambling to turn such word into word1.

Complexity:
    Time: O(n^n)
    Space: O(n**2)
"""

from collections import Counter
from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        # Check if we can transform word2 to word1 by scrambling word2
        @lru_cache(None)
        def backtrack(word1, word2):

            # Get the length of both words
            n = len(word1)

            # If both words contain 1 character, compare them
            if n == 1:
                return word1 == word2

            # Else,
            # Split word1 into two partitions where all characters start in the right partition
            s1_left, s1_right = Counter(), Counter(word1)

            # Split word2 into two partitions where all characters start in the right partition
            s2_left_1, s2_right_1 = Counter(), Counter(word2)

            # Split word2 into two partitions where all characters start in the left partition
            s2_left_2, s2_right_2 = Counter(word2), Counter()

            # Start distributing each character
            for i in range(n - 1):

                # Move the current character of word1 from the right partition into the left partition
                s1_left[word1[i]] += 1
                s1_right[word1[i]] -= 1

                # Move the current character of word2 from the right partiton into the left parition
                s2_left_1[word2[i]] += 1
                s2_right_1[word2[i]] -= 1

                # Move the current character of word2 from the left partition into the right partition
                s2_left_2[word2[n - i - 1]] -= 1
                s2_right_2[word2[n - i - 1]] += 1

                # Return True if same order partition result in word2 be scrambled into word1
                if (
                    s1_left == s2_left_1
                    and s1_right == s2_right_1
                    and backtrack(word1[: i + 1], word2[: i + 1])
                    and backtrack(word1[i + 1 :], word2[i + 1 :])
                ):
                    return True

                # Return True if swapping partition result in word2 be scrabled into word1
                if (
                    s1_left == s2_right_2
                    and s1_right == s2_left_2
                    and backtrack(word1[: i + 1], word2[n - i - 1 :])
                    and backtrack(word1[i + 1 :], word2[: n - i - 1])
                ):
                    return True

            return False

        return backtrack(s1, s2)
