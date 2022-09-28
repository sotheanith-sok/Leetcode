"""
Problem:
    You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

    Each train can only depart at an integer hour, so you may need to wait in between each train ride.

    For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
    Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

    Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

    Example 1:
    Input: dist = [1,3,2], hour = 6
    Output: 1
    Explanation: At speed 1:
    - The first train ride takes 1/1 = 1 hour.
    - Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
    - Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
    - You will arrive at exactly the 6 hour mark.
    
    Example 2:
    Input: dist = [1,3,2], hour = 2.7
    Output: 3
    Explanation: At speed 3:
    - The first train ride takes 1/3 = 0.33333 hours.
    - Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
    - Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
    - You will arrive at the 2.66667 hour mark.
    
    Example 3:
    Input: dist = [1,3,2], hour = 1.9
    Output: -1
    Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.

Solution:
    Use binary search to find a speed such that hourUsed is cloest to the hour. The range of solution is between 1 and 10**7. If hourUsed is equal to hour, return the current speed. Else if hourUsed is less than hour, we need to search the left side. Else, we search the right side. Save all hourUsed that is less than hour into the result. 

Complexity:
    Time: O(mlogn) where m in the length of distance and n is the range of solution
    Space: O(1)
"""


from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:

        # Initialize the left and right pointer
        l, r = 1, 10 ** 7

        # Initialize the result
        res = -1

        # While the left and right pointer hasn't cross each other
        while l <= r:

            # Calculate the mid pointer or the speed
            m = (r - l) // 2 + l

            # Calculate the hourUsed using current speed
            hourUsed = sum(ceil(h / m) for h in dist[:-1]) + dist[-1] / m

            # If the hourUsed is equal to hour, return the current speed
            if hourUsed == hour:
                return m

            # If hourUsed is less than hour, save the current speed into the result
            if hourUsed < hour:
                res = m

            # Search the left side if hourUsed is less than hour. Else, search the right side
            l, r = (l, m - 1) if hourUsed < hour else (m + 1, r)

        return res
