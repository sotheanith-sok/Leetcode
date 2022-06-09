""" 
Problem:
    The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.
    When studying DNA, it is useful to identify repeated sequences within the DNA.

    Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

    Example 1:

    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]
    Example 2:

    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]


Solution:
    Use a hashmap to keep tracks of unique sequences and their counts. If count of a sequence is equal 2, add it the result list. Iterate through all possible sequences using sliding windows.

Complexity:
    Time: O(n)
    Space: O(n)

"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:

        # Length of the dna.
        N = len(s)

        # Map 10 digits sequences to their counts.
        map = {}

        # The result list.
        res = []

        # Iterate through all sequences.
        for i in range(0, N - 10 + 1):
            seq = s[i : i + 10]

            # Update the sequence's count in the map.
            map[seq] = map[seq] + 1 if seq in map else 1

            # The count reachs 2, add it to the result.
            if map[seq] == 2:
                res.append(seq)

        return res

