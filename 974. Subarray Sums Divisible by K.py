"""
Problem:
    Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

    A subarray is a contiguous part of an array.

    Example 1:
    Input: nums = [4,5,0,-2,-3,1], k = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by k = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
    
    Example 2:
    Input: nums = [5], k = 9
    Output: 0

Solution:
    Let a and be the current and previous prefix sum. Thus, we can define a and b as
    a - b = n * k
    (a - b) % k = (n * k) % k
    a % k - b % k = 0
    a % k = b % k 

    As shown above, two prefix sums that equal each other when mod with k will create a multiple of k.

    Start by initializing a cache of size k to store counts of previous prefix sums. Iterate through all numbers. For each number, calculate the prefix sum up to such number and check if there exists a previous prefix sum that can be pair with the current prefix sum such that both sums are equal when modded by k. If yes, add the count of such previous prefix sum to the result. Then, increment the count of the current prefix sum by 1.

    Initialize counts[0] as 1 since empty list is divisable by k.

Complexity:
    Time: O(n)
    Space: O(k)
"""


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        # Intialize the cache to store counts of previous prefix sum
        counts = [1] + [0] * (k - 1)

        # Intialize variables to keep track of the current prefix sum and result
        prefix, res = 0, 0

        # Iterate through all nums
        for num in nums:

            # Calculate the current prefix sum
            prefix = (prefix + num) % k

            # Check for a previous prefix sum that we can pair with the current prefix and add its count to the result
            res += counts[prefix]

            # Increment the count of the current prefix sum by 1
            counts[prefix] += 1

        return res

