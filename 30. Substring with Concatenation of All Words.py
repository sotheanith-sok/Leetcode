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

   We can optimize the counter calculation by performing some lookback. A counter at some arbitrary i is the counter at i-w removed the first word of i-w and added the last word of i where w is the length of each word. 
   ie: words = 1,2,3,4,5 and numWord = 3
   counter(0) = [1,2,3]
   counter(1) = [2,3,4]
   counter(3) = [3,4,5]

   However, since each counter represents words of size w, we have to maintain at most w counters to account for all possible starting characters.


   Ex: s = "barfoothefoobarman", words = ["foo","bar"]
    i   substring   counterNum  counter                 result
    0   barfoo      0           {'bar': 1, 'foo': 1}    [0]
    1   arfoot      1           {'arf': 1, 'oot': 1}    [0]
    2   rfooth      2           {'rfo': 1, 'oth': 1}    [0]
    3   foothe      0           {'foo': 1, 'the': 1}    [0]
    4   oothef      1           {'oot': 1, 'hef': 1}    [0]
    5   othefo      2           {'oth': 1, 'efo': 1}    [0]
    6   thefoo      0           {'the': 1, 'foo': 1}    [0]
    7   hefoob      1           {'hef': 1, 'oob': 1}    [0]
    8   efooba      2           {'efo': 1, 'oba': 1}    [0]
    9   foobar      0           {'foo': 1, 'bar': 1}    [0,9]
    10  oobarm      1           {'oob': 1, 'arm': 1}    [0,9]
    11  obarma      2           {'oba': 1, 'rma': 1}    [0,9]
    12  barman      0           {'bar': 1, 'man': 1}    [0,9]

    Special thank to this [post](https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/1753357/Clear-solution!-Easy-to-understand-with-diagrams%5C) for the counter lookback.

Complexity:
    Time: O(mn) where m is the length of s and n is the length of words
    Space: O(nw) where n is the length of words and w is the length of each word
"""


from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        # Find the length of s, words, and each word
        m, n, w = len(s), len(words), len(words[0])

        # Count words
        words = Counter(words)

        # Cache to store previously calculated counter
        cache = {}

        # Count words in a substring
        def counts(i):

            # Initialize the counter
            counter = defaultdict(int) if 0 <= i < w else cache[i % w]

            # Calcualte the start and end of the current substring
            start, end = i, i + n * w

            # We have to do a full counter calculation for the first w characters
            if 0 <= i < w:
                for j in range(start, end, w):
                    counter[s[j : j + w]] += 1

            # Else, we can reused i-w counter
            else:

                # Remove the first word of i-w substring from the counter

                # First word of i-w substring
                firstWordPrevCounter = s[start - w : start]

                # Remove the first word of the i-w substring from the counter
                counter[firstWordPrevCounter] -= 1

                # Remove the word if its count is 0
                if counter[firstWordPrevCounter] == 0:
                    counter.pop(firstWordPrevCounter)

                # Add the last word of i substring
                
                # Lastword of i substring
                lastWord = s[end - w : end]

                # Add such word to the counter
                counter[lastWord] += 1

            # Save the counter to cache
            cache[i % w] = counter

            # Return the counter
            return cache[i % w]

        # Initialize the result
        res = []

        # Iterate through all possible substrings
        for i in range(0, m - n * w + 1):

            # If counters of substring and words are equal, add the starting index to the result
            if counts(i) == words:
                res.append(i)

        return res
