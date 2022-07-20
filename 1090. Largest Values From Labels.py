"""
Problem:
    There is a set of n items. You are given two integer arrays values and labels where the value and the label of the ith element are values[i] and labels[i] respectively. You are also given two integers numWanted and useLimit.

    Choose a subset s of the n elements such that:

    The size of the subset s is less than or equal to numWanted.
    There are at most useLimit items with the same label in s.
    The score of a subset is the sum of the values in the subset.

    Return the maximum score of a subset s.

    Example 1:
    Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
    Output: 9
    Explanation: The subset chosen is the first, third, and fifth items.
    
    Example 2:
    Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
    Output: 12
    Explanation: The subset chosen is the first, second, and third items.
    
    Example 3:
    Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
    Output: 16
    Explanation: The subset chosen is the first and fourth items.

Solution:
    Use a max heap to store labels and their values and a hashmap to keep track of how many time we have used a label. Iterate through the heap until we used x numbers. Pop a label and its value and check if we can still use such label. If yes, add its value to the result and update its count in the hashmap. 

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


from collections import defaultdict
import heapq


class Solution:
    def largestValsFromLabels(
        self, values: list[int], labels: list[int], numWanted: int, useLimit: int
    ) -> int:

        # Add labels and values into the heap
        heap = [(-value, label) for value, label in zip(values, labels)]
        heapq.heapify(heap)

        # Initialize the hashmap
        used = defaultdict(int)

        # Initialize the result
        res = 0

        # Iterate until we have used a certain number or the heap is empty
        while numWanted > 0 and heap:

            # Pop a label and its value from the heap
            value, label = heapq.heappop(heap)

            # If we can use such label
            if used[label] < useLimit:

                # Add its value to the result
                res += -value

                # Increment its count in the hashmap
                used[label] += 1

                # Decrement the number of numbers we still want
                numWanted -= 1

        return res

