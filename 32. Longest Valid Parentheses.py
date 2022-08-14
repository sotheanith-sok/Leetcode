"""
Problem:
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    Example 1:
    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".
    
    Example 2:
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".
    
    Example 3:
    Input: s = ""
    Output: 0

Solution:
    Using a stack, iterate through all characters in s and pair opening parentheeses with closing parentheses and store pairs in a dictionary. Then, iterate through all pairs of parentheses and merge adjacent pairs together. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # Initialize a dict to map open parenthesis with closing parethesis
        pairs = {}

        # A stack to keep track of unpair open parenthesis
        stack = []

        # Iterate through all characters in s
        for i, p in enumerate(s):

            # If we see an opening parenthesis, add it to the stack
            if p == "(":
                stack.append(i)

            # Else, if we see a closing parethesis, pair it with an opening parenthesis if there is one
            elif stack:

                # Save the pair to the dictionary
                pairs[stack.pop()] = i

        # Initialize the result
        res = 0

        # Iterate through all characters
        for i, _ in enumerate(s):

            # If there isn't a pair of parentheses at the current index, continue to the next one
            if i not in pairs:
                continue

            # Merge the current pair of parentheses with its adjacent pairs
            while pairs[i] + 1 in pairs:
                pairs[i] = pairs.pop(pairs[i] + 1)

            # Find the distance of merged parentheses
            res = max(res, pairs[i] - i + 1)

        return res

