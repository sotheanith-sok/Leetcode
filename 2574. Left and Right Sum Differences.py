"""
Problem:
    Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

    answer.length == nums.length.
    answer[i] = |leftSum[i] - rightSum[i]|.
    Where:

    leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
    rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
    Return the array answer.

    Example 1:
    Input: nums = [10,4,8,3]
    Output: [15,1,11,22]
    Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
    The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
    
    Example 2:
    Input: nums = [1]
    Output: [0]
    Explanation: The array leftSum is [0] and the array rightSum is [0].
    The array answer is [|0 - 0|] = [0].

Solution:
    Initialize the left and right partition sums to 0 and sum of nums respectively. Iterate through all numbers. At each iteration, update both partition sums and append their absolute difference into the result. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:

        # Initialize the sum of the left and right partitions
        left, right = 0, sum(nums)

        # Initialize the result
        res = []

        # Iterate through all numbers
        for num in nums:

            # Remove the current number from the right partition
            right -= num

            # Append the absolute difference between the two partitions into the result
            res.append(abs(left - right))

            # Add the current number to the left partition
            left += num

        return res
