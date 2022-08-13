"""
Problem:
    You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

    You can return the answer in any order.

    Example 1:
    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
    The output order does not matter, returning [9,0] is fine too.
    
    Example 2:
    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    Output: []
    
    Example 3:
    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]

Solution:
   Iterate through s and check every possible substrings. For each substring, count all words and their counts. If the counter of the substring is equal to the counter of words, add the starting index to to the resulting list.     

Complexity:
    Time: O(mn) where m is the length of s and n is the length of words
    Space: O(n*wordLength)
"""


from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        # Find the length of s, words, and each word
        m, n, wordLength = len(s), len(words), len(words[0])

        # Count words
        words = Counter(words)

        # Count words in a substring
        def counts(sub):

            # Initialize the counter
            count = defaultdict(int)

            # Go through all words
            for i in range(0, n * wordLength, wordLength):
                
                word = sub[i : i + wordLength]

                # If such word exists, increment its count in the counter
                if word in words:
                    count[word] += 1

                # Else, this substring is invalid and thus, return empty counter
                else:
                    return {}

            # Return counter
            return count

        # Initialize the result
        res = []

        # Iterate through all possible substrings
        for i in range(0, m - n * wordLength + 1):

            # If counters of substring and words are equal, add the starting index to the result
            if counts(s[i : i + n * wordLength]) == words:
                res.append(i)

        return res

