"""
Problem:
    A sequence x1, x2, ..., xn is Fibonacci-like if:

    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n
    Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

    A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

    

    Example 1:

    Input: arr = [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
    Example 2:

    Input: arr = [1,3,7,11,12,14,18]
    Output: 3
    Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].

Solution:
    We will reduce this problem to 2sum (Leetcode 1). Iterate through all numbers. At each iteration, assume that the current number is the target and all previous numbers are the second term. Check if the first term exists. If yes, increment the cached count of longest sequence to reaching (first term, second term) and cache the result as the count of the longest sequence to reach (second term, target term). 


Complexity:
    Time: O(n**2)
    Space: O(n**2)
"""


class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:

        # Initailize a set to check if a number exist
        exist = set(arr)

        # Initialize the cache cache[(i,j)] = count of the longest sequence to reach ith term, jth term
        cache = {}

        # Iterate through all numbers
        for j in range(len(arr)):

            # Iterate through all numbers up to jth index
            for i in range(j):

                # Calculate the first, second, and target terms
                # a + b = c => a = b - c
                target = arr[j]
                second = arr[i]
                first = target - second

                # Ensure that first term is less than second (avoid duplicate work) and first term exists
                if first < second and first in exist:

                    # If we haven't cache the count to reach (first term, second term), intialize it to zero
                    if (first, second) not in cache:
                        cache[(first, second)] = 0

                    # Update the cached count to reach (second term, target term)
                    cache[(second, target)] = cache[(first, second)] + 1

        # Add 2 to account for the first two terms if we found a valid subsequence else 0
        return max(cache.values()) + 2 if cache else 0

