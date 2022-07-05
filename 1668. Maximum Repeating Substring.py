""" 
Problem:
    For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

    Given strings sequence and word, return the maximum k-repeating value of word in sequence.

    Example 1:
    Input: sequence = "ababc", word = "ab"
    Output: 2
    Explanation: "abab" is a substring in "ababc".
    
    Example 2:
    Input: sequence = "ababc", word = "ba"
    Output: 1
    Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
    
    Example 3:
    Input: sequence = "ababc", word = "ac"
    Output: 0
    Explanation: "ac" is not a substring in "ababc". 

Solution:
    The question asks us to find k where k is the largest multiple of a word concanated together that exists in the sequence. We will start by determine the largest k possible. Then, we form a target which is a multiple concatenation of the word from k times to 0 times. If the target exists in the string, return k. At k = 0, it will always true as an empty string is always a part of the other string.

Complexity:
    Time: O(kn) where k is the longest multiple of the work that result in the longest substring and n is the length of the sequence. 
    Space: O(1)
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        # Find the largest k
        k = len(sequence) // len(word)

        # Search from k until 0
        while True:

            # If k multiple of a word concatenated together exists in the sequence, return k
            if word * k in sequence:
                return k

            # Decrement k
            k -= 1

