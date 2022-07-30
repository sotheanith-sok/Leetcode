"""
Problem:
    You are given two string arrays words1 and words2.

    A string b is a subset of string a if every letter in b occurs in a including multiplicity.

    For example, "wrr" is a subset of "warrior" but is not a subset of "world".
    A string a from words1 is universal if for every string b in words2, b is a subset of a.

    Return an array of all the universal strings in words1. You may return the answer in any order.

    Example 1:
    Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
    Output: ["facebook","google","leetcode"]
    
    Example 2:
    Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
    Output: ["apple","google","leetcode"]

Solution:
    Instead of counting and comparing each pairs of words in words1 and words2, we can merge all words in words2 into a single counter. This counter will contain the maximum occurence of a character among all words in words2. 

    The intuition behind this is that if a word has 5 x "a" and another word has 10 x "a" and there is a word that contain at least 10 x "a", then such word is the universal string.  

    Then, iterate through all words in words1 and check if it has all characters and at least corresponding occruence of such characters in the counter2. If yes, add such word to the result.     

Complexity:
    Time: O(n*c) where n is the number of words in words1 and c is the number of unique characters among all words in words2 
    Space: O(c)
"""

from collections import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:

        # Merge all words in words2 into a single counter
        counter2 = {}

        # Iterate through all words in words2
        for word in words2:

            # Count its characters
            for c, count in Counter(word).items():

                # Store the maximum occurence for each character among all words
                counter2[c] = max(count, counter2[c]) if c in counter2 else count

        # Initialize the result
        res = []

        # Iterate through all words in words1
        for word in words1:

            # Count its characters
            counter1 = Counter(word)

            # If such word contains all characters and at least corresponding occruence of such characters in the counter2, add it to the result
            if all(
                [
                    char in counter1 and counter1[char] >= count
                    for char, count in counter2.items()
                ]
            ):
                res.append(word)

        return res

