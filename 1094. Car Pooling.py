""" 
Problem:
    There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

    You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

    Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

    Example 1:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false
    
    Example 2:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true

Solution:
    We start by sorting the trips based on the starting index and create a minheap to keep track of the end index and the number of passengers. Then, for every trip, we check if there exist other trips on the minheap that ended before or at the current starting index. If yes, we pop it from the minheap and add the stored number of passenger back to the capacity. Then, we subtract the current number of passengers from the capacity. If the capacity is less than 0, return False. Finally, we store the end index and the current number of passengers onto the min heap. Repeat the process for all trips. Once, we done with the loop, we return True since we never exceeded the capacity.   

Complexity:
    Time: O(nlogn)
    Space: O(nlogn)

"""


import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # Keep track of the end and its number of passengers
        ends = []  # [end_node, nums_passengers]

        # Sort the trips based on the starting index.
        trips.sort(key=lambda trip: trip[1])

        # Iterate through all trips.
        for nums_passengers, start, end in trips:

            # If there exists a trip that ended before or at the current starting index
            while ends and ends[0][0] <= start:

                # Add the stored numbers of passengers back into the capacity.  
                capacity += heapq.heappop(ends)[1]
            
            # Subtract the number of passengers from the capacity
            capacity -= nums_passengers

            # If capacity is less than 0, return False
            if capacity < 0:
                return False

            # Push the end index and the number of passengers onto the heap. 
            heapq.heappush(ends, [end, nums_passengers])

        return True

