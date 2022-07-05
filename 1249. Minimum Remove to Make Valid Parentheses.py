""" 
Problem:
    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
    
    Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
    
    Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"
    
    Example 3:
    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.

Solution:
    Iterate through all chracters. Use a stack to keep track of all opening parenthesis and a set to keep track of which index we are skipping. If we found an opening parenthesis, add it to the stack. Once, we found a closing parenthesis, we match it with an opening parenthesis and continue if there is an opening parenthesis. Else, we skip such parenthesis. Once, we iterated through all chracters, we will skip left over opening parentehsis. Finally, iterate all chracters and skip any characters that has been marked as skipped. 


Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Get the number of character
        N = len(s)

        # Initialize the stack and a set
        stack, skip = [], set()

        # Iterate through all chracters
        for i in range(N):

            # If we found an opening parenthesis
            if s[i] == "(":

                # Add it to the stack
                stack.append(i)

            # Elif, we found a closing parenthesis
            elif s[i] == ")":

                # If there is an opening parenthesis, match both of them.
                if stack:
                    stack.pop()

                # Else, mark such closing parenthesis as skipped
                else:
                    skip.add(i)

        # Mark all left over opening parenthesis as skipped
        skip.update(stack)

        # Form a new string without all skipped characters
        res = [s[i] for i in range(N) if i not in skip]

        return "".join(res)

