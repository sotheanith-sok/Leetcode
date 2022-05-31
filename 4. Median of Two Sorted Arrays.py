"""
Problem:
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
    
    Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Solution (Binary Search):
    To find the median, we will perform a binary search on the small array and its mid point will be used to determine the small array left partition and the large array left partition such that the sum of their lengths will be the same as the merged array left partition. Let m and n be the midpoint of the small and large arrays respectively. If we pick the correct m, small[m] < large[n+1] and large[n] < small[m+1]. If small[m] > large[n+1], it means that we picked too many values from the small array and thus, the correct m will on the left partition. If large[n] > small[m+1], it means that we picked too little values from the small array and thus, the correct m will be on the right partition. Repeat the process until the correct m is found.   

Complexity:
    Time:
    Space
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Initialze variables.
        small, large = nums1, nums2
        m, n, half = 0, 0, (len(small) + len(large))//2

        # Determine which of the given array is smaller.
        if len(small) > len(large):
            small, large = large, small

        # Pointers for the binary search.
        left, right = 0, len(small)-1

        while True:

            # Calculate midpoints of both arrays.
            m = (left + right) // 2
            n = half - m - 1

            if small[m] <= large[n+1] and large[n] <= small[m+1]:
                return 

            elif small[m] > large[n+1]:
                right = m
            else:
                left = m


print(Solution().findMedianSortedArrays(
    [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5]))
