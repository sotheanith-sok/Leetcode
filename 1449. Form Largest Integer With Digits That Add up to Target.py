"""
Problem:
    Given an array of integers cost and an integer target, return the maximum integer you can paint under the following rules:

    The cost of painting a digit (i + 1) is given by cost[i] (0-indexed).
    The total cost used must be equal to target.
    The integer does not have 0 digits.
    Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return "0".

    Example 1:
    Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
    Output: "7772"
    Explanation: The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.
    Digit    cost
    1  ->   4
    2  ->   3
    3  ->   2
    4  ->   5
    5  ->   6
    6  ->   7
    7  ->   2
    8  ->   5
    9  ->   5
    
    Example 2:
    Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
    Output: "85"
    Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.
    
    Example 3:
    Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
    Output: "0"
    Explanation: It is impossible to paint any integer with total cost equal to target.

Solution:
    Use dp to solve this problem. Let dp be the function that generate the largest number given a budget. For each dp call, check for all digits that we can use and if we were to use such digit, can the remaining budget be all used to form a number. If yes, append the digit to front of the returned number. Lastly, return the largest number.

Complexity:
    Time: O(n**2) where n == target // min(cost) and we will call dp n times and it costs O(n) to compare and concatenate n-length strings  
    Space: O(n)
"""


from functools import lru_cache


class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:

        # Determine if string a is greater than string b
        def greater(a, b):

            # If their lengths are different, use their length to determine if a is greater than b
            if len(a) != len(b):
                return len(a) > len(b)

            # Else, check all digits one by one
            for c1, c2 in zip(a,b):

                # If current digits of a and b are equal, continue to the next digits pair
                if c1 == c2:
                    continue

                # Else, check if digit of a is greater than digit of b
                return c1>c2

            # Return False if all digits are the same
            return False

        # Save costs and their corresponding digits into a dict 
        # Override the smaller digit with a larger one if their costs are the same
        costs = {c: str(i + 1) for i, c in enumerate(cost)}

        # Top-down dp to find the largest number giving a budget
        @lru_cache(None)
        def dp(budget):

            # If we have 0 budget left, we have reach the basecase, return (True, "")
            if budget == 0:
                return True, ""

            # Initialize varaibles to store the largest number and the boolean to indicate that there is a digit where if we were to pick such digit, we can form a number using all of the remaining budget
            largestNum, ableToUseAll = "", False

            # Iterate through all digits
            for cost, digit in costs.items():

                # If the current digit has a higher cost than the budget, skip it
                if cost > budget:
                    continue

                # Else, if we were to pick such digit, can all of the remaining budget be used to form a number?
                usedAll, nextNum = dp(budget - cost)

                # If yes
                if usedAll:

                    # Concatenate the picked digit with the next number to form the current number
                    num = digit + nextNum

                    # If the current number is greater than previous number, save it
                    largestNum = num if greater(num, largestNum) else largestNum

                    # Update the boolean  to indicate that we have found a number that formed using all of the budget
                    ableToUseAll = ableToUseAll or usedAll

            # Return result if we were able to find a number formed using all of the budget
            # Else, return "0"
            return ableToUseAll, largestNum if ableToUseAll else "0"

        return dp(target)[1]

