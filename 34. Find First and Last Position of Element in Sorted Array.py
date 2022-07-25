"""
Problem:
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    
    Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
    
    Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

Solution:
    Use binary search to solve this problem. If we found target at an index that is less than the previous saved index, we have to search the left side of it. If we found target at an index that is greater than previous saved index, we also have to search the right side of it. 

Complexity:
    Time: O(logn)
    Space: O(1)
"""

from math import inf

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        # Initialize the result.
        res = [inf, -inf]

        def binarySearch(start, end):

            # Calculate the mid index
            mid = ((end-start)//2)+start

            # If start index is greater than end index, end the search
            if start>end:
                return

            # If number at mid is equal to the target
            if nums[mid] == target:

                # If the mid index is less than previous saved index
                if mid<res[0]:

                    # Save the mid index
                    res[0]=mid

                    # Search the left side of the mid index
                    binarySearch(start, mid-1)
                
                # If the mid index is greater than previous saved index
                if mid>res[1]:

                    # Save the mid index
                    res[1]=mid

                    # Search the right side of the mid index
                    binarySearch(mid+1, end)

            # Else, if the number at mid is less than the target, search the right side
            elif nums[mid]<target:
                binarySearch(mid+1, end)

            # Else, if the number at mid is greater than the target, search the left side
            else:
                binarySearch(start,mid-1)

        # Perform the binary search
        binarySearch(0, len(nums)-1)
        
        # If we never found a target, change infinity to negative one
        if res[0]==inf:
            res = [-1,-1]

        return res
