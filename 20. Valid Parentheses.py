"""
Problem:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    
    Example 1:
    Input: s = "()"
    Output: true
    
    Example 2:
    Input: s = "()[]{}"
    Output: true
    
    Example 3:
    Input: s = "(]"
    Output: false

Solution:
    Iterate through all characters in s and add any opening parenthesis onto a stack. When we found a closing parenthesis, check if its corresponding opening parenthesis is on top of the stack. If yes, pop it and continue to the next character. Else, return False. Once we processed all characters, the stack should be empty if the string is valid. 

Complexity:
    Time: O(n)
    Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:

        # Initialize the stack to stores all opening parentheses
        stack = []

        # Bi-directional dictionaries to map opening and closing parentheses
        openP = {"(": ")", "[": "]", "{": "}"}
        closeP = {")": "(", "]": "[", "}": "{"}

        # Itearate through all characters in s
        for c in s:

            # If the current character is an opening parenthesis, add it to the stack
            if c in openP:
                stack.append(c)

            # Else if it is a closing parenthesis,
            else:

                # If the stack is empty or an opening parenthesis on top of the stack isn't a correct type, we can't pair such closing parenthesis and thus, return False
                if not stack or stack[-1] != closeP[c]:
                    return False

                # Else, pair the current closing parenthesis with an opening parenthesis on top of the stack
                stack.pop()

        # Return True if stack is empty aka we have paired all parentheses
        return not stack

