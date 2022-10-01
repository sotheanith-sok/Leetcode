"""
Problem:
    A message containing letters from A-Z can be encoded into numbers using the following mapping:

    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

    Given a string s containing only digits, return the number of ways to decode it.

    The test cases are generated so that the answer fits in a 32-bit integer.

Solution:
    Let dp be the number of possible decoding given we start at some arbitrary index. At each iteration, we have to examine two cases: picked 1 character and picked 2 character. Thus, dp can be define as

    dp[i] = (dp[i+1] if s[i:i+1] is valid else 0 ) + (dp[i+2] if s[i:i+2] is valid else 0) 
    
    where 
        dp[i+1] and dp[i+1] repesents the case where we pick 1 and 2 characters respectively where such characters are valid. Thus, we have to check the remainig string. If picked characters aren't valid, we can't process further.

    Do note that if we are able to reach nth index, we have found a valid decoding.

Complexity:
    Time: O(n)
    Space: O(n)
"""


from functools import lru_cache

# Top down dp
class Solution:
    def numDecodings(self, s: str) -> int:

        # Find length of s
        n = len(s)

        # A set for O(1) lookup if picked characters are valid
        valid = set(str(num) for num in range(1, 27))

        # Calculate the number of valid decoding given we start at ith index
        @lru_cache(None)
        def dp(i):

            # If we reach nth index, we have found a valid decoding
            if i == n:
                return 1

            # Sum both cases where we pick 1 character and 2 characters
            return sum(
                (dp(i + j) if i + j <= n and s[i : i + j] in valid else 0)
                for j in [1, 2]
            )

        return dp(0)


# Bottom-up
class Solution:
    def numDecodings(self, s: str) -> int:

        # Find length of s
        n = len(s)

        # A set for O(1) lookup if picked characters are valid
        valid = set(str(num) for num in range(1, 27))

        # Initialize the cache
        dp = [0] * n + [1]

        # Start from n-1 index to 0th index
        for i in range(n - 1, -1, -1):

            # Calculate the number of valid decoding for each i
            dp[i] = sum(
                (dp[i + j] if i + j <= n and s[i : i + j] in valid else 0)
                for j in [1, 2]
            )

        return dp[0]

