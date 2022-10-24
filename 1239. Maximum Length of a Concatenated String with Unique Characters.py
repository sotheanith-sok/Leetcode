""" 
Problem:
    You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

    Return the maximum possible length of s.

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

    Example 1:
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All the valid concatenations are:
    - ""
    - "un"
    - "iq"
    - "ue"
    - "uniq" ("un" + "iq")
    - "ique" ("iq" + "ue")
    Maximum length is 4.
    
    Example 2:
    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
    
    Example 3:
    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
    Explanation: The only string in arr has all 26 characters.

Solution:
    1. Backtrack + BitMasking
        Convert all string into bitmasks of length 26 each. If there is a duplicate character in a string, assign 0 as such string bitmask. 
        
        Then, we can use backtracking to solve this problem. For a given i index and accumulative bitmask, check if  i is at the end of the arr. If yes, return the count of 1s bit in the accumulative bitmask. Else, check if any bitmask from i to the end of the arr can contribute to the current accumulative bitmask. If yes, xor them to produce the next accumlative bitmask and continue to the next recursion call.

    2. Set
        Let dp be the list containing all previous valid solution. Initally, dp has an empty set. Then, iterate through all strings. If the current string has duplicate character, skip it. Else, check if current string can contribute to any previous solution. If yes, we have found another valid solution and thus, we append it onto dp. Lastly, return the longest solution. 


Complexity:
    Time: O(n)
    Space: O(n)
"""


from functools import lru_cache


class Solution:
    def maxLength(self, arr: list[str]) -> int:

        # Find length of arr
        n = len(arr)

        # 1. Convert all strings to bitmasks
        # Initialize a list of bitmask
        bitmasks = [0] * n

        # Iterate through all strings
        for k, s in enumerate(arr):

            # Iterate through all characters
            for c in s:

                # Find the corresponding bit location
                i = ord(c) - 97

                # If there is 1s bit at such location, change the bitmask of this string to 0 and the conversion
                if (bitmasks[k] & 1 << i) >> i == 1:
                    bitmasks[k] = 0
                    break

                # Else, flip the bit at such location to 1
                bitmasks[k] = bitmasks[k] ^ 1 << i

        # 2. Recursively check for the number of 1s bits given ith index and a bitmask
        @lru_cache(None)
        def backtrack(i, bitMask):

            # If we reach the end of the list, return the count of 1s bits
            if i == n:
                return bin(bitMask).count("1")

            # Else, recursively check if any of the string from i onward can contribute to the current bitmask
            return max(
                backtrack(
                    j + 1,
                    (
                        (bitMask ^ bitmasks[j])
                        if (bitMask & bitmasks[j] == 0)
                        else bitMask
                    ),
                )
                for j in range(i, n)
            )

        return backtrack(0, 0)


class Solution:
    def maxLength(self, arr: list[str]) -> int:

        # Initialize a list of keep track of discovered solution
        dp = [set()]

        # Iterate through all strings
        for s in arr:

            # If there is a duplicate character, skip this string
            if len(set(s)) != len(s):
                continue

            # Convert the current string to a set
            s = set(s)

            # Iterate through all previous solution
            for prev in dp:

                # If there is an intersection between the current string and previous solution, they can't found a new valid solution
                if s & prev:
                    continue

                # Else, we have found a new solution
                dp.append(s | prev)

        # Return the longest solution
        return max(len(s) for s in dp)
