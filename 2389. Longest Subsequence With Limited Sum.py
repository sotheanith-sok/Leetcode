""" 
Problem:
    You are given an integer array nums of length n, and an integer array queries of length m.

    Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

    Example 1:
    Input: nums = [4,5,2,1], queries = [3,10,21]
    Output: [2,3,4]
    Explanation: We answer the queries as follows:
    - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
    - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
    - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
    
    Example 2:
    Input: nums = [2,3,4,5], queries = [1]
    Output: [0]
    Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

Solution:
    To find the largest subsequence sum up to less than or equal to an arbitrary target, we should increase the total sum as little as possible while expanding the subseqence. 
    
    Start by sorting all numbers in an ascending order and continue to expand the subsequence from left to right until it is larger than a query. Then, we know that the length of such subsequence minus one is the largest possible subsequence. 
    
    In order to avoid repeated work, we will also sort all queries in an ascending order and continue to find the result for each of the query.      

Complexity:
    Time: O(mlogm + nlogn)
    Space: O(m + n)
"""


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:

        # Find lengths of nums and queries
        m, n = len(nums), len(queries)

        # Sort both nums and queries in an ascending order
        nums, queries = sorted(nums), sorted(
            [(val, i) for i, val in enumerate(queries)]
        )

        # Calculate the sum of subsequences starting at 0 and ending at all possible indices
        for i in range(1, m):
            nums[i] += nums[i - 1]

        # Initialize the result
        # The basecase is when the sum of all numbers are less or equal to the query
        res = [m] * n

        # Initialize pointers to both nums and queries
        i, j = 0, 0

        # Continue until a pointer each the end
        while i < m and j < n:

            # While the sum of a subsequence is less than or equal to the query, continue to expand it
            if nums[i] <= queries[j][0]:
                i += 1
                continue

            # Else, we have found a solution
            res[queries[j][1]] = i

            # Continue to the next query
            j += 1

        return res
