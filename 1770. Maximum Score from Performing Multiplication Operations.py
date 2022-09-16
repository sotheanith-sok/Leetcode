"""
Problem:
    You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

    You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

    Choose one integer x from either the start or the end of the array nums.
    Add multipliers[i] * x to your score.
    Remove x from the array nums.
    Return the maximum score after performing m operations.

    Example 1:
    Input: nums = [1,2,3], multipliers = [3,2,1]
    Output: 14
    Explanation: An optimal solution is as follows:
    - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
    - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
    - Choose from the end, [1], adding 1 * 1 = 1 to the score.
    The total score is 9 + 4 + 1 = 14.
    
    Example 2:
    Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
    Output: 102
    Explanation: An optimal solution is as follows:
    - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
    - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
    - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
    - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
    - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
    The total score is 50 + 15 - 9 + 4 + 42 = 102.

Solution:
    Use dp to solve this problem. Let m and n be the length of multipliers and nums respectively. Let score be the function that return the maximum score for some arbitrary k-th pick between a left pointer l (front) and a right pointer r (back). Thus, we can define score as:

    score(k, l, r) = max(
        nums[l] * multipliers[k] + score(k + 1, l + 1, r), 
        nums[r] * multipliers[k] + score(k + 1, l, r - 1)
    ) 
    
    where score(k >= m, _, _) = 0 

    Since r can be caclulate from k and l, we can reduce the space complexity by 1 dimension. Thus, 

    score(k, l) = max(
        nums[l] * multipliers[k] + score(k + 1, l + 1), 
        nums[r] * multipliers[k] + score(k + 1, l)
    )

    where r = (n-1) - k + l

Complexity:
    Time: O(m**2)
    Space: O(m**2)
"""


from functools import lru_cache

# Top-down dp
class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:

        # Calculate the length of multipliers and nums
        m, n = len(multipliers), len(nums)

        # Recursive function to calculate score for k-th pick between nums at the left and right pointer
        @lru_cache(None)
        def score(k, l):

            # If we overpick, return 0
            if k == m:
                return 0

            # Calculate the right pointer
            r = (n - 1) - k + l

            # Calculate the maximum score if we were to pick a number at the left pointer vs the right pointer
            return max(
                nums[l] * multipliers[k] + score(k + 1, l + 1),
                nums[r] * multipliers[k] + score(k + 1, l),
            )

        return score(0, 0)


# Bottom-up dp
class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:

        # Calculate the length of multipliers and nums
        m, n = len(multipliers), len(nums)

        # Initialze a cache to store scores
        score = [[0 for _ in range(m + 1)] for _ in range(m + 1)]

        # Fill in the cache starting from k == m-1,...,0 since we know that k==m is 0
        for k in range(m - 1, -1, -1):

            # Go through all possible left pointers
            for l in range(k + 1):

                # Calculate the right pointer
                r = (n - 1) - k + l

                # Calculate the maximum score if we were to pick a number at the left pointer vs the right pointer
                score[k][l] = max(
                    nums[l] * multipliers[k] + score[k + 1][l + 1],
                    nums[r] * multipliers[k] + score[k + 1][l],
                )

        return score[0][0]

