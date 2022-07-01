""" 
Problem:
    You are given an array of positive integers arr. Perform some operations (possibly none) on arr so that it satisfies these conditions:

    The value of the first element in arr must be 1.
    The absolute difference between any 2 adjacent elements must be less than or equal to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed). abs(x) is the absolute value of x.
    There are 2 types of operations that you can perform any number of times:

    Decrease the value of any element of arr to a smaller positive integer.
    Rearrange the elements of arr to be in any order.
    Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

    Example 1:
    Input: arr = [2,2,1,2,1]
    Output: 2
    Explanation: 
    We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1].
    The largest element in arr is 2.
    
    Example 2:
    Input: arr = [100,1,1000]
    Output: 3
    Explanation: 
    One possible way to satisfy the conditions is by doing the following:
    1. Rearrange arr so it becomes [1,100,1000].
    2. Decrease the value of the second element to 2.
    3. Decrease the value of the third element to 3.
    Now arr = [1,2,3], which satisfies the conditions.
    The largest element in arr is 3.
    
    Example 3:
    Input: arr = [1,2,3,4,5]
    Output: 5
    Explanation: The array already satisfies the conditions, and the largest element is 5.

Solution:
    The goal of the problem is to modify the given array such that it is started with 1 and any two adjacent numbers are at most 1 difference while minimumize the amount of editing required. Thus, we start by sorting the array and set the value at the first index to 1. Then, we iterate through the remaining numbers. If a number is more than 1 larger than the previous number, we edit it to the previous number + 1. Repeat for all numbers and keep track of the largest number

Complexity:
    Time: O(nlogn)
    Space: O(1)
"""


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        # Start by sorting the array is an ascending order
        arr.sort()

        # Initialize the result and the first index of the array to 1
        res = arr[0] = 1

        # Iterate through the remaining values
        for i in range(1, len(arr)):

            # Set the current value to the previous value plus 1 if the current value is more than 1 larger than the previous value
            arr[i] = arr[i - 1] + 1 if arr[i] > arr[i - 1] + 1 else arr[i]
 
            # Update the result if we found a larger value
            res = arr[i] if arr[i] > res else res

        return res

