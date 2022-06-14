""" 
Problem:
    Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

    The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
    

    Example 1:
    Input: s = "()"
    Output: true
    
    Example 2:
    Input: s = "(*)"
    Output: true

    Example 3:
    Input: s = "(*))"
    Output: true
    
Solution:
    There are two possible solutions to this problem.
        1. We will use two variables to keep track of the minimum and the maximum open parenthesis. Then, we will always choose a greedy option. If we see a "(", we will increment both varaibles. If we see a ")", we will decrement both variables. Finally, if we see a "*", we will decrement the minimum and increment the maximum. If the maximum ever reach a negative number, we know that there is a parenthesis that we won't be able to pair and thus, we return false. If the minimum reaches a negative number, we know that the previous assumption about the "*" as a closing parenthesis is wrong and thus, we increment the minimum by 1. Once we iterated through all numbers and the minimum reaches 0, we know that the given string is valid.
        
        2. We will use two stacks: main and stars, to solve this problem. We will iterate through characters until we see a ")". Then, we will try to pair it with a "(" from the main stack or a "*" from the stars stack if there exists an occurance of a "*" before the current ")". If it isn't possible, return False. Once, we paired all the closing parentheses, we will pair the remaining "(" with a "*" as long as it shows after an "(". If we succesful paired all "(", the given string is valid.   

Problem:
    Time: O(n)
    Space: O(1) or O(n)

"""


class Solution:
    def checkValidString(self, s: str) -> bool:

        # Keep track of the minimum and the maximum opening parentheses. 
        leftMin, leftMax = 0, 0

        # Iterate through all characters
        for c in s:

            # Opening paranthesis case
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            
            # Closing paranthesis case
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            
            # Star case
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1


            # The maximum of the opening parentheses should never reach negative unless, we have more closing parentheses than opening parentheses.  
            if leftMax < 0:
                return False

            # If the minimum of opening parentheses reach negtaive, we made a wrong  assumption about a previous star as a closing parenthesis and thus, we increase the minimum by 1 aka assume the previous star as blank space. 
            if leftMin < 0:
                leftMin += 1

        return leftMin == 0


class Solution:
    def checkValidString(self, s: str) -> bool:

        # Stacks to store indicies of opening parentheses and stars.
        main, stars = [], []

        # Iterate through all characters
        for i, c in enumerate(s):

            # Add opening parentheses to the stack.
            if c == "(":
                main.append(i)
                continue

            # Add stars to the stack.
            if c == "*":
                stars.append(i)
                continue

            # If we found a closing parenthesis, we try to pair it with either an opening parenthesis or a star. Return false if it isn't possible
            if main:
                main.pop()
            elif stars and stars[-1] < i:
                stars.pop()
            else:
                return False

        # Pair the remaining openining parenthesis with stars. 
        while main and stars and main[-1] < stars[-1]:
            main.pop()
            stars.pop()

        return not main

