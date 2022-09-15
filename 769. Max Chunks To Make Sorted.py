"""
Problem:
    You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

    We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

    Return the largest number of chunks we can make to sort the array.

    Example 1:
    Input: arr = [4,3,2,1,0]
    Output: 1
    Explanation:
    Splitting into two or more chunks will not return the required result.
    For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
    
    Example 2:
    Input: arr = [1,0,2,3,4]
    Output: 4
    Explanation:
    We can split into two chunks, such as [1, 0], [2, 3, 4].
    However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Solution:
    Use a monotonically increasing stack to solve this problem. Since we are working with a partition, maintain only a single minimum value would not work. (Ex: [2,0,1]) Instead we will maintain a range for each partition. A partition is only valid if its min value is greater than or equal to the maximum value of the previous partition on top of the stack. If a partition isn't valid, we will merge it with the partition on top of the stack. Lastly, return the length of the stack for the number of partition.  

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:

        # Intialize the stack
        stack = []

        # Iterate through all numbers
        for num in arr:

            # Initialize the range of the current partition
            minVal, maxVal = num, num

            # While the current partition isn't greater than a previous partition on top of the stack, mergethem together
            while stack and stack[-1][1] > minVal:
                minVal, maxVal = min(minVal, stack[-1][0]), max(maxVal, stack[-1][1])
                stack.pop()

            # Add the current parition onto the stack
            stack.append((minVal, maxVal))

        return len(stack)
