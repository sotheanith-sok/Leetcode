"""
Problem:
    Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".
    
    Example 1:
    Input: s = "abcde", words = ["a","bb","acd","ace"]
    Output: 3
    Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
    
    Example 2:
    Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    Output: 2

Solution:
    Similar solution to https://leetcode.com/problems/number-of-matching-subsequences/discuss/329381/Python-Solution-With-Detailed-Explanation.

    Use a hashmap to map words' prefix to words. Use deque to avoid string slicing. Start by convert all words into deque of characters and store those words in a hashmap based on their first character. Then, iterate through all characters in s. At each character, check if there exists words that start with that character. If yes, iterate through all words, pop their first character, and move them to their new hashmap location based on their new first character. If a word is empty, increment the result.  

Complexity:
    Time: O(mn) where m is the length of s and n is the length of words.
    Space: O(k) where k is the number of characters in all words
"""


from collections import defaultdict, deque


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:

        # Initialize pointers that map chracter to a deque of words
        pointers = defaultdict(deque)

        # Convert all words to deque of characters and add them the pointers based on their first chracter
        for word in words:
            pointers[word[0]].append(deque(word))

        # Initialzie the result
        res = 0

        # Iterate through all characters of s
        for c in s:

            # Find how many words that start with the current chracter
            i = len(pointers[c])

            # Iterate through those words
            for _ in range(i):

                # Pop a word from the left
                word = pointers[c].popleft()

                # Remove the first character from the word
                word.popleft()

                # If the word is empty, increment result
                if len(word) == 0:
                    res += 1
                    continue

                # Else, add the word back into the hashmap based on the new first character.
                pointers[word[0]].append(word)

        return res

