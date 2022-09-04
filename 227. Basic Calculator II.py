"""
Problem:
    Given a string s which represents an expression, evaluate this expression and return its value. 

    The integer division should truncate toward zero.

    You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

    Example 1:
    Input: s = "3+2*2"
    Output: 7
    
    Example 2:
    Input: s = " 3/2 "
    Output: 1
    
    Example 3:
    Input: s = " 3+5 / 2 "
    Output: 5

Solution:
    Use a stack to maintain all operands. Initialize the current operator and operand to "+" and 0 respectively. Then, iterate through all characters in s. If a character is a number, append it to the current operand. Else, if a character is an operator, append the current operand into the stack based on the current operator. Update the current operand and operator. 

    1. If operator == "+", add operand to the stack
    2. If operator == "-", add negative operand to the stack
    3. If operator == "**, pop an operand from the stack, multiply it with the current operand, and add the result to the stack.
    4. If operator == "/", pop an operand from the stack, divide it with the current operand, and add the result to the stack.

    Finally, sum up all operands in the stack for the finaly result. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def calculate(self, s: str) -> int:

        # Initialize the stack
        stack = []

        # Append an operand onto the stack based on an operator
        def append(operator, operand):
            if operator == "+":
                stack.append(operand)
            elif operator == "-":
                stack.append(-operand)
            elif operator == "*":
                stack.append(stack.pop() * operand)
            else:
                stack.append(int(stack.pop() / operand))

        # Initialize the current operator and operand
        operator, operand = "+", 0

        # Iterate through all characters in s
        for c in s:

            # If the current character is a digit,
            if c in "0123456789":

                # Append it to the current operand
                operand = operand * 10 + int(c)

            # Elif the current character is a operator,
            elif c in "+-*/":

                # Append the current operand onto the stack
                append(operator, operand)

                # Update the current operand and operator
                operator, operand = c, 0

        # Add the last operand onto the stack
        append(operator, operand)

        # Return the sum of all operands as the result
        return sum(stack)


