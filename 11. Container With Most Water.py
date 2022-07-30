"""
Problem:
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    
    Example 2:
    Input: height = [1,1]
    Output: 1

Solution:
    Use two pointers to solve this problem. Initialize the left pointer to 0 and the right pointer to the end of height. Iterate until both pointers cross. At each iteration, calculate the area by finding the distance between the two pointers and multiply such distance with the minimum height of both pointers. Save the largest area. Increment/decrement the pointer which corresponding to the lesser of the two heights. If both heights are equal, increment the left pointer and decrement the right pointer. The last case works because the area between both pointers and their corresponding next pointers are always less than the area between the two pointers. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:

        # Initialize the left and right pointers
        l, r = 0, len(height) - 1

        # Initialize the result
        res = 0

        # Iterate until both pointers cross
        while l < r:

            # Calculate and save the largest area
            res = max(res, (r - l) * min(height[l], height[r]))

            # If the height at the left pointer is less than the height at the right pointer, increment the left pointer
            if height[l] < height[r]:
                l += 1

            # If the height at the left pointer is greater than the height at the right pointer, decrement the right pointer
            elif height[l] > height[r]:
                r -= 1

            # Else, increment the left pointer and decrement the right pointer
            else:
                l, r = l + 1, r - 1

        return res


