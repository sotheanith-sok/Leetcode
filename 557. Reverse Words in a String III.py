"""
Problem:
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

    Example 1:
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    
    Example 2:
    Input: s = "God Ding"
    Output: "doG gniD"

Solution:
    Split string s into words using space as the seperator. Reverse each words and join them all back using space as the seperator. 

Complexity:
    Time: O(n) where n is length of s
    Space: O(n)
"""


class Solution:
    def reverseWords(self, s: str) -> str:

        # Split words based on spaces
        words = s.split(" ")

        # Reverse each word
        words = [word[::-1] for word in words]

        # Join words back together using spaces as the seperator
        return " ".join(words)
