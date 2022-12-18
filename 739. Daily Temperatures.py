""" 
Problem:
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    
    Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]
    
    Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]

Solution:
    Use a monotonically decrease stack to solve this problem. Start by intializing the result with all 0s. Then, we will iterate through all temperatures. For each temperature, we will see if it is an increase of a previous temperature in the stack. If yes, we have found the solution to a previous temperature and we just update the difference between the two indices. Then, we add the current temperature and its index into the stack.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        # Get the length of temperatures
        n = len(temperatures)

        # Initialize the result and the monotonically decreasing stack
        res, stack = [0] * n, []

        # Itearte through all temperatures
        for i, temperature in enumerate(temperatures):

            # Check if the current temperature is an increase any previous temperatuer
            while stack and stack[-1][1] < temperature:

                # If yes, pop the previous temperature from the stack
                j, _ = stack.pop()

                # Update the result
                res[j] = i - j

            # Add the current temperature and its index into the stack
            stack.append((i, temperature))

        return res
