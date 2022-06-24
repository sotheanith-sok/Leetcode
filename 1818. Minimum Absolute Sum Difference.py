"""
Problem:
    You are given two positive integer arrays nums1 and nums2, both of length n.

    The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

    You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

    Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

    |x| is defined as:

    x if x >= 0, or
    -x if x < 0.
    
    Example 1:
    Input: nums1 = [1,7,5], nums2 = [2,3,5]
    Output: 3
    Explanation: There are two possible optimal solutions:
    - Replace the second element with the first: [1,7,5] => [1,1,5], or
    - Replace the second element with the third: [1,7,5] => [1,5,5].
    Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.
    
    Example 2:
    Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
    Output: 0
    Explanation: nums1 is equal to nums2 so no replacement is needed. This will result in an 
    absolute sum difference of 0.
    
    Example 3:
    Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
    Output: 20
    Explanation: Replace the first element with the second: [1,10,4,4,2,7] => [10,10,4,4,2,7].
    This yields an absolute sum difference of |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20

Solution:
    We will iterate through all pair of numbers in nums1 and nums2. At each iteration, we calculate the absolute difference and add it to the total. This represent the difference if we don't replace a value. Then, we use a binary search to find a number in nums1 that is closest to the number in nums2 and calculate their absolute difference. This represent the difference if we replace a value with a better number. Keep track of the best replacement aka the largest difference between the non-replace difference and replace difference. Lastly, return the new total by subtracting the best non-replace difference and adding the best replace difference.   

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


from math import inf


class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        # Create a new nums1 and sort it
        sorted_nums1 = list(nums1)
        sorted_nums1.sort()

        # Binary search to find a value in nums1 cloest to t
        def binarySearch(t):

            # Initialize the left pointer, the right pointer, the result variable.
            l, r, res = 0, len(sorted_nums1) - 1, inf

            # Repeat the search until the left and right pointers crossed.
            while l <= r:

                # Calculate the mid pointer
                m = (r + l) // 2

                # Calculate the difference between the target and the value at mid pointer
                diff = t - sorted_nums1[m]

                # If the value at mid pointer is closer to the target and the previous result, update the result
                if abs(diff) <= abs(t - res):
                    res = sorted_nums1[m]

                # If the difference is 0, we have found the cloest possible value and thus, we can end the search
                if diff == 0:
                    break

                # If the difference is larger than 0, there could be a value to the right that is closer to target
                elif diff > 0:
                    l = m + 1

                # If the difference is smaller than 0, there could be a value to the left that is closer to the target.
                else:
                    r = m - 1

            return res

        # Initialize varaibles to keep track of total, best difference if not replace, and best difference if replaced.
        total, bestNotReplace, bestReplace = 0, 0, 0

        # Iterate through all pairs in nums1 and nums2
        for i in range(len(nums2)):

            # Calculate the difference if we don't replace
            notReplace = abs(nums1[i] - nums2[i])

            # Calculate the difference if we replaced
            replace = abs(binarySearch(nums2[i]) - nums2[i])

            # Add the not replace difference to the total
            total += notReplace

            # If we found a better saving than previously (aka the gap between not replace difference and replace difference is larger), update corresponding varaibles
            if bestNotReplace - bestReplace < notReplace - replace:
                bestNotReplace, bestReplace = notReplace, replace

        # Return the new total mod 10^9+7
        return (total - bestNotReplace + bestReplace) % 1000000007

