""" 
Problem:
    Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

    Example 1:
    Input: arr = [3,1,2,4]
    Output: 17
    Explanation: 
    Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
    Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
    Sum is 17.
    
    Example 2:
    Input: arr = [11,81,94,43,3]
    Output: 444

Solution:
    Use monotonically decreasing stack to solve this problem. Iterate through all numbers. At each iteration, we will add the number into the monotonically decreasing stack. Then, we can calculate the sum of all subarray ending at such number. Lastly, we just accumulate the sum into the result.
    
    In order to avoid repeated calculation, we will maintain a variable for such sum and update it as we add and remove values from the monotonic stack. 

    Ex: arr = [3,1,2,4]

    i   num     stack(index, num)                   pRes        res
    -1  0       [(-1,0)]                            0           0
    0   3       [(-1, 0), (0, 3)]                   3           3
    1   1       [(-1, 0), (1, 1)]                   2           5
    2   2       [(-1, 0), (1, 1), (2, 2)]           4           9
    3   4       [(-1, 0), (1, 1), (2, 2), (3, 4)]   8           17

    
Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:

        # Initialize the monotonically decreasing stack
        stack = [(-1, 0)]

        # Initialize the result and partial result per number
        res, pRes = 0, 0

        # Iterate through all numbers
        for i, num in enumerate(arr):

            # Remove all previous numbers that are not lesser than the current number from the stack and update the partial result
            while stack and stack[-1][1] >= num:
                pRes -= stack[-1][1] * (stack[-1][0] - stack[-2][0])
                stack.pop()

            # Add the current number onto the stack and update the partial result
            stack.append((i, num))
            pRes += stack[-1][1] * (stack[-1][0] - stack[-2][0])

            # Update the result
            res = (res + pRes) % (10**9 + 7)

        return res
