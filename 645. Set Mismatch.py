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
    Iterate through all numbers and mark it as seen by using such number as an index and change a number at such index to negative. Then, if we see a number that seen before, we have found a solution. Lastly, iterate through nums one more time and find the index where the number isn't negative. This is the other solution. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:

        # Initialize length of nums and result
        n, res = len(nums), [0, 0]

        # Iterate through all numbers
        for num in nums:

            # Get the current number
            num = abs(num)

            # If we have see the current number before, we have found a solution
            if nums[num - 1] < 0:
                res[0] = num
                continue

            # Mark the current number as seen by changing the number at the corresponding index to negative
            nums[num - 1] = -nums[num - 1]

        # Find the number that we havn't see before
        res[1] = [i + 1 for i in range(n) if nums[i] > 0][0]

        return res

