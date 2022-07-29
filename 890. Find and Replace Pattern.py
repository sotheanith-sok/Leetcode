"""
Problem:
    Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

    A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

    Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

    Example 1:
    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
    "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
    
    Example 2:
    Input: words = ["a","b","c"], pattern = "a"
    Output: ["a","b","c"]

Solution:
    Iterate through all characters in a word and the pattern. If both characters are mapped to each other, we continue to the next character. Else, this word doesn't match the pattern and thus, continue to the next word. If we are able to map all characters in a word to the pattern, add the word to the result. 

Complexity:
    Time: O(n) where n is the number of characters of all words
    Space: O(n)
"""


class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:

        # Get the length of the pattern
        n = len(pattern)

        # Initialize the result
        res = []

        # Iterate through all word
        for word in words:

            # Initialize the bidirectional hashmap
            wordToPattern, patternToWord = {}, {}

            # Iterate through all characters
            for i in range(n):

                # If both characters havn't been mapped, map them together
                if pattern[i] not in patternToWord and word[i] not in wordToPattern:
                    patternToWord[pattern[i]] = word[i]
                    wordToPattern[word[i]] = pattern[i]

                # If there isn't a valid mapping for current characters, continue to the next word.
                if (
                    pattern[i] not in patternToWord
                    or word[i] not in wordToPattern
                    or patternToWord[pattern[i]] != word[i]
                    or wordToPattern[word[i]] != pattern[i]
                ):
                    break

                # If we processed the last character pairs, add the word to the result.
                if i == n - 1:
                    res.append(word)

        return res

