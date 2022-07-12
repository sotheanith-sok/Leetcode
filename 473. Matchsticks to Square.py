"""
Problem:
    You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

    Return true if you can make this square and false otherwise.

    Example 1:
    Input: matchsticks = [1,1,2,2,2]
    Output: true
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

    Example 2:
    Input: matchsticks = [3,3,3,3,4]
    Output: false
    Explanation: You cannot find a way to form a square with all the matchsticks.

Solution:
    This problem is the same as leetcode 698 where we have to check if we can divide an array into k equal partition. k in this case in 4. The idea is simple. If it is possible to divide an array into k partition, then there is a way to add all numbers such that it will never surpass the size of each partition and the final sum will be zero if we mod the partial sum by the size of the partition.

    We will DFS through all possible order of numbers and use a bitmask to keep track of which number is still available. At each iteration, we pick a number and calculate the partial sum on the remaining number. If the partial sum and the current number sum up to a value larger than the size of the partition, we know this order of addition is invalid and thus, return -1. Else, we mod the sum of the two and return it. Lastly, if the dfs return 0, we know that this array can be partition into k equal partition. 

Complexity:
    Time: O(2^n)
    Space: O(2^n)
"""


from functools import lru_cache


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        
        # Find the number of sticks
        N = len(matchsticks)

        # Find the size of each partition if we split the arrays into 4
        partition, rem = divmod(sum(matchsticks), 4)

        # Return false if it isn't possible create 4 equal partitions
        if rem != 0 or max(matchsticks) > partition:
            return False

        # Caching based on bitmask
        @lru_cache(None)
        def dfs(mask):

            # If mask is 0, we used all numbers
            if mask == 0:
                return 0

            # Iterate through all numbers
            for j in range(N):

                # A number is still available if its bit is 1
                if mask & 1 << j:

                    # DFS through the remaining numbers
                    partialSum = dfs(mask ^ 1 << j)

                    # If the partial sum is not zero and adding the partial sum with the current number is less than or equal to the size of a partition
                    if partialSum >= 0 and partialSum + matchsticks[j] <= partition:

                        # We can add this number to the partial sum. Mod the result by the size of the partition. We will only surpass the partition size if the addition order is invalid. 
                        return (partialSum + matchsticks[j]) % partition
            
            # Return -1 if we can't find a valid addition order starting from this bitmask. 
            return -1

        # Start with bitmask of 1111111....
        return dfs((1 << N) - 1) == 0
