"""
    Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

    The test cases are generated so that the answer can fit in a 32-bit integer.

    Example 1:
    Input: nums = [1,2,3], target = 4
    Output: 7
    Explanation:
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    Note that different sequences are counted as different combinations.
    
    Example 2:
    Input: nums = [9], target = 3
    Output: 0

Solution:
    Use a top down dynamic problem approach to solve this problem. We will recursively pick numbers from nums that reduce the target to 0 but not lesser than 0. Everytime, we are able to reach a 0, we have found a combination. Sum up all combinations and return the result. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:

        # Recursively picking numbers from nums that reduce target to 0 but not lesser than 0
        # Use lru_cache to avoid repeated work
        @lru_cache(None)
        def dp(taget):

            # If target is 0, we have found a combination
            if taget == 0:
                return 1

            # Initialize the partial result to 0
            partialRes = 0

            # Pick numbers from nums
            for num in nums:

                # Skip any numbers that reduce target to a negative number
                if taget - num < 0:
                    continue

                # Add the numbers of combinations added to the remain of target subtracting picked number into the partial result
                partialRes += dp(taget - num)

            # Return the partial result
            return partialRes

        return dp(target)
