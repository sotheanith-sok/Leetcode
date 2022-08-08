"""
Problem:
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

    Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    
    Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4
    Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Solution:
    A bottom-up dp approaches would requires look back through previous numbers to find the longest increasing subsequence that the current number can contribute to. Thus, the overall running time will be O(n**2) 

    A faster approach is to use a binary search with greedy approach to solve this problem. Itearate through all numbers. For each number, append it to the result if it is larger than the last number in the result. Else, replace such number with the smallest number in the result that is greater than or equal to it. Lastly, return the length of the result as the solution. 

    This approach works because an increasing subsequence of some arbitrary length will only be fully replaced if there is another increasing subsequence of identical length but contains smaller values. Thus, the last numbers in the result will always be the smallest overall of the last number of all increasing subsequence of that size. So if the next number is larger than the last number of the result, it guarantees to increasing the length of at least one increasing subsequence.  

    Ex: nums = [10,11,12,1,2,3,4]    
        i   Result          Longest Increasing Sequences
        0   [10]            [10] 
        1   [10, 11]        [10, 11] 
        2   [10, 11, 12]    [10, 11, 12]
        3   [1, 11, 12]     [10, 11, 12]
        4   [1, 2, 12]      [10, 11, 12]
        5   [1, 2, 3]       [10, 11, 12]
                            [1, 2, 3]
        6   [1, 2, 3, 4]    [1, 2, 3, 4]

    Ex: nums = [10,11,12,1,2,3,13]    
        i   Result          Longest Increasing Sequences
        0   [10]            [10] 
        1   [10, 11]        [10, 11] 
        2   [10, 11, 12]    [10, 11, 12]
        3   [1, 11, 12]     [10, 11, 12]
        4   [1, 2, 12]      [10, 11, 12]
        5   [1, 2, 3]       [10, 11, 12]
                            [1, 2, 3]
        6   [1, 2, 3, 13]   [10, 11, 12, 13]
                            [1, 2, 3, 13]

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        # Initialize the result
        res = []

        # Binary search to find the index of the smallest number in result that is greater than or equal to the target
        def binarySearch(l, r, target):

            nonlocal res

            # If the left and right pointers meet, we have found the smallest number that is greater than the target
            if l == r:
                return l

            # Find the mid pointer
            m = (r - l) // 2 + l

            # If the number at the mid pointer is equal to the target, we have found a number that is equal to the target
            if res[m] == target:
                return m

            # Else if the number at the mid poitner is less than the target, we search the right side
            elif res[m] < target:
                return binarySearch(m + 1, r, target)

            # Else, we search the left side including the number at mid pointer because it is one of the possible solution since it is greater than the target
            else:
                return binarySearch(l, m, target)

        # Iterate through all numbers
        for n in nums:

            # If the last number in the result is less than the current number
            if not res or res[-1] < n:

                # Append the current number to the result
                res.append(n)

                continue

            # Else, find the index of the smallest number in the result that is greater than or equal to the current number
            i = binarySearch(0, len(res) - 1, n)

            # Replace the current number at such index
            res[i] = n

        return len(res)
