""" 
Problem:
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.

    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
    Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Solution:
    Since we can take infinite steps, we can be greedy here and take the largest jump for every step. However, if we land on a step with 0 jump, we need to backtrack by one step. Thus, we will maintain a stack of next steps as we jump.

    Iterate through all steps. For each step, if the next step on top of the stack is less than or equal to the current step, pop it. Then, if there is no next step and we are a step with 0 jump, we are stuck and we should return False. Else, we calculate the next step from the current step and add it onto the stack.    


Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:

        # Find the number of steps and initialize a stack to keep track of next steps
        n, stack = len(nums), []

        # Iterate through all steps
        for step in range(n - 1):

            # If there is a next step and it is less than or equal to the current step, pop it from the stack
            while stack and stack[-1] <= step:
                stack.pop()

            # Else, if there is no next step and we are at a 0 jump step, we are stuck
            if not stack and nums[step] == 0:
                return False

            # Else, add the next step onto the stack
            stack.append(step + nums[step])

        return True
