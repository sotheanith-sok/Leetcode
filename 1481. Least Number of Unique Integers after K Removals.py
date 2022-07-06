""" 
Problem:
    Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

    Example 1:
    Input: arr = [5,5,4], k = 1
    Output: 1
    Explanation: Remove the single 4, only 5 is left.
    
    Example 2:
    Input: arr = [4,3,1,1,3,3,2], k = 3
    Output: 2
    Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Solution:
    Find all unique nums and their count and store it into a map. Then, we sort the map based on counts. Starting from the smallest counts, keep removing numbers from the map as long as we haven't remove k numbers yet. Return the size of the map as the result.

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""

from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:

        # Count the numbers and sort them based on their counts
        sortedCount = Counter(arr).most_common()

        # Remove  numbers starting from the one with the smallest count until we have removed exactly k numbers
        while sortedCount and k > 0 and sortedCount[-1][1] <= k:
            k -= sortedCount.pop()[1]

        # Return the remaining unique numbers
        return len(sortedCount)

