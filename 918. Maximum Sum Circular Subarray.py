"""
Problem:
    Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

    A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

    A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

    Example 1:
    Input: nums = [1,-2,3,-2]
    Output: 3
    Explanation: Subarray [3] has maximum sum 3.
    
    Example 2:
    Input: nums = [5,-3,5]
    Output: 10
    Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
    
    Example 3:
    Input: nums = [-3,-2,-3]
    Output: -2
    Explanation: Subarray [-2] has maximum sum -2.

Solution:
    There are two cases to consider.

    1. If a largest subarray is in a non-circular array, we can use Kandane algorithm to find it.
    
    2. If a largest subarray is in a circular array aka part of the subarry are composed from the head and tail of the main array, then it must be equal to the sum of the main array minus the minimum of the non-circular array.
    If you think about it, a number has to either contribute to a minimum subarray of the non-circular array or the maximum subarray of the cricular array. 

    ie: Given arr = [1, -50, 25, -500]
        -500 will contirbute to minimum subarraay of [-50,25,-500]

    ie: Given arr = [1, -50, 25, 500]
        500 will contributge to the maximum subarray of [1, 500]

    Finally, take the maximum between the two cases.

    Also, if all numbers are negative, sum(arr) - minSum == 0. So we need to deal with this edge case by checking if maxSum == max(arr) and minSum == sum(arr). If yes, we will return maxSum.


Complexity:
    Time: O(n)
    Space: O(1)
"""

from math import inf


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        # Variables to store max sum and max accumulator
        maxSum, maxAcc = -inf, 0

        # Variables to store min sum and min accumulator
        minSum, minAcc = inf, 0

        # Variables to store sum of nums and the largest number in nums
        allSum, maxN = 0, nums[0]

        # Iterate through all nums
        for n in nums:

            # Use kandane algorithm to find max sum
            # Update the accumulator to be the max between (n-1) + n or n
            maxAcc = max(maxAcc + n, n)

            # Update the max sum if the accumulator surpasses it
            maxSum = max(maxSum, maxAcc)

            # Use kandane algorithm to find the min sum
            # Update the accumulator to be the min between (n-1) + n or n
            minAcc = min(minAcc + n, n)

            # Update the min sum if the accumulator surpasses it
            minSum = min(minSum, minAcc)

            # Add n to total sum
            allSum += n

            # Update the largest nums
            maxN = max(maxN, n)

        # Return maxSum if all numbers are negative. Else, return the max between the largest subarray in the non-circular array vs the largest subarray in the circular array
        return (
            maxSum
            if maxSum == maxN and minSum == allSum
            else max(maxSum, allSum - minSum)
        )

