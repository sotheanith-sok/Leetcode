"""
Problem:
    A car travels from a starting position to a destination which is target miles east of the starting position.

    There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

    The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

    Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

    Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

    Example 1:
    Input: target = 1, startFuel = 1, stations = []
    Output: 0
    Explanation: We can reach the target without refueling.
    
    Example 2:
    Input: target = 100, startFuel = 1, stations = [[10,100]]
    Output: -1
    Explanation: We can not reach the target (or even the first gas station).
    
    Example 3:
    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    Output: 2
    Explanation: We start with 10 liters of fuel.
    We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
    Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
    and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
    We made 2 refueling stops along the way, so we return 2.

Solution:
    Since our car is started at position 0, the maximum travelable distance is depending on its fuel. However, we can only refuel at stations between 0 and max travelable distance. If we refuel at such station, it will increase our maximum travelable distance. Thus, we can be greedily refuel only at stations that contain maximum amount of fuel until we can reach the target. 

    Use to heap to quickly find a station with a maximum amount of fuel

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""

import heapq

class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: list[list[int]]
    ) -> int:

        # Intialize the step and max travelable distance
        step, maxDist = 0, startFuel

        # Initialize the index and bound of stations
        i, n = 0, len(stations)

        # Initialize the heap
        heap = []

        # Iterate until the car reaches the target
        while maxDist < target:

            # Add all available stations to the heap
            while i < n and stations[i][0] <= maxDist:
                heapq.heappush(heap, -stations[i][1])
                i += 1

            # If there is a station that the car hasn't refuel at
            if heap:

                # Pop such station from the heap and add its fuel to the max travalable distance
                maxDist += -heapq.heappop(heap)
                step += 1

            # Else, the car isn't able to reach the next station or target
            else:
                return -1

        # Return the number of refueled station
        return step
