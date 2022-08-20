"""
Problem:
    The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.

    Example 1:
    Input: n = 3, k = 3
    Output: "213"
    
    Example 2:
    Input: n = 4, k = 9
    Output: "2314"
    
    Example 3:
    Input: n = 3, k = 1
    Output: "123"

Solution:
    For a given list of n numbers, it contains n! permuations or (n-1)! for each number. Thus, we can simply divide k by (n-1)! to know which number we can pick as the first number. Remove such number from the list, decrement n by 1 and use the remain of k divdided by (n-1)! as the new k. Repeat until we picked n numbers. 

    ie. n = 4, k = 9 (8th permutation)
    n   k   k//(n-1)!   k mod (n-1)!    list        res
    4   8   1           3               [1,2,3,4]   [2]
    3   2   1           0               [1,3,4]     [2,3]
    2   0   0           0               [1,4]       [2,3,1]
    1   0   0           0               [4]         [2,3,1,4]         
    

Complexity:
    Time: O(n**2)
    Space: O(n)
"""

from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # Decrement k by 1 since k is between 1 and n!
        k = k - 1

        # Generate all possible numbers
        nums = list(range(1, n + 1))

        # Initialize the result
        res = []

        # Pick n numbers
        while n > 0:

            # Calculate the index of a picked number and new k
            i, k = divmod(k, factorial(n - 1))

            # Remove the picked number from nums and add it to the result
            res.append(str(nums.pop(i)))

            # Decrement n
            n -= 1

        return "".join(res)

