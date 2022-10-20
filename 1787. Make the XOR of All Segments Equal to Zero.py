"""
Problem:
    You are given an array nums​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

    Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.

    Example 1:
    Input: nums = [1,2,0,3,0], k = 1
    Output: 3
    Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
    
    Example 2:
    Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
    Output: 3
    Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
    
    Example 3:
    Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
    Output: 3
    Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].

Solution:
    Given nums = [A, B, C, D, E], k = 4
        (A ^ B ^ C ^ D) ^ (B ^ C ^ D ^ E) == 0
    
    From the equation above, we can see that 'A' must be equal to 'E' for the xor of both segments to be equal to 0. Thus, we can conclude that all numbers at each segment position 0, 1,..., k-1 must be the same number for the xor of all segments to equal 0.

    Instead of considering minimum changes, let's find the maximum numbers we can keep.

    There are two cases to consider:
    1. We can be greedy and keep the most frequent numbers for k-2 positions and change numbers at the last position to the xor of numbers we kept. 
    
    However, this approach won't give us the best result because two numbers with the same frequency will produce a different result.
    
    2. Thus, we have to search through all combinations using DFS.  

    To avoid searching through all combinations, we will use case 1 as the initial floor of the maximum numbers we can keep. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


from collections import defaultdict
from itertools import accumulate


class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:

        # Find the length of numbers
        n = len(nums)

        # Counts of numbers for each position 0, 1, ..., k-1
        counts = [defaultdict(int) for _ in range(k)]
        for i in range(n):
            counts[i % k][nums[i]] += 1

        # Find the maximum numbers we can keep for each position
        maxKeptPerPosition = [max(count.values()) for count in counts]

        # Create a suffix sum for O(1) lookup for how many numbers we can keep from i position onward
        suffix = list(accumulate(maxKeptPerPosition[::-1]))[::-1]

        # Case 1: Greedy approach
        maxKept = sum(maxKeptPerPosition) - min(maxKeptPerPosition)

        # Case 2: Search through all combinations with pruning
        def dfs(i, xor, kept):
            nonlocal maxKept

            # If the current position is k, we have reach the basecase
            if i == k:

                # If the xor of all numbers is 0
                if xor == 0:

                    # Update the maximum numbers that we kept
                    maxKept = max(maxKept, kept)
                return

            # If processing the current position won't result in us keeping more numbers than before, end the search
            if kept + suffix[i] <= maxKept:
                return

            # Else, check all numbers at the current position
            for num, count in counts[i].items():
                dfs(i + 1, xor ^ num, kept + count)

        dfs(0, 0, 0)

        return n - maxKept
