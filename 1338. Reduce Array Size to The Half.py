"""
Problem:
    You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

    Return the minimum size of the set so that at least half of the integers of the array are removed.

    Example 1:
    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2
    Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
    Possible sets of size 2 are {3,5},{3,2},{5,2}.
    Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
    
    Example 2:
    Input: arr = [7,7,7,7,7,7]
    Output: 1
    Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Solution:
    Count the frequency of each number. Sort frequencies in a descending order. Iterate through all frequencies and continue to reduce length of arr by each frequency until there is only at most half left.  

Complexity:
    Time: O(klogk) where k is the number of unique number in the arr.
    Space: O(k)
"""

from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:

        # Find the length of the array
        n = len(arr)

        # Count the frequency of each number in the array
        counts = Counter(arr)

        # Sort frequencies in a descending order
        counts = sorted(counts.values(), reverse=True)

        # Initialize a variable to keep track of remaining element in the array
        remains = n

        # Iterate through all frequencies
        for i in range(n):

            # Reduce the remaining element by the current frequency
            remains -= counts[i]

            # End the search if there at most half element left in the array
            if remains <= n / 2:
                return i + 1

