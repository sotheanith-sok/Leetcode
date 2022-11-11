""" 
Problem:
    You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

    We repeatedly make duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

    Example 1:
    Input: s = "abbaca"
    Output: "ca"
    Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
    
    Example 2:
    Input: s = "azxxzy"
    Output: "ay"

Solution:
    Use a stack to store all good characters. A character on top of the stack is no longer good if it is equal to the current character. Return all good characters.

Complexity:
    Time: O(n)
    Space: O(n)
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:

        # Initialize the stack
        stack = []

        # Iterate through all characters
        for c in s:

            # Check if the character on top of the stack is good
            if stack and stack[-1]==c:
                stack.pop()
                continue

            # Append the current character on top of the stack
            stack.append(c)

        return ''.join(stack)