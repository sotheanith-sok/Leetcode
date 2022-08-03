"""
Problem:
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.

    Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    
    Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]

Solution: 
    This is a solution to K-sum where k is bigger than 2. To start with, we will sort the nums and perform a recursive call. At each iteration, we pick a number and call the recursive funtion on the remaining numbers. Once we picked k-2 numbers, we will use two pointers to pick the last two numbers. The left pointer will be placed at the start and the right pointers will be placed at the end of remaining nums. If the sum of value at the two pointers are more than the remaining target, we move the right pointers by once. Else if it is less than the remaining target, we move the left pointer by 1. Else, we found a solution and save to the result. Finally, we increase the left pointer by 1 and iterate until the left cross the right pointer.  

    To prevent duplicate solution, we will skip a recurisve call or a left pointer when the previous num is the same as the current num. 

Complexity:
    Time: O(n**k)
    Space: O(n**k)
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        # Sort nums
        nums.sort()

        # Get length of nums
        N = len(nums)

        # List to store result
        res = []

        # The recursive calls
        def kSum(k=4, start=0, target=target, quad=[]):

            # Pick k-2 numbers
            if k != 2:

                # Iterate through all nums except for the last k
                for i in range(start, N - k + 1):

                    # If previous num is the same as current num, skip it
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # Do the recurisve call on the remaining nums
                    kSum(k - 1, i + 1, target - nums[i], quad + [nums[i]])

                # Return here to prevent the next of the algorithm from running if we havn't pick k-2 numbers
                return

            # Two sum algorithm

            # Set left and right pointers to the start and end of the remining nums
            l, r = start, N - 1

            # While left is less than right
            while l < r:

                # If the sum is less than the remaining target, increment the left pointer.
                if nums[l] + nums[r] < target:
                    l += 1

                # If the sum is larger than the remaining target, decrement the right pointer.
                elif nums[l] + nums[r] > target:
                    r -= 1

                # Else, we found a solution
                else:
                    # Append the solution to the result and increment the left pointer
                    res.append(quad + [nums[l], nums[r]])
                    l += 1

                    # While left pointer hasn't overlapping the right pointer, if the previous num is the same as the current num, skip it by increment the left pointer.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum()
        return res

