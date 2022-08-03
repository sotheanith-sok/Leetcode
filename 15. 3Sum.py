"""
Problem:
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.
    
    Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.
    
    Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Solution:
    This solution applied to any k-sum where k is greater than 2. Start by sorting nums. Then, recursively pick a number until you picked k-2 numbers. To avoid duplication, you can pick only from subsequent numbers after the previously picked number. 

    We will use the two pointers technique to picks the last two numbers. Initialize the left pointers to the index of the last picked number adding 1 and the right pointers to the end of nums. 
    If the sum of values at both pointers are less than the target, increment the left pointer by 1. Else, if the sum of values at both pointers are greater than the taget, decrement the right pointer by 1. Else, add the two values along with previously picked numbers into the result. Then, to avoid duplication, we will increment the left pointer until its value is different than the previous and repeat the process.  

Complexity:
    Time: O(n**k)
    Space: O(n**k)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # Initialize the result
        res = []

        # Sort nums so it is easier to avoid duplication
        nums = sorted(nums)

        # k-sum backtracking
        def backtrack(k=3, start=0, target=0, partialRes=[]):
            nonlocal res

            # While k hasn't reach 2
            if k != 2:

                # Pick a number from nums starting from the index of the previously picked number plus 1
                for i in range(start, len(nums)):

                    # To avoid duplication, we skip any number that is the same as the previous number
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # Pick a number recursively
                    backtrack(k - 1, i + 1, target - nums[i], partialRes + [nums[i]])

                return

            # Once we have picked k - 2 numbers

            # Initialize the left and right pointers
            l, r = start, len(nums) - 1

            # Iterate until both pointers crossed
            while l < r:

                # If the sum is greater than the target, decrement the right pointer
                if nums[l] + nums[r] > target:
                    r -= 1

                # If the sum is lesser than the target, increment the left pointer
                elif nums[l] + nums[r] < target:
                    l += 1

                # Else,
                else:

                    # Add the two values along with previously picked values into the result
                    res.append(partialRes + [nums[l], nums[r]])

                    # Increment the left pointer
                    l += 1

                    # To avoid duplication, we will skip any values at the left pointer that is equal to the previous value
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        backtrack()

        return res

