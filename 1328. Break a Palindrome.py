"""
Problem:
    Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

    Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

    A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

    Example 1:
    Input: palindrome = "abccba"
    Output: "aaccba"
    Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
    Of all the ways, "aaccba" is the lexicographically smallest.
    
    Example 2:
    Input: palindrome = "a"
    Output: ""
    Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Solution:
    If palindrome has a length of 1, return "" because we can't replace any characters to break the palindrome. 
    
    Iterate through the first half (exclude middle if the length is odd) of the palindrome and check if there is a character that is lexicographically larger than 'a'. If yes, replace such character with 'a' and return the result. 
    
    Else, our palindrome must be consisted of all 'a'. Thus, replace the last character of the plaindrome with 'b' and return the result.

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        # Since we are working with a palindrome, we only have to check the first half
        n = len(palindrome) // 2

        # Iterate through all chracters
        for i in range(n):

            # If there is a character that is lexicographically larger than 'a', replace such character with 'a' and return the result
            if ord(palindrome[i]) > ord("a"):
                return palindrome[:i] + "a" + palindrome[i + 1 :]

        # Elif the length of plaindrome is greater than 1, return a resulting palindrome with last character replaced with 'b'
        # Else, return empty string
        return palindrome[:-1] + "b" if len(palindrome) > 1 else ""

