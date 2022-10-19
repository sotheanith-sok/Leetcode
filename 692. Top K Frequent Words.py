"""
Problem:
    Given an array of strings words and an integer k, return the k most frequent strings.

    Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

    Example 1:
    Input: words = ["i","love","leetcode","i","love","coding"], k = 2
    Output: ["i","love"]
    Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
    
    Example 2:
    Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
    Output: ["the","is","sunny","day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Solution:
    Use heap to solve this problem. "nsmallest" will starts by constructing a heap of size k and continue updating heap with the smallest value. We use 'nsmallest' instead of 'nlargest' because it is easier to sort counts in descending order by negating each count than sort words in descending order. 

Complexity:
    Time: O(nlogk)
    Space: O(n)
"""

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        # Get words and their counts
        counts = Counter(words)

        # Add counts and words into the heap
        heap = [(-count, word) for word, count in counts.items()]

        # Find the k smallest words
        res = heapq.nsmallest(k, heap)

        # Return words
        return [word for _, word in res]

