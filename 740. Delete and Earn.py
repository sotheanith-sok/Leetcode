""" 
Problem:
    You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

    Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
    Return the maximum number of points you can earn by applying the above operation some number of times.

    Example 1:
    Input: nums = [3,4,2]
    Output: 6
    Explanation: You can perform the following operations:
    - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
    - Delete 2 to earn 2 points. nums = [].
    You earn a total of 6 points.
    
    Example 2:
    Input: nums = [2,2,3,3,3,4]
    Output: 9
    Explanation: You can perform the following operations:
    - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
    - Delete a 3 again to earn 3 points. nums = [3].
    - Delete a 3 once more to earn 3 points. nums = [].
    You earn a total of 9 points.

Solution:
    We will use a cache to keep track of the earned point from 0 to each value in nums. At each iteration, we calculate the point for the current value and check if the previous value is 1 less than the current value. If yes, we take the max between the current point plus the second previous point and the previous point. Else, we add the current point with the previous point.
    Noted: we only have to keep track of the last two previous points instead of every point. 

Complexity:
    Time: O(n)
    Space: O(n)
"""
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:

        # Count how many occurences of each number
        count = Counter(nums)

        # Sort nums and eliminate duplicate.
        nums = sorted(set(nums))

        # Keep track of the second and the first previous points
        earn1, earn2 = 0, 0

        # Iterate through all values in nums
        for i in range(len(nums)):

            # Calculate the point for this value
            earn = nums[i] * count[nums[i]]

            # If there is a previous value and it was 1 less than the current value.
            if i > 0 and nums[i] == nums[i - 1] + 1:

                # Decide between the first previous point and the sum(current point + the second previous point)
                earn1, earn2 = earn2, max(earn + earn1, earn2)

            # Else, add the current point with the first previous point.
            else:
                earn1, earn2 = earn2, earn + earn2

        return earn2

