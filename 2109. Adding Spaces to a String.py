"""
Problem:
    You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

    For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
    Return the modified string after the spaces have been added.

    Example 1:
    Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
    Output: "Leetcode Helps Me Learn"
    Explanation: 
    The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
    We then place spaces before those characters.
    
    Example 2:
    Input: s = "icodeinpython", spaces = [1,5,7,9]
    Output: "i code in py thon"
    Explanation:
    The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
    We then place spaces before those characters.
    
    Example 3:
    Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
    Output: " s p a c i n g"
    Explanation:
    We are also able to place spaces before the first character of the string.

Solution:
    Let m, n be the length of s and spaces respectively. If we do spaces insertion into s, it would require O(mn). A better apporach would be to append each character at the end of a list and add extra space when we require one. This would require O(m+2n) running time.

Complexity:
    Time: O(max(m,n))
    Space: O(m+n)
"""


class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:

        # Convert a list of spaces to a set for O(1) checking
        spaces = set(spaces)

        # Initialize the result
        res = []

        # Iterate through all characters
        for i, c in enumerate(s):

            # If the current index requires a space, append one
            if i in spaces:
                res.append(" ")

            # Append the current character to the result
            res.append(c)

        # Convert result to a string
        return "".join(res)
