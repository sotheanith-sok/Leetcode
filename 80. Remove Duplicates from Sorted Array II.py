"""
Problem:
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    Custom Judge:

    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.

    Example 1:
    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    
    Example 2:
    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
    Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Solution:
    Use two pointers approach to solve this problem. Initialize the left pointer to 0. Use the right pointer to iterate through nums. If the value at the right pointer is equal to two previous values before the left pointer, continue to the next value. Else, take the value at the right pointer and place it at the left pointer and increment the left pointer. Lastly, return the left pointer. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # Find the length of nums and initialize the left pointer
        n, l = len(nums), 0

        # Use the right pointer to iterate through nums
        for r in range(n):

            # If the value at the right pointer is equal to the two previous values before the left pointer, skip it
            if l >= 2 and nums[r] == nums[l - 1] == nums[l - 2]:
                continue

            # Else, replace the value at the left pointer with the value at the right pointer
            nums[l] = nums[r]

            # Increment the left pointer
            l += 1

        # Return the left pointer because it is the same length as used slots
        return l
