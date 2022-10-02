"""
Problem:
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    Custom Judge:

    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int val = ...; // Value to remove
    int[] expectedNums = [...]; // The expected answer with correct length.
                                // It is sorted with no values equaling val.

    int k = removeElement(nums, val); // Calls your implementation

    assert k == expectedNums.length;
    sort(nums, 0, k); // Sort the first k elements of nums
    for (int i = 0; i < actualLength; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.

    

    Example 1:

    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    Example 2:

    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    Note that the five elements can be returned in any order.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Solution:
    Intialize the i and j pointers to 0 and use them to iterate through nums. While i and j havent reach the end of nums, increment i until nums[i]==val and increment j until nums[j]!=val. Note that j must be always bigger than i. Once, we found both location, swap their values and continue. 

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        # Find the length of nums
        n = len(nums)

        # Intialize the i and j pointers
        i, j = 0, 0

        # While i and j haven't reach the end
        while i < n and j < n:

            # Increment the i pointer until nums[i] == val
            if nums[i] != val:

                # Increment i
                i += 1

                # Ensure that j pointer is greater than equal to i pointer
                j = max(j, i)
                continue

            # Increment the j pointer until nums[j] != val
            if nums[j] == val:
                j += 1
                continue

            # Swap both values
            nums[i], nums[j] = nums[j], nums[i]

            # Increment both pointers
            i, j = i + 1, j + 1

        return i

