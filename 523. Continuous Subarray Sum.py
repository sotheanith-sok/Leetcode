"""
    Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

    Example 1:
    Input: nums = [23,2,4,6,7], k = 6
    Output: true
    Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
    
    Example 2:
    Input: nums = [23,2,6,4,7], k = 6
    Output: true
    Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
    42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
    
    Example 3:
    Input: nums = [23,2,6,4,7], k = 13
    Output: false

Solution:
    The idea is that as we sum the num from left to right, the only time we see a remainder twice is when we have added a multiple of k into the sum. Since we also want the subarray to be at least two elements, we will use a hashmap to track remainders to indices and check if there is at least one element between remainders. There is also a possibility that we will only see a 0 remainder once and thus, to account for this edge case, we will assume that there exists a 0 remainder at index -1 in our hashmap (Ex: [23,2,4,6,6], 7).

Problem:
    Time: O(n)
    Space: O(n)

"""

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:

        # Map {remainder of sum : index}. Append the edge case.        
        remainders = {0: -1}

        # Total
        t = 0

        # Iterate through all num
        for i, n in enumerate(nums):

            # Add it to the total
            t += n

            # Calculate the remainder
            r = t % k

            # If remainder isn't exist, add it the map with its index
            if r not in remainders:
                remainders[r] = i

            # Else, if it exists and there is at least one element between this and the previous remainder, we have found the solution
            elif i - remainders[r] >= 2:
                return True

        # Return false if we didn't find a solution.
        return False

print(Solution().checkSubarraySum([5,7,1,2],7))