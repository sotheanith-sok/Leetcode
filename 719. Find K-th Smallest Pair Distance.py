"""
Problem:
    The distance of a pair of integers a and b is defined as the absolute difference between a and b.

    Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

    Example 1:
    Input: nums = [1,3,1], k = 1
    Output: 0
    Explanation: Here are all the pairs:
    (1,3) -> 2
    (1,1) -> 0
    (3,1) -> 2
    Then the 1st smallest distance pair is (1,1), and its distance is 0.

    Example 2:
    Input: nums = [1,1,1], k = 2
    Output: 0

    Example 3:
    Input: nums = [1,6,1], k = 3
    Output: 5

Solution:
    Using heap to process pairs of numbers with the least distance will result in an O(n**2) running time.
    
    We can do better with binary search through all possible solution. The goal is to find the least distance where there are at least k pairs with such distance apart. The range of possible solution is between 0 and max(nums) - min(nums). However, the main question is given a distance, how can we efficiently counts how many pairs are at most such distance apart. 

    We actually can find the count of such pairs in linear time by sorting nums and using two pointers approach. Let the left pointer be the start of a sequence and the right pointer be the next number to be added to the sequence. While the difference between numbers at left and right are greater than the current distance, increment the left pointer. Then, remaining numbers between l and r-1 will be how many numbers we can pair with the number at the right pointer such that they are at most such current distance apart. 

Complexity:
    Time: O(nlog(maxDst) + nlogn)
    Space: O(1)
"""


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:

        # Find the count of numbers
        n = len(nums)

        # Sort numbers
        nums.sort()

        # Initialize the minimum and maximum distance
        minDst, maxDst = 0, nums[-1] - nums[0]

        # While the min distance isn't greater than the maximum distance
        while minDst <= maxDst:

            # Calculate the current distance
            dst = (maxDst - minDst) // 2 + minDst

            # Count how many pairs of numbers with at most the current distance apart
            # Intialize the count
            count = 0

            # Initialize the left pointer
            l = 0

            # Increment the right pointer
            for r in range(1, n):

                # While the distance between numbers at both pointers are greater than the distance, increment the left pointer
                while nums[r] - nums[l] > dst:
                    l += 1

                # Calculate how many previous numbers can be pair with the number at the right pointer and add it to the count
                count += r - l

            # If the count is greater than k, search the left side since we want the minimum
            if count >= k:
                maxDst = dst - 1

            # Else, search the right side
            else:
                minDst = dst + 1

        return minDst
