""" 
Problem:
    We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
    Given a string word, return true if the usage of capitals in it is right.

    Example 1:
    Input: word = "USA"
    Output: true
    
    Example 2:
    Input: word = "FlaG"
    Output: false

Solution:
    Count the number of capitalized alphabets of a given word and check if such word much one of the three given conditions. 

    1. All letters in this word are capitals, like "USA".
        Count of capitalized alphabets is equal to the length of word

    2. All letters in this word are not capitals, like "leetcode".
        Count of capitalized alphabets is zero 

    3. Only the first letter in this word is capital, like "Google".
        Count of capitalized alphabets is one and such alphabet is the first character of the word

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # Find the length of the word and the count of capitalized alphabets
        n, capitals = len(word), sum(65 <= ord(c) <= 90 for c in word)

        # Check the three conditions
        return (
            capitals == n
            or capitals == 0
            or (65 <= ord(word[0]) <= 90 and capitals == 1)
        )
