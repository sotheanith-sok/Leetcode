""" 
Problem:
    A string s is called good if there are no two different characters in s that have the same frequency.

    Given a string s, return the minimum number of characters you need to delete to make s good.

    The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

    Example 1:
    Input: s = "aab"
    Output: 0
    Explanation: s is already good.
    
    Example 2:
    Input: s = "aaabbbcc"
    Output: 2
    Explanation: You can delete two 'b's resulting in the good string "aaabcc".
    Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
    
    Example 3:
    Input: s = "ceabaacb"
    Output: 2
    Explanation: You can delete both 'c's resulting in the good string "eabaab".
    Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Solution:
    Count frequencies of all characters. For each frequency, check if it exists previously. If yes, decrement the frequency and increment the res and check again until we found a non existed frequency or it reach 0. Then, we mark the frequency as existed and continue to the next frequency. 

Complexity:
    Time: O(n)
    Space: O(1) because there exists at most 26 characters. 
"""

from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        # Count characters and their frequencies
        counts = Counter(s)

        # Create a set to check for existing frequency and a res
        exist, res = set(), 0

        # Iterate through all frequency
        for freq in counts.values():

            # While this frequency exists previously and it hasn't reach 0
            while freq > 0 and freq in exist:

                # Decrement the frequency and increment the res
                freq, res = freq - 1, res + 1

            # Mark the frequency as exist
            exist.add(freq)

        return res

