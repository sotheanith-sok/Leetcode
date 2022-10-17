"""
Problem:
    A pangram is a sentence where every letter of the English alphabet appears at least once.

    Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

    Example 1:
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: true
    Explanation: sentence contains at least one of every letter of the English alphabet.
    
    Example 2:
    Input: sentence = "leetcode"
    Output: false

Solution:
    Put all characters of s into a set and return true if all letter of the English alphabets are in the set.

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
