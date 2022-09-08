"""
Problem:
    Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

    The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

    Example 1:
    Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
    Output: 2
    Explanation: 
    For arr1[0]=4 we have: 
    |4-10|=6 > d=2 
    |4-9|=5 > d=2 
    |4-1|=3 > d=2 
    |4-8|=4 > d=2 
    For arr1[1]=5 we have: 
    |5-10|=5 > d=2 
    |5-9|=4 > d=2 
    |5-1|=4 > d=2 
    |5-8|=3 > d=2
    For arr1[2]=8 we have:
    |8-10|=2 <= d=2
    |8-9|=1 <= d=2
    |8-1|=7 > d=2
    |8-8|=0 <= d=2
    
    Example 2:
    Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
    Output: 2
    
    Example 3:
    Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
    Output: 1

Solution:
    A bruteforce approach to solve this problem would require a comparision between every element in arr1 with every element in arr2. This would requires O(mn) running time where m and n are lengths of arr1 and arr2 respectively.

    A better approach is to use binary search two elements in arr2 that bounded each element in the arr1.Start by sorting arr2. Then, for every element in arr1, perform binary search on arr2 to find a element lesser but cloest to the current element and another element that is equal to or greater but cloest to the current element. If both elements are more than d away from the current element, increment the result.

Complexity:
    Time: O(nlogn + mlogn) where m and n are lengths of arr1 and arr2 respectively
    Space: O(1)
"""


from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:

        # Initialize the length of arr2 and result
        n, res = len(arr2), 0

        # Sort arr2
        arr2.sort()

        # Iterate through all element in arr1
        for num in arr1:

            # Find the first index of arr2 such that we can insert the current element at and maintain a sorted order of arr2
            idx = bisect_left(arr2, num)

            # Increment the result by 1 if both bounded elements are more than d distance away from the current element
            # index - 1 will be element less than the current element
            # index will be element equal to or greater than the current element
            res += int(
                (idx - 1 < 0 or abs(arr2[idx - 1] - num) > d)
                and (idx >= n or abs(arr2[idx] - num) > d)
            )

        return res
