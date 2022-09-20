"""
Problem:
    Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

    Example 1:
    Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
    Output: 3
    Explanation: The repeated subarray with maximum length is [3,2,1].
    
    Example 2:
    Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
    Output: 5

Solution:
    Let dp be the function that return the longest substring common between nums1 ended at ith index and nums2 ended at jth index. If nums1[i] == nums2[j], the longest common substring is 1 plus the longest common substring at ended at i-1 and j-1. Else, the longest common ended at i and j is 0. 

    Thus, we can define dp as
        dp(i, j) = dp(i-1, j-1) + 1 if nums1[i] == nums[j] else 0

    Find the longest common substring for all possible i and j and return the largest one. 

    Thoughts:
    1. Why does the top-down dp throw tle?
    Ans: My guess is that because we have to find the longest common substring for all possible i and j, the running time is actually O(2mn). 

    2. Why does the bottom-up dp throw tle?
    Ans: If Im being honest, I have no clue why. But, there are other Python solution that leetcode will throw tle for such as leetcode 1938. Anyhow, here are a few things you can try. 
        Remove space compression
        Taking max of dp at the end instead of every combination i and j

Complexity:
    Time: O(mn)
    Space: O(mn)
"""


from functools import lru_cache
from itertools import product


# Top-down
class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:

        # Find lengths of nums1 and nums2
        m, n = len(nums1), len(nums2)

        # Find the longest common substring of nums1 ended at ith index and nums2 ended at jth index
        @lru_cache(None)
        def dp(i, j):

            # If i and j are  out of bound or nums1[i] != nums2[j], return 0
            if not (0 <= i < m) or not (0 <= j < n) or nums1[i] != nums2[j]:
                return 0

            # Else, return the longest common substring at i-1 and j-1 plus 1
            return dp(i - 1, j - 1) + 1

        # Initialaize the result
        res = 0

        # Find the longest common substring for all possible i and j
        for i, j in product(range(m), range(n)):
            res = max(res, dp(i, j))
        return res


# Bottom-up
class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:

        # Find lengths of nums1 and nums2
        m, n = len(nums1), len(nums2)

        # Initialize the cache
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # Calculate the longest common substring for all possible i and j
        for i, j in product(range(1, m + 1), range(1, n + 1)):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

        # Return the longest common substring overall
        return max(max(row) for row in dp)

