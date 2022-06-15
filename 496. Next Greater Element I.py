"""
Problem:
    The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

    You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

    For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

    Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

    Example 1:
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]
    Explanation: The next greater element for each value of nums1 is as follows:
    - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
    - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
    - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
    
    Example 2:
    Input: nums1 = [2,4], nums2 = [1,2,3,4]
    Output: [3,-1]
    Explanation: The next greater element for each value of nums1 is as follows:
    - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
    - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
    
Solution:
    The idea behind the optimal solution is that for a series of decreasing numbers, if we found a solution to the first value in the series, it will also be the correct solution for all values in that series. Thus, we will use a monotonic decresing stack to solve this problem. To start with, we will iterate through all values in nums2. While the value on top of the stack is less than the current value, we have found a solution to that top value on the stack and so we pop it. Then, if the current value is one of the value we trying to find a solution for, we will add it to the stack. Repeat the process until we iterate through all values in nums2. Do note that we will use a hashmap of [value in nums1: index in nums1] to know which index should we save the the solution to. 

    Ex 
       Given nums1=[4,1,2] and nums2=[1,3,4,2]
       hashmap = {4:0, 1:1, 3:2}
       result = [-1, 3, -1]


Complexity:
    Time: O(n + m) where n == len(nums1) and m == len(nums2)
    Space: O(m)

"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # Create a hashmap of [val:index] to know which index we should save the answers to.
        hashmap = {v: i for i, v in enumerate(nums1)}

        # Result array
        res = [-1] * len(nums1)

        # Monotonic Stack
        stack = []

        # Iterate through all values in nums2
        for n in nums2:

            # If the value on the top of the stack is less than the current value.
            while stack and n > stack[-1]:

                # Pop it
                val = stack.pop()

                # Find which index we should save the answer to
                i = hashmap[val]

                # Save result to the result array
                res[i] = n

            # If the current value is one of the value we are trying to find the answer to, append the value to the monotonic stack.
            if n in hashmap:
                stack.append(n)

        return res
