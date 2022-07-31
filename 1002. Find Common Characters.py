""" 
Problem:
    Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

    Example 1:

    Input: words = ["bella","label","roller"]
    Output: ["e","l","l"]
    Example 2:

    Input: words = ["cool","lock","cook"]
    Output: ["c","o"]

Solution:
    For each character in the first word, check if such character is in other words. If yes, append the character into the result based on the smallest frequency of such character among all words. Return the result.

Complexity:
    Time: O(n * words) where n is the number of unique character in the first word 
    Space: O(c) where c is all chracters in all words

"""
from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        # If only one word is given,
        if len(words) == 1:

            # Return all character in such word
            return list(words[0])

        # Convert all words from list to counter
        for i in range(len(words)):
            words[i] = Counter(words[i])

        # Initialie result
        res = []

        # For each character in the first word
        for c in words[0]:

            # Count how many time such character appeared in each word.
            count = [word[c] if c in word else 0 for word in words]

            # If there exists a word that doesn't contain such character, continue to the next character
            if 0 in count:
                continue

            # Append the chracter based on its smallest frequency among all words into the res
            res += [c] * min(count)

        return res

