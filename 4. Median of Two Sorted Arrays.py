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

Solution:
    To find the median, we will perform a binary search on the small array and its mid point will be used to determine the small array left partition(including the midpoint) and the large array left partition such that the sum of their lengths will be the same as the merged array left partition. Let m and n be the midpoint of the small and large arrays respectively. If we pick the correct m, small[m] <= large[n+1] and large[n] <= small[m+1]. If small[m] > large[n+1], it means that we picked too many values from the small array and thus, the correct m will on the left partition. If large[n] > small[m+1], it means that we picked too little values from the small array and thus, the correct m will be on the right partition. Repeat the process until the correct m is found. Assume negative infinity and positive infinity for out of bound.   

Complexity:
    Time: O(log(min(m,n)))
    Space: O(1)
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Initialze variables.
        small, large = nums1, nums2
        m, n = 0, 0
        total = len(small) + len(large)
        half = total // 2

        # Determine which of the given array is smaller.
        if len(small) > len(large):
            small, large = large, small

        # Pointers for the binary search.
        left, right = 0, len(small) - 1

        while True:

            # Calculate midpoints of both arrays.
            m = (left + right) // 2
            n = half - m - 2

            # Assume negative and positive infinity when out of bound
            small_m = small[m] if m >= 0 else float("-infinity")
            small_m_next = small[m + 1] if (m + 1) < len(small) else float("infinity")
            large_n = large[n] if n >= 0 else float("-infinity")
            large_n_next = large[n + 1] if (n + 1) < len(large) else float("infinity")

            # Found the mid point
            if small_m <= large_n_next and large_n <= small_m_next:

                # Even case.
                if total % 2 == 0:
                    return (max(large_n, small_m) + min(large_n_next, small_m_next)) / 2

                # Odd case.
                else:
                    return min(large_n_next, small_m_next)

            # Overpick from the small array, the midpoint is somewhere left.
            elif small_m > large_n_next:
                right = m - 1

            # Underpick from the small array, the midpoint is somewhere right.
            else:
                left = m + 1

