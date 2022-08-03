"""
Problem:
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    
    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Solution:
    Use the first word as the target. Iterate through all characters in the target and compare such character to all characters in other words at such index. If they are all the same, continue to the next character. Else, return the substring of the target up to such index.  

Complexity:
    Time: O(mn) where m is the length of the shortest word and n is the number of words
    Space: O(1)
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Save the first word as the target
        target = strs[0]

        # Iterate through all characters in target
        for i, c in enumerate(target):

            # If all characters at the current index is the same, continue to the next index
            if all(i < len(word) and c == word[i] for word in strs):
                continue

            # Else, return all characters up to such index
            return target[:i]

        return target
