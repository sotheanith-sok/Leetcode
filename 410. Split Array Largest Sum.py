""" 
Problem:
    Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

    Write an algorithm to minimize the largest sum among these m subarrays.

    Example 1:
    Input: nums = [7,2,5,10,8], m = 2
    Output: 18
    Explanation:
    There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8],
    where the largest sum among the two subarrays is only 18.
    
    Example 2:
    Input: nums = [1,2,3,4,5], m = 2
    Output: 9
    
    Example 3:
    Input: nums = [1,4,4], m = 3
    Output: 4

Solution (Binary Search):
    This is a binary search problem (Can you believe it?). Our boundary for the largest sum of a subarray is between max(nums) and sum(nums). Thus, we will use that as our left and right pointers and calculate the mid point. Then, we ask "Can we form m subarrays where the largest sum of those subarrays is the mid point?" If yes, we save it and search the left side (We try to minimize the largest sum. Thus, if a value is a valid largest sum, any larger value is also valid). Else, we search the right side. 

    To check if we can split the array into m subarrays with the largest sum being the target, we can sum up each value in the array and see how many array do we need to use such that each subarray is less than the target value. If we use less than or equal to m subarray, return True. Else, return False.   

Complexity:
    Time: O(nlogn)
    Space: O(1)

"""


class Solution:
    def splitArray(self, nums: list[int], m: int) -> int:

        # Check if we can split the array into m subarrays for a given target where target is the largest sum of those subarrays
        def canSplit(target):

            # Start with 1 subarray
            subarray = 1

            # Accumlate the sum
            total = 0

            # Iterate through all values in nums
            for n in nums:

                # Add values to the total
                total += n

                # If the total exceed the target
                if total > target:

                    # Add 1 more subarray
                    subarray += 1

                    # Move the last value to the new subarray
                    total = n
            
            # return result
            return subarray <= m


        # Find boundaries
        # Since there can't be an empty subarray, the lower bound of the largest sum of the subarrays is the largest value in nums
        l = max(nums) 

        # The upperbound is the sum of all values in nums
        r = sum(nums)

        # Keep track of the largest
        largest = 0

        # Iterate until left and right pointers overlapping
        while l <= r:

            # Find the mid pointer
            mid = (l + r) // 2

            # If we can spit the array using value at mid as our target, we save it and search the left side.
            if canSplit(mid):
                largest = mid
                r = mid - 1
            
            # Else, we search the right side
            else:
                l = mid + 1

        return largest

