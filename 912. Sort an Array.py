"""
Problem:
    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

    Example 1:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]
    Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
    
    Example 2:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
    Explanation: Note that the values of nums are not necessairly unique.

Solution:
    Sort the list of numbers using Timsort algorithm which is a hybrid of insertion sort and merge sort.

    1. Divide the list into buckets of equal size.
        > Initial bucket size is usually a power of 2

    2. Sort each bucket using insertion sort.
        > Use auxilery bucket and binary search to quickly sort each bucket.

    3. Merge each pair of buckets together using merge algorithm from merge sort.
        > Reduce merge space overhead using binary search 
        
        @Credit: https://en.wikipedia.org/wiki/Timsort 
        Example: two runs [1, 2, 3, 6, 10] and [4, 5, 7, 9, 12, 14, 17] must be merged. Note that both runs are already sorted individually. The smallest element of the second run is 4 and it would have to be added at the fourth position of the first run in order to preserve its order (assuming that the first position of a run is 1). The largest element of the first run is 10 and it would have to be added at the fifth position of the second run in order to preserve its order. Therefore, [1, 2, 3] and [12, 14, 17] are already in their final positions and the runs in which elements movements are required are [6, 10] and [4, 5, 7, 9]. With this knowledge, we only need to allocate a temporary buffer of size 2 instead of 4.

    4. Double the bucket size and repeat until bucket size greater than the list of numbers

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


from bisect import bisect_left, insort_left


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        # Sort a bucket using an auxilery bucket and the insertion sort algorithm
        def insertionSort(low, high):

            # Initialize the auxilery bucket
            bucket = []

            # Insert each element into the auxilery bucket using binary search
            for i in range(low, high):
                insort_left(bucket, nums[i])

            # Copy sorted numbers from the auxilery bucket back into the original bucket
            for i, j in zip(range(low, high), range(len(bucket))):
                nums[i] = bucket[j]

        # Merge two buckets together using merging algorithm from merge sort
        def merge(low1, high1, low2, high2):

            # Reduce merge space overhead by excluding leading numbers of bucket 1 and tailing numbers of bucket 2
            low1, high2 = bisect_left(nums, nums[low2], low1, high1), bisect_left(
                nums, nums[high1 - 1], low2, high2
            )

            # Create auxilery copies of both buckets and reverse them
            list1, list2 = nums[low1:high1], nums[low2:high2]
            list1.reverse(), list2.reverse()

            # Copy numbers from both auxilery buckets back into the original bucket
            i = low1

            while list1 or list2:
                nums[i] = (
                    list1.pop()
                    if not list2 or (list1 and list1[-1] < list2[-1])
                    else list2.pop()
                )
                i += 1

        # Find the length of numbers
        n = len(nums)

        # Initialize the bucket size
        bucketSize = min(n, 32)

        # Iterate until bucket size is greater than the length of numbers
        while bucketSize <= n:

            # Sort all buckets using insertion sort
            for i in range(0, n, bucketSize):
                insertionSort(i, min(n, i + bucketSize))

            # Merge each pair of buckets using merging algorithm from merge sort
            for i in range(0, n, bucketSize * 2):
                if i + bucketSize >= n:
                    continue

                merge(i, i + bucketSize, i + bucketSize, min(n, i + bucketSize * 2))

            # Double the bucket size
            bucketSize *= 2

        return nums
