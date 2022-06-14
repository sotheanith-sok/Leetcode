""" 
Problem:
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

    Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
    
    Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false
    
    Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false

Solution:
    We will solve this problem by keeping track of unique pairs of a character and a word. To ensure that a char can only map to a word, we will use two hashmaps to simulate a bidirectional mapping. To start, we will splits words into a list of word. Then, we will will iterate through all characters in the pattern. If the current character isn't mapped to the current word or the current word isn't mapped to the current character, we return False. Else, we map the current character to the current word and repeat the process. Return true after the loop.   

Complexity:
    Time: O(n)
    Space: O(n)

"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Split the words into a list of words
        s = s.split()

        # Two map: char to word and word to char
        char_to_word = {}
        word_to_char = {}

        # Edge case: if the len is different, we can't match the pattern.
        if len(pattern) != len(s):
            return False

        # Iterate through all characters
        for i, c in enumerate(pattern):

            # If the current character isn't mapped to the current word or the current word isn't mapped to the current character, return False.
            if (c in char_to_word and char_to_word[c] != s[i]) or (
                s[i] in word_to_char and word_to_char[s[i]] != c
            ):
                return False

            # Else, map them.
            char_to_word[c], word_to_char[s[i]] = s[i], c

        return True
