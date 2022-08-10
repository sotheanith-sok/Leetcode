"""
Problem:
    Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

    We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

    Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

    Example 1:
    Input: arr = [2,4]
    Output: 3
    Explanation: We can make these trees: [2], [4], [4, 2, 2]
    
    Example 2:
    Input: arr = [2,4,5,10]
    Output: 7
    Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Solution:
    Iterate through all numbers. For each number C, find pairs of numbers A and B such that A * B = C. Then, for all pairs of (A,B), sum up the number of combinations leading up to A multiply by the number of combinations leading up to B. Aka we are doing C(a,1) * C(b,1) where a is the number of combination leading up to A and b is the number of combination leading up to the B. 

    This approach also account for the location of A and B. ie if A and B are different numbers, we will count it twice for when A is the left child and B is the right child and for when B is the left child and A is the right child. However, if A and B are the same number, we will only count it once because A is unique in the array. 

    Ex: Given arr = [2, 4, 8] 

    dp(2) = 1
    dp(4) = 1 + dp(2) * dp(2) = 2
    dp(8) = 1 + dp(2) * dp(4) + dp(4) * dp(8) = 1 + 2 + 2 = 5

    Total = 1 + 2 + 5 = 8

Complexity:
    Time: O(n**2)
    Space: O(n)
"""


# Top-down dp
from functools import lru_cache


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:

        # Sort arr so that we know when to stop searching for A and B
        arr = sorted(arr)

        # Create a set of numbers for faster checking if a number exists
        exist = set(arr)

        # Find the number of combinations of A and B that multiply to C
        @lru_cache(None)
        def combination(C):

            # Initlaize the base case to 1 because a number can always form at least 1 tree of itself
            total = 1

            # Iterate through A
            for A in arr:

                # If A is bigger than or equal to C, end the search
                if A >= C:
                    break

                # Calculate B
                B, remind = divmod(C, A)

                # If A * B == C and B exists
                if remind == 0 and B in exist:

                    # Multiple the number of combinations leading up to A with the number of combinations leading up to B and add the result to the total
                    total = (total + combination(A) * combination(B)) % 1000000007

            return total

        # Return sum of the number of combinations leading up to all C
        return sum(combination(n) for n in arr) % 1000000007


# Bottom-up dp
class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:

        # Sort arr so that we know when to stop searching for A and B
        arr = sorted(arr)

        # Cache to store the number of combinations leading up C
        cache = {C: 1 for C in arr}

        # Iterate through all possible C
        for i, C in enumerate(arr):

            # Iterate through indices from 0 to i-1
            for j in range(0, i):

                # Find A
                A = arr[j]

                # Calculate B
                B, remind = divmod(C, A)

                # If A * B == C and B exists in the arr
                if remind == 0 and B in cache:

                    # Multiple the number of combinations leading up to A with the number of combinations leading up to B and add the result the cache
                    cache[C] = (cache[C] + cache[A] * cache[B]) % 1000000007

        # Return the sum of the number of combinations leading up to all C
        return sum(cache.values()) % 1000000007

