"""
Problem:
    Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

    An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

    We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

    Example 1:
    Input: nums = [3,5,2,6], k = 2
    Output: [2,6]
    Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
    
    Example 2:
    Input: nums = [2,4,3,3,5,4,9,6], k = 4
    Output: [2,3,3,4]

Solution:
    Use a monotonically increasing stack to solve this problem. We will place a range limit on the stack size. Let n be the length of nums and k be the desired result. Initially, the minimum and the maximum stack size will be k-n and k respectively. 
    
    Iterate through all numbers. While the current number is larger than the number on top of the stack, pop such number as long as the stack size is not less than the minimum stack size. Then, if the stack has not reach its maximum, append the current number on it. Lastly, increment the minimum stack size.

    Ex: nums = [2,4,3,3,5,4,2,1], k = 4
        stack       num         minSize     maxSize 
        []          2           -4          4
        [2]         4           -3          4
        [2,4]       3           -2          4
        [2,3]       3           -1          4
        [2,3,3]     5            0          4
        [2,3,3,5]   4            1          4
        [2,3,3,4]   2            2          4
        [2,3,2]     1            3          4
        [2,3,2,1]   _            4          4

Complexity:
    Time: O(n)
    Space: O(k)
"""


class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:

        # Initialize the stack
        stack = []

        # Initiliaze the minimum and the maximum stack size
        minSize, maxSize = k - len(nums), k

        # Iterate through all numbers
        for num in nums:

            # While there is a number on top of the stack and it is larger than the current number
            while stack and stack[-1] > num:

                # If the stack size reaches the minimum, end the removal
                if len(stack) == minSize:
                    break

                # Else, pop a number from top of the stack
                stack.pop()

            # If the stack hasn't reach its maximum, add the current number onto it
            if len(stack) < maxSize:
                stack.append(num)

            # Increment the minimum size of the stack
            minSize += 1

        return stack

