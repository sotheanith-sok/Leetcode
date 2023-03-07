"""
Problem:
    You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

    Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

    You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

    Example 1:
    Input: time = [1,2,3], totalTrips = 5
    Output: 3
    Explanation:
    - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
    The total number of trips completed is 1 + 0 + 0 = 1.
    - At time t = 2, the number of trips completed by each bus are [2,1,0]. 
    The total number of trips completed is 2 + 1 + 0 = 3.
    - At time t = 3, the number of trips completed by each bus are [3,1,1]. 
    The total number of trips completed is 3 + 1 + 1 = 5.
    So the minimum time needed for all buses to complete at least 5 trips is 3.
    
    Example 2:
    Input: time = [2], totalTrips = 1
    Output: 2
    Explanation:
    There is only one bus, and it will complete its first trip at t = 2.
    So the minimum time needed to complete 1 trip is 2.

Solution:
    Use binary search to find the minimum time required for all buses to complete the given total trips where the lower bound is 1 and the upper is the time requires for the fastest buses to complete all trips solo. 
    For some arbitrary time, we can find the number of trips possible for all buses to complete in linear time by dividing the speed of each bus with such time and sum results together. 

Complexity:
    Time: O(nlogn)
    Space: O(1)
"""


from math import inf


class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:

        # Initialize the lower and upper bound of the minimum time required for all buses to complete a given trip
        lower, upper = 1, min(time) * totalTrips

        # Initialize the result
        res = inf

        # Iterate until the lower and upper bound crossed
        while lower <= upper:

            # Calculate the minimum time
            minTime = (upper - lower) // 2 + lower

            # Calcualate the number of trips possible given such minimum time
            completedTrips = sum(minTime // t for t in time)

            # If we can complete the given total trip, try to find the smaller minimum time
            if completedTrips >= totalTrips:
                res = min(res, minTime)
                upper = minTime - 1

            # Else, we should increase the minimum time
            else:
                lower = minTime + 1

        return res
