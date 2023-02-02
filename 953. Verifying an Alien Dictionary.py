"""
Problem:
    In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

    Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
    
    Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
    
    Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Solution:
    Compare each word to its predecessor based on the order of alphabets given. 
    
    To compare an arbitrary pair of words, we will start by comparing their leading charaters. We can determine the order of both words here if there is a pair of characters with a different position in the order of given alphabets. Else, we will determine the order based on words' lengths.       

Complexity:
    Time: O(mn) where is m is the length of the longest word and n is the number of words
    Space: O(1)
"""


class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        # Find the number of words
        n = len(words)

        # Create a dict of quick look up of characters and their positions
        pos = {c: i for i, c in enumerate(order)}

        # Compare two words
        def ordered(word1, word2):

            # Compare leading characters of both words
            for c1, c2 in zip(word1, word2):

                # If both characters are the same position, continue
                if pos[c1] == pos[c2]:
                    continue

                # Else, we can determine the order of both words
                return True if pos[c1] < pos[c2] else False

            # If leading characters are equal, determine the order of both words based on their lengths
            return True if len(word1) <= len(word2) else False

        # Compare a word with its predecessor
        for i in range(1, n):

            # If two words are out of order, return False
            if not ordered(words[i - 1], words[i]):
                return False

        return True
