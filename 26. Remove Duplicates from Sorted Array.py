"""
Problem:
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

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
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    
    Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Solution:
    Use two pointers to solve this problem. Left pointer will point to an available slot and right pointer will point to the current number. If current number is equal to the number to the left of the left pointer, skip it. Else, save the current number at such location and increment the left pointer. Return the left pointer as it will be equal to the number of replacement.

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # Find the length of numbers and initialize the left pointer
        n, l = len(nums), 1

        # Iterate through all number
        for r in range(1, n):

            # If the current number is equal to the number to the left of the left pointer, skip it
            if nums[l - 1] == nums[r]:
                continue

            # Else, save the current number at the left pointer and increment the left pointer
            nums[l], l = nums[r], l + 1

        return l
