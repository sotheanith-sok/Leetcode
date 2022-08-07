"""
Problem:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    Example 2:

    Input: n = 1
    Output: ["()"]

Solution:
    Recursively add closing and opening parentheses to the partial result until we have added n parentheses for both cases. Only add a closing parenthesis if there is at least 1 opening parenthesis. 

Complexity:
    Time: O(2**n)
    Space: O(2**n)
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        # Initialize the result
        res = []

        # Recursively go through all possible combinations
        def add(open, close, partialRes):

            nonlocal res

            # If we have added opening and closing parentheses n times, we reaches a solution
            if open == close == n:
                res.append("".join(partialRes))
                return

            # Add a closing parenthesis to the partial result if we have at least 1 opening parenthesis
            if close < open:
                add(open, close + 1, partialRes + [")"])

            # Add an opening parenthesis to the partial result if we haven't added n parenthesis yet
            if open < n:
                add(open + 1, close, partialRes + ["("])

        add(0, 0, [])

        return res
