"""
Problem:
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

    Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    
    Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

Solution:
    We can easily solve this problem in O(nlogn) by iterating through numbers from 0 to n+1 and count how many 1bit in each number. However, what we will notice is that there is a lot of repeated work. For example. countBits(16) will also call countBits(8) and so on. Thus, we will restructure this problem into a dynamic programming problem. Start by initializing the cache and add in the base case. Then, we will recursively dfs through a number until we reach the base case by dividing the number by 2 everytime. At each recursive call, we also add the count of 1 bit with subsequent counts and return the partial counts. 

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def countBits(self, n: int) -> list[int]:

        # Intialize the cache and add in the base case
        cache = {0:0, 1:1}

        # DFS call
        def dfs(n):

            # If we haven't calculate this number
            if n not in cache:

                # Calculate the count of 1bit recursively
                # n & 1 is the same as n % 2
                # n >> 1 is the same as n//2 
                count = (n & 1) + dfs(n >> 1)

                # Save the count to the cache
                cache[n] = count

            return cache[n]

        return [dfs(i) for i in range(n + 1)]
