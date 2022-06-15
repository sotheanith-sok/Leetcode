""" 
Problem:
    Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

    Example 1:
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]
    
    Example 2:
    Input: nums = [1,1]
    Output: [2]

Solution:
    In order to solve this problem without using extra spaces, we will mark values as we see them. Noticed that the possible values (1-n) can be mapped 1 to 1 with indices of the nums (0-(n-1)). Thus, for each value, we will calculate the index that map to such value and change values at that index to a negative number. Since we only changes the sign of the value, we can recover the original value easily by taking its absolute value. Once, we marked all values, we will iterate through the list again find which indices haven't been marked and thus, extract our result.    

Complexity:
    Time: O(n)
    Space: O(1)

"""


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        # Mark detected values by mapping it to an index and change value at that index to negative.
        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(
                nums[index]
            )  # Use abs() here since a value can be negative or positive.

        # Find indices that do not contain a negative value and append them to the result.
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res

