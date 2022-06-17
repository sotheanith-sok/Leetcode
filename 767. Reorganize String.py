""" 
Problem:
    Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

    Return any possible rearrangement of s or return "" if not possible.

    Example 1:
    Input: s = "aab"
    Output: "aba"
    
    Example 2:
    Input: s = "aaab"
    Output: ""

Solution:
    Use a hashmap to count how many occurrences of each character. Then, we add characters and their counts into a max heap. Finally, we pop the most frequent characters from the heap and append the character to the result. If the current most frequent chracter is the same the last character that was added to the result, we skip it. Repeat until the heap is empty or we can't add any character anymore.   

Complexity:
    Time: O(nlogk) where 0 <= k <= 26 and n is the length of s
    Space: O(k) where 0 <= k <= 26 
"""
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:

        # Count the occurrences of each character
        map = {}
        for c in s:
            map[c] = map[c] + 1 if c in map else 1

        # Add counts and characters onto the max heap.
        heap = []
        for k, v in map.items():
            heap.append((-v, k))
        heapq.heapify(heap)

        # Varaible to keep track of the result
        res = ""

        # Iterate until the heap is empty
        while heap:

            # Pop the most frequent character
            count, c = heapq.heappop(heap)

            # If it the same as the last added character
            if res and c == res[-1]:

                # If we don't have another character in the heap, return ""
                if len(heap) == 0:
                    return ""
                # Else, use the second most frequent character instead.
                else:
                    count2, c2 = heapq.heappop(heap)
                    heapq.heappush(heap, (count, c))
                    count, c = count2, c2

            # Add the frequent character to the res and decrement its count
            res, count = res + c, count + 1

            # If the count hasn't reach 0, add it back to the heap.
            if count < 0:
                heapq.heappush(heap, (count, c))

        return res

