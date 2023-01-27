"""
Problem:
    Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

    A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

    Example 1:
    Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
    "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
    
    Example 2:
    Input: words = ["cat","dog","catdog"]
    Output: ["catdog"]

Solution:
    Solve this problem using dynamic programing. Let dp be the function that return the largest number of words concatenated together to form a given word. At each iteration, split a word into prefix and suffix. Then, we will check if a prefix is one of the possible words. If yes, we will continue to check the remaining suffix at the next iteartion. Once we are able to reach the end of a word, we return 0. Else, we return -inf. 

Complexity:
    Time: O(n**2)
    Space: O(n**2)
"""


from functools import lru_cache
from math import inf


class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:

        # Get all possible lengths of words
        lengths = set(len(word) for word in words)

        # Convert a list of words into a set for O(1) checking
        words = set(words)

        # Find the largest number of words concatenated together to form a given word
        @lru_cache(None)
        def dp(word):

            # Return 0 if we reach the end of a word
            if not word:
                return 0

            # Initialize the number of words that can be concatenated together to form the current word
            count = -inf

            # Iterate through all possible lengths of a prefix
            for length in lengths:

                # If the length of the prefix is greater than the length of the current word, skip it
                if length > len(word):
                    continue

                # Split a word into prefix and suffix
                prefix, suffix = word[:length], word[length:]

                # If a prefix is one of the possible words
                if prefix in words:

                    # Check the remaining suffix
                    count = max(count, 1 + dp(suffix))

            return count

        return [word for word in words if dp(word) >= 2]
