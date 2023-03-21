"""
Problem:
    Given an integer array nums, return the number of subarrays filled with 0.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:
    Input: nums = [1,3,0,0,2,0,0,4]
    Output: 6
    Explanation: 
    There are 4 occurrences of [0] as a subarray.
    There are 2 occurrences of [0,0] as a subarray.
    There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
    
    Example 2:
    Input: nums = [0,0,0,2,0,0]
    Output: 9
    Explanation:
    There are 5 occurrences of [0] as a subarray.
    There are 3 occurrences of [0,0] as a subarray.
    There is 1 occurrence of [0,0,0] as a subarray.
    There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
    
    Example 3:
    Input: nums = [2,10,2019]
    Output: 0
    Explanation: There is no subarray filled with 0. Therefore, we return 0.

Solution:
    For a given array of zeros, the number of subarrays is equal to the sum of 1 to length of such array.

    Ex: [0, 0, 0, 0] = 
            4 x [0]
            3 x [0, 0]
            2 x [0, 0, 0, 0]
            1 x [0, 0, 0, 0]

    Thus, we can iterate through all numbers in the array and keep track of the count of zeros we observe. Everytime, we observe a non-zero, we add the number of valid subarrays into the result and reset the count. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:

        # Add an extra number to trigger the number of subarrays calculation at the end
        nums.append(1)

        # Initialize the count of zeros and the result
        count, res = 0, 0

        # Iterate through all numbers
        for num in nums:

            # If the current number is zero, increment the count
            if num == 0:
                count += 1
                continue

            # Else, calculate the number of zeros subarrays
            res += count * (count + 1) // 2

            # Reset the count
            count = 0

        return res
