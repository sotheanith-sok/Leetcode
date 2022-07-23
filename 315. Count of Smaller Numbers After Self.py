"""
Problem:
    You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

    Example 1:

    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.
    Example 2:

    Input: nums = [-1]
    Output: [0]
    Example 3:

    Input: nums = [-1,-1]
    Output: [0,0]

Solution:
    Use merge sort to solve this problem. Given two arrays that need to be merged. If a number in the left array is larger than a number in the right array, we know that such number on the right also less than all subsequent numbers in the left array.  

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:

        # Convert nums to an enumerate of nums
        nums = list(enumerate(nums))

        # Initialize the result
        res = [0] * len(nums)


        # Do merge sort
        def mergeSort(nums):

            # If there is only 1 number, return the array
            if len(nums) == 1:
                return nums


            # Else, split array into a left and right arrays
            left, right = (
                mergeSort(nums[: len(nums) // 2]),
                mergeSort(nums[len(nums) // 2 :]),
            )

            # Initialize pointers to the start of the left and right arrays
            l, r = 0, 0

            # Initialize a varaible to keep track of how many numbers in the right array are less than the number in the left array

            countRightLessThanLeft =0

            # Initialize the merged array
            merged = []

            # While the left pointer or the right pointer hasn't reach the end of its respective array
            while l < len(left) and r < len(right):

                # If the number at the left pointer is larger than the number at the right pointer
                if left[l][1] > right[r][1]:

                    # Increment how many numbers in the right array that are less than numbers in the left array
                    countRightLessThanLeft += 1

                    # Add the right number into the merged array
                    merged.append(right[r])

                    # Increment the right pointer
                    r += 1
                else:

                    # Increment the count of numbers in the right array less than the number at the left pointer by how many numbers in the right array that are less than numbers in the left array 
                    res[left[l][0]] += countRightLessThanLeft

                    # Add the left number into the merged array
                    merged.append(left[l])

                    # Increment the left pointer
                    l += 1


            # Add the remaining numbers in the left array into the merged array
            while l < len(left):
                # Increment the count of numbers in the right array less than the number at the left pointer by how many numbers in the right array that are less than numbers in the left array 
                res[left[l][0]] += countRightLessThanLeft

                # Add the left number into the merged array
                merged.append(left[l])

                # Increment the left pointer
                l += 1


            # Add the remaining numbers in the right array into the merged array
            while r < len(right):

                # Add the right number into the merged array
                merged.append(right[r])

                # Increment the right pointer
                r += 1

            return merged

        mergeSort(nums)

        return res

