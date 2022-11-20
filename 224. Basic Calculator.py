""" 

Problem:
    Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

    Example 1:
    Input: s = "1 + 1"
    Output: 2
    
    Example 2:
    Input: s = " 2-1 + 2 "
    Output: 3
    
    Example 3:
    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

Solution:
    The goal is to reduce all operations into an addition of positive and negative numbers. Start by iterate through all numbers. There are 4 cases to consider:

    1. If the current character is a digit, append it to the operand.
    2. If the current character is a sign, we can add the operand and its corresponding sign into the stack. Then, save the current sign and update the operand to 0.
    3. If the current character is an open parentheses, we will recrusively call the calculate on subsequent subarray and update the current index to the locaiton closing parentheses. 
    4. If the current character is a closing parenthese, we will return the sum of all numbers in the stack and the index of the such closing parenthese.  

Complexity:
    Time: O(n**2)
    Space: O(n)
"""


class Solution:
    def calculate(self, s: str) -> int:

        # Initialize the stack
        stack = []

        # Add an operand and its corresponding sign onto the stack
        def update(sign, op):
            if sign == "+":
                stack.append(op)
            if sign == "-":
                stack.append(-op)

        # Initialize the current index, operand, and sign
        i, op, sign = 0, 0, "+"

        # Iterate until we reach the end of s
        while i < len(s):

            # Case 1: If the current character is a digit, append it to the operand
            if s[i].isdigit():
                op = op * 10 + int(s[i])

            # Case 2: If the current character is a sign, we can add the operand and its corresponding sign into the stack. Then, save the current sign and update the operand to 0
            elif s[i] in "+-":
                update(sign, op)
                op, sign = 0, s[i]

            # Case 3: If the current character is an open parentheses, we will recrusively call the calculate on subsequent subarray and update the current index to the locaiton closing parentheses
            elif s[i] == "(":
                op, j = self.calculate(s[i + 1 :])
                i = i + j + 1

            # Case 4: If the current character is a closing parenthese, we will return the sum of all numbers in the stack and the index of the such closing parenthese
            elif s[i] == ")":
                update(sign, op)
                return sum(stack), i

            i += 1

        # Save the last operand onto the stack
        update(sign, op)

        return sum(stack)
