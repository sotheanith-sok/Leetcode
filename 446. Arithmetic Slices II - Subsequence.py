""" 
Problem:
    Given an integer array nums, return the number of all the arithmetic subsequences of nums.

    A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

    For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
    For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
    A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

    For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
    The test cases are generated so that the answer fits in 32-bit integer.

    Example 1:
    Input: nums = [2,4,6,8,10]
    Output: 7
    Explanation: All arithmetic subsequence slices are:
    [2,4,6]
    [4,6,8]
    [6,8,10]
    [2,4,6,8]
    [4,6,8,10]
    [2,4,6,8,10]
    [2,6,10]

    Example 2:
    Input: nums = [7,7,7,7,7]
    Output: 16
    Explanation: Any subsequence of this array is arithmetic.

Solution:
    Let dp be the function that return the number of valid sequences ending at jth number with an arbitrary difference. Thus, we can define dp as

        dp(j, diff) += dp(i, i-j) + 1 for i in range(j) 

        where "+1" account for subsequence of [i, j]

    However, since a subsequence must have at least 3 numbers to be valid, we will only accumulate dp(i, i-j) into the result.  


Complexity:
    Time: O(n**2)
    Space: O(n**2)
"""

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:

        # Find the length of nums and initialize the result
        n,  res = len(nums), 0

        # Initialize the dp cache
        dp = defaultdict(int)

        # Iterate through all numbers
        for j in range(n):

            # Check if the current number can form a subseqence with previous numbers
            for i in range(j):

                # Calculate their difference
                diff = nums[i] - nums[j]

                # Accumulate the number of sequence ending at a previous number with the same difference of ith and jth numbers into the result 
                res += dp[(i, diff)]

                # Update the number of subsequence ending at jth number with some arbitrary difference
                dp[(j, diff)] += 1 + dp[(i, diff)]

        return res
