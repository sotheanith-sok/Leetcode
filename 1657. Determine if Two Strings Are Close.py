""" 
Problem:
    Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
    For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
    You can use the operations on either string as many times as necessary.

    Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

    Example 1:
    Input: word1 = "abc", word2 = "bca"
    Output: true
    Explanation: You can attain word2 from word1 in 2 operations.
    Apply Operation 1: "abc" -> "acb"
    Apply Operation 1: "acb" -> "bca"
    
    Example 2:
    Input: word1 = "a", word2 = "aa"
    Output: false
    Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
    
    Example 3:
    Input: word1 = "cabbba", word2 = "abbccc"
    Output: true
    Explanation: You can attain word2 from word1 in 3 operations.
    Apply Operation 1: "cabbba" -> "caabbb"
    Apply Operation 2: "caabbb" -> "baaccc"
    Apply Operation 2: "baaccc" -> "abbccc"

Solution:
    Check if both words have the same characters and the same occurences of characters independent of actual characters.  

Complexity:
    Time: O(n)
    Space: O(n)
"""
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # Count characters and their occurences in both words
        count1, count2 = Counter(word1), Counter(word2)

        # Check if both words have the same characters and occurences (independent of characters)
        return sorted(count1.keys()) == sorted(count2.keys()) and sorted(count1.values()) == sorted(count2.values())
        