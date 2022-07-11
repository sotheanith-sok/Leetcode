"""
Problem:
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.

    Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    
    Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
    
    Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Solution:
    Use two pointers to solve this problem. Left pointer starts at 0 and right pointer starts at the end. Iterate until the two pointers meet. If num at left and right pointer sum up to the target, we  found the solution. Else if the sum is less than the target, we increment the left poiner. Else if the sum is larger than the target, we decrement the right pointer. This approach only works for the sorted arrays of increasing order 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # Initialzie pointers
        l, r = 0, len(numbers) - 1

        # Iterate until left and right pointers overlap
        while l < r:

            # If the sum is equal to the target, we found the solution
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            # If the sum is larger than the target, we decrement the right pointer
            elif numbers[l] + numbers[r] > target:
                r -= 1

            # If the sum is smaller than the target, we increment the left pointer
            else:
                l += 1

