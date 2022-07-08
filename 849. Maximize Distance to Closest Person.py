"""
    You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

    There is at least one empty seat, and at least one person sitting.

    Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

    Return that maximum distance to the closest person.

    Example 1:
    Input: seats = [1,0,0,0,1,0,1]
    Output: 2
    Explanation: 
    If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.
    
    Example 2:
    Input: seats = [1,0,0,0]
    Output: 3
    Explanation: 
    If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.
    
    Example 3:
    Input: seats = [0,1]
    Output: 1

Solution:
    Use two pointers to keep track of seated spot. We can find the max distance by finding the middle between thet two seated spot. There are two edges to consider. If there are a lot of empty seats in the beginning or the end, we have to take the furthest empty seat from the cloest seated spot.

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:

        # Find the numbers of seats
        n = len(seats)

        # Intitialize the left pointer
        l = 0

        # Initalize the result
        res = 0

        # Iterate through all seats using the right pointer
        for r in range(n):

            # If the current seat is not empty or we reach the last seat
            if seats[r] == 1 or r == n - 1:

                # If at least one seat is empty, we know that we are working with the edge case and thus, the max distance is the different between the two pointers
                if seats[l] == 0 or seats[r] == 0:
                    res = max(res, r - l)

                # Else, the maximum distance between two seated spots are the middle
                else:
                    res = max(res, (r - l) // 2)

                # Move the left pointer
                l = r

        return res

