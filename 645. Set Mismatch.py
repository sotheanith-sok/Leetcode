""" 
Problem:
    You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.

    Find the number that occurs twice and the number that is missing and return them in the form of an array.

    Example 1:
    Input: nums = [1,2,2,4]
    Output: [2,3]
    
    Example 2:
    Input: nums = [1,1]
    Output: [1,2]

Solution:
    Count all numbers and their occruences. Then, iterate thorugh all numbers from 1 to n and find a number with frequency of 2 and a number with frequency of 1. Return both numbers.

Complexity:
    Time: O(n)
    Space: O(n)
"""


from collections import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:

        # Initialize length of nums, result, counter
        n, res, counts = len(nums), [0, 0], Counter(nums)

        # Iterate through all numbers from 1 to n
        for num in range(1, n + 1):

            # If the current number has 2 occurence, save it into the result
            if counts[num] == 2:
                res[0] = num

            # If the current number has 0 occurnece, save it into the result
            if counts[num] == 0:
                res[1] = num

        return res

