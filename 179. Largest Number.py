"""
Problem:
    Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

    Since the result may be very large, so you need to return a string instead of an integer.

    Example 1:
    Input: nums = [10,2]
    Output: "210"

    Example 2:
    Input: nums = [3,30,34,5,9]
    Output: "9534330"

Solution:
    We will sort the nums with a custom comparison function. a comes before b if and only if str(a+b) > str(b+a) and thus, the function will return True or -1. Else, it will return false or 1. 
Complexity:
    Time: O(nlogn)
    Space: O(1)
"""

# Quick Sort Solution
class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        # A custom comparator function.
        def compare(a, b):
            a, b = str(a), str(b)
            return int(a + b) > int(b + a)

        # Partition step for quicksort
        def partition(l, r, nums):
            # Assume the right most element is the pivot
            
            # Use two pointers from the left
            i, j = l, l

            # While iterate through the list
            for i in range(l, r):

                # If we found an element that should be on the left of the pivot, we will switch it with the j. Then, we increment j by 1.
                # J acts as our tracker for which slots to add element into.
                if compare(nums[i], nums[r]):
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1

            # Swap the pivot with j.
            nums[j], nums[r] = nums[r], nums[j]

            return j

        # Quick sort recursive
        def quicksort(l, r, nums):

            # While left is less than right pointer
            if l < r:

                # Find a pivot
                pivot = partition(l, r, nums)
                
                # Sort the left partition
                quicksort(l, pivot - 1, nums)

                # Sort the right partition
                quicksort(pivot + 1, r, nums)

        quicksort(0, len(nums) - 1, nums)

        # Edge case for when we have "0000" and thus, we return only 0. Else, merge all numbers.
        return "0" if nums[0] == 0 else "".join(map(str, nums))

from functools import cmp_to_key
# Built-in Sort Solution
class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        # A custom comparator. It expects to return 
        #   -1 if a comes before b
        #   0 if a is the same as b
        #   1 if a comes after b
        def compare(a, b):
            a, b = str(a), str(b)
            if int(a + b) > int(b + a):
                return -1
            return 1

        nums.sort(key=cmp_to_key(compare))

        # Edge case for when we have "0000" and thus, we return only 0. Else, merge all numbers.
        return "0" if nums[0] == 0 else "".join(map(str, nums))


