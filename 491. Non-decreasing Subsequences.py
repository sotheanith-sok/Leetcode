"""
Problem:
    Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.


    Example 1:

    Input: nums = [4,6,7,7]
    Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    Example 2:

    Input: nums = [4,4,3,2,1]
    Output: [[4,4]]

Solution:
    Solve this problem using backtracking. Start with an empty list and continue to add an element into the list as long as the list is non-decreasing. At each iteration, copy the created list into the result.

Complexity:
    Time: O(2**n)
    Space: O(n**2)
"""


class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:

        # Find the length of numbers
        n = len(nums)

        # Initialize the result and a set to keep track of created subsequences
        res, existed = [], set()

        # Recursively generate all possible subsequences
        def backtrack(i, pRes):

            # If the current index is out of bound or the current number is less than the previous number, end the search
            if i == n or (pRes and pRes[-1] > nums[i]):
                return

            # Else, add the current number to the subsequence
            pRes.append(nums[i])

            # If the current subsequence already existed previously, end the search
            if tuple(pRes) in existed:
                pRes.pop()
                return

            # Else, copy the current subsequence into the result and mark it as existed if its length is at least 2
            if len(pRes) >= 2:
                existed.add(tuple(pRes))
                res.append(list(pRes))

            # Go to all possible next numbers
            for j in range(i + 1, n + 1):
                backtrack(j, pRes)

            # Remove the current number from the subsequence
            pRes.pop()

        # Start to genereate subsequence from all numbers
        for i in range(n):
            backtrack(i, [])

        return res


print(Solution().findSubsequences(nums=[4, 6, 7, 7]))
