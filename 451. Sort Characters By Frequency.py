""" 
Problem:
    Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

    Return the sorted string. If there are multiple answers, return any of them.

    Example 1:
    Input: s = "tree"
    Output: "eert"
    Explanation: 'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
    
    Example 2:
    Input: s = "cccaaa"
    Output: "aaaccc"
    Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
    Note that "cacaca" is incorrect, as the same characters must be together.
    
    Example 3:
    Input: s = "Aabb"
    Output: "bbAa"
    Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.

Solution:
    Count all characters and their occurences. Then, sort all characters by their occurences in a descending order and build the result.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        # Count characters and initialize the result
        counts, res = Counter(s), ""

        # Build the result from sorted characters based on their occurences
        for c, count in sorted(counts.items(), key=lambda x: -x[1]):
            res += c * count

        return res
