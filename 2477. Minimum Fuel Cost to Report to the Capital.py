"""
Problem:
    There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

    There is a meeting for the representatives of each city. The meeting is in the capital city.

    There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

    A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

    Return the minimum number of liters of fuel to reach the capital city.

    Example 1:

    Input: roads = [[0,1],[0,2],[0,3]], seats = 5
    Output: 3
    Explanation: 
    - Representative1 goes directly to the capital with 1 liter of fuel.
    - Representative2 goes directly to the capital with 1 liter of fuel.
    - Representative3 goes directly to the capital with 1 liter of fuel.
    It costs 3 liters of fuel at minimum. 
    It can be proven that 3 is the minimum number of liters of fuel needed.
    
    Example 2:
    Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
    Output: 7
    Explanation: 
    - Representative2 goes directly to city 3 with 1 liter of fuel.
    - Representative2 and representative3 go together to city 1 with 1 liter of fuel.
    - Representative2 and representative3 go together to the capital with 1 liter of fuel.
    - Representative1 goes directly to the capital with 1 liter of fuel.
    - Representative5 goes directly to the capital with 1 liter of fuel.
    - Representative6 goes directly to city 4 with 1 liter of fuel.
    - Representative4 and representative6 go together to the capital with 1 liter of fuel.
    It costs 7 liters of fuel at minimum. 
    It can be proven that 7 is the minimum number of liters of fuel needed.
    
    Example 3:
    Input: roads = [], seats = 1
    Output: 0
    Explanation: No representatives need to travel to the capital city.

Solution:
    Start by building an adjacency list of roads. Then, we will recursively calcualate the cost of transporting all representatives to city 0. For some arbitrary city, we need to sum up costs of transporting representatives to its neighboring cities with costs of transporting those people from such neighboring cities to the current city. Finally, we return the total cost and the number of people.   

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict
from math import ceil


class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:

        # Build an adjacency list of roads
        adj = defaultdict(list)

        for city1, city2 in roads:
            adj[city1].append(city2)
            adj[city2].append(city1)

        # Calculate the cost of transporting representatives to a city
        def totalCost(pCity, city):

            # Initialize the cost of transportation and the count of representatives
            cost, count = 0, 1

            # Check for previous cost and count of its neighboring cities
            for nextNode in adj[city]:

                if nextNode == pCity:
                    continue

                # Get the previous cost and count
                pCost, pCount = totalCost(city, nextNode)

                # Accumulate the cost of transporting representatives to a neighboring city plus the to transporting those people from such neighboring city to the current city
                cost += pCost + ceil(pCount / seats)

                # Accumulate the number of representatives
                count += pCount

            # Return the total cost of transportation and the total count of representatives
            return cost, count

        # Calculate the cost of transporting all representatives to city 0
        cost, _ = totalCost(-1, 0)

        return cost
