"""
Problem:
    A string s is called happy if it satisfies the following conditions:

    s only contains the letters 'a', 'b', and 'c'.
    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    s contains at most a occurrences of the letter 'a'.
    s contains at most b occurrences of the letter 'b'.
    s contains at most c occurrences of the letter 'c'.
    Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

    A substring is a contiguous sequence of characters within a string.

    Example 1:
    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.
    
    Example 2:
    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    Explanation: It is the only correct answer in this case.

Solution:
    Use a max heap to store counts and characters. While heap is not empty, pop a character with the largest count and use it. Decrement the count by 1 and add the new count and char back into the heap. If a count reach 0, don't add the character back into the heap. If last two characters are the same as the character on top of the heap, skip it and pop another character. If there is no character that can be use (aka heap is empty after we skip/pop the first char), end the loop. Re-add the skip character back onto the heap.

Complexity:
    Time: O(n)
    Space: O(1)

"""
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # Add counts and chars into the heap. We will turn count to negative and use a min heap.
        heap = []
        combs = [(-a, "a"), (-b, "b"), (-c, "c")]
        for comb in combs:
            heapq.heappush(heap, comb)

        # Result string
        res = ""

        # Iterate until the heap is empty
        while heap:

            # A variable to store a skipped character
            noUse = None

            # If the last two characters are the same the the character on top of the heap, skip it
            if len(res) > 1 and res[-1] == heap[0][1] and res[-2] == heap[0][1]:
                noUse = heapq.heappop(heap)

            # If the heap is empty after we skipped a character, break out of the loop
            if not heap:
                break

            # Pop a character
            count, char = heapq.heappop(heap)

            # If its count is less than 0, use it
            if count < 0:
                count += 1
                res += char
                heapq.heappush(heap, (count, char))

            # If we skipped a character, add it back into the heap.
            if noUse:
                heapq.heappush(heap, noUse)

        return res

