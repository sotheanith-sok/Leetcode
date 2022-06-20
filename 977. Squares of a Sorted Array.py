""" 
Problem:
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

    Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
    
    Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Solution:
    Use a monotonic decreasing stack to solve this problem. For each number in nums, square them and add them to the stack. While, there is a number at the end of the stack less than current number, pop it and add it to the result. Lastly, pop all numbers from the stack and add them to the result. 
Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        monoStack, res = [], []

        # Add all values from nums to the monotonic decreasing stack.
        for n in nums:

            # Square the value here
            n = n * n

            # When we pop a number from the stack, we know that it is the current smallest number and thus, we add it to the res.
            while monoStack and n > monoStack[-1]:
                res.append(monoStack[-1])
                monoStack.pop()

            monoStack.append(n)

        # Add the rest of numbers from the monotonic decreasing stack to the res.
        while monoStack:
            res.append(monoStack[-1])
            monoStack.pop()

        return res

