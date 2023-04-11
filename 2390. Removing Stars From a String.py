"""
Problem:
    You are given a string s, which contains stars *.

    In one operation, you can:

    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove the star itself.
    Return the string after all stars have been removed.

    Note:

    The input will be generated such that the operation is always possible.
    It can be shown that the resulting string will always be unique.
    

    Example 1:
    Input: s = "leet**cod*e"
    Output: "lecoe"
    Explanation: Performing the removals from left to right:
    - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
    - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
    - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
    There are no more stars, so we return "lecoe".
    
    Example 2:
    Input: s = "erase*****"
    Output: ""

Solution:
    Use a stack to maintain remaining characters. Everytime, we encounter a star character, we pop a character from the stack. Else, we append the character onto the stack.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def removeStars(self, s: str) -> str:

        # Initialize the stack
        stack = []

        # Iterate through all characters
        for c in s:

            # Remove a non-star character from the stack if we encounter a star character
            if c == "*":
                stack.pop()
                continue

            # Else, append a non-star character onto the stack
            stack.append(c)

        return "".join(stack)
