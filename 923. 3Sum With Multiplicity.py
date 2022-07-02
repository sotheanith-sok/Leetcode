""" 
Problem:
    Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

    As the answer can be very large, return it modulo 109 + 7.

    Example 1:
    Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
    Output: 20
    Explanation: 
    Enumerating by the values (arr[i], arr[j], arr[k]):
    (1, 2, 5) occurs 8 times;
    (1, 3, 4) occurs 8 times;
    (2, 2, 4) occurs 2 times;
    (2, 3, 3) occurs 2 times.
    
    Example 2:
    Input: arr = [1,1,2,2,2,2], target = 5
    Output: 12
    Explanation: 
    arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
    We choose one 1 from [1,1] in 2 ways,
    and two 2s from [2,2,2,2] in 6 ways.
    
    Example 3:
    Input: arr = [2,1,3], target = 6
    Output: 1
    Explanation: (1, 2, 3) occured one time in the array so we return 1.

Solution:
    Instead of performing backtracking and finding twoSum like Leetcode 18, we will instead use some statistic to solve this problem because we want the total combination. We will start by counting all numbers and store unique numbers and their count in a hashmap. Then, we iterate through all unique numbers using double loops to get the i and j values. Then, we can calculate the k by subtracting the two values from target. If all three values exist in the hashmap, we have three situation. 
        
        1. If i<j<k, 
            total combination = C(count[i], 1) * C(count[j], 1) * C(count[k], 1)
        
        2. If i==j!k or two values are equal, 
            total combination = C(count[i], 2) * C(count[k], 1)

        3. If i==j==k or three values are equal,
            total combination = C(count[i], 3)

Complexity:
    Time: O(n**2) where n is the unique numbers in arr
    Space: O(n)  where n is the unique numbers in arr
"""


from collections import Counter


class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:

        # Count all characters
        count = Counter(arr)

        # Initialize result
        res = 0

        # Iterate through all uniques numbers
        for i in count:
            for j in count:

                # Calculate k
                k = target - i - j

                # If i, j, and k exist in count
                if i in count and j in count and k in count:

                    # Case 1: Pick one from each value
                    if i < j < k:
                        res += count[i] * count[j] * count[k]
                    
                    # Case 2: Pick two from one value and 1 from another value
                    if i == j != k:
                        res += count[i] * (count[i] - 1) / 2 * count[k]

                    # Case 3: Pick three from one value.
                    if i == j == k:
                        res += count[i] * (count[i] - 1) * (count[i] - 2) / 6

        return int(res % 1000000007)

