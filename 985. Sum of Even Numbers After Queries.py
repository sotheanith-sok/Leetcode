"""
Problem:
    You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

    For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

    Return an integer array answer where answer[i] is the answer to the ith query.

    Example 1:
    Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
    Output: [8,6,2,4]
    Explanation: At the beginning, the array is [1,2,3,4].
    After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
    After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
    After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
    After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
    
    Example 2:
    Input: nums = [1], queries = [[4,0]]
    Output: [0]

Solution:
    Start by calculating the sum of all even numbers. Then, iterate through all queries. For each query, if nums[i] is even, substract such number from the sum. Then, add val[i] to nums[i]. Next, if nums[i] is even, add such number to the sum. Lastly, add sum to the result. Continue to the next query. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def sumEvenAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:

        # Initialize the result
        res = []

        # Calculate the sum of all even numbers
        s = sum(num for num in nums if num % 2 == 0)

        # Iterate through all queries
        for val, i in queries:

            # If the current number is even, subtract such number from the sum
            s -= nums[i] if nums[i] % 2 == 0 else 0

            # Add value to the curret number
            nums[i] += val

            # If the current number is even, add such number to the sum
            s += nums[i] if nums[i] % 2 == 0 else 0

            # Append the sum to the result
            res.append(s)

        return res
