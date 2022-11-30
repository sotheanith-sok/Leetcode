""" 
Problem:
    Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

    Example 1:
    Input: arr = [1,2,2,1,1,3]
    Output: true
    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

    Example 2:
    Input: arr = [1,2]
    Output: false

    Example 3:
    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true

Solution:
    Count all characters and their occurences. Then, iterate through all occurences and use a set to keep track of previous occurences. Return False if the current occurence existed before. Else, return True.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        # Count all characters and initialize a set to keep track of previous occurences
        counts, existed = Counter(arr), set()

        # Iterate through all occurences
        for occurence in counts.values():

            # If the current occurence existed before, return False
            if occurence in existed:
                return False

            # Else, mark such occurence as existed
            existed.add(occurence)

        return True
