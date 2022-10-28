""" 
Problem:
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    Example 2:
    Input: strs = [""]
    Output: [[""]]
    
    Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Solution:
    Group all strings based on its characters and their counts. I used 'char1, count1, char2, count2,...' as the key in this case. 

Complexity: 
    Time: O(n)
    Space: O(n)
"""

from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Initialize a dict to store all groups
        groups = defaultdict(list)

        # Iterate through all strings
        for s in strs:

            # Count all characters
            counts = Counter(s)

            # Form the key
            key = "".join(c + str(counts[c]) for c in sorted(counts))

            # Add the string into a group
            groups[key].append(s)

        return list(groups.values())
