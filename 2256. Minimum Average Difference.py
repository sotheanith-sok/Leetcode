""" 
Problem:
    You are given a 0-indexed integer array nums of length n.

    The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

    Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

    Note:

    The absolute difference of two numbers is the absolute value of their difference.
    The average of n elements is the sum of the n elements divided (integer division) by n.
    The average of 0 elements is considered to be 0.
    
    Example 1:
    Input: nums = [2,5,3,9,5,3]
    Output: 3
    Explanation:
    - The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
    - The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
    - The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
    - The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
    - The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
    - The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
    The average difference of index 3 is the minimum average difference so return 3.
    
    Example 2:
    Input: nums = [0]
    Output: 0
    Explanation:
    The only index is 0 so return 0.
    The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.

Solution:
    Iterate through all numbers while maintain four variables: sum of left partition, count of left partition, sum of right partition, and count of right partition. At each number, calculate the average difference between both partitions and save the index of the best one. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


from math import inf


class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:

        # Find the length of numbers
        n = len(nums)

        # Initialize the sum of both paritions
        leftSum, rightSum = 0, sum(nums)

        # Initialize the count of both partitions
        leftCount, rightCount = 0, n

        # Initialize the best index and its corresponding average
        bestIndex, bestAverage = 0, inf

        # Iterate through all numbers
        for i in range(n):

            # Move the current number from the right to the left partion
            leftCount, rightCount = leftCount + 1, rightCount - 1
            leftSum, rightSum = leftSum + nums[i], rightSum - nums[i]

            # Calculate the average of both partitions
            average = abs(
                ((leftSum // leftCount) if leftCount else 0)
                - ((rightSum // rightCount) if rightCount else 0)
            )

            # If we found a better average, save the result
            if average < bestAverage:
                bestIndex, bestAverage = i, average

        return bestIndex
