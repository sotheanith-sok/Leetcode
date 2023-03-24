"""
Problem:
    There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

    Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

    This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

    Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

    It's guaranteed that each city can reach city 0 after reorder.

    Example 1:
    Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    Output: 3
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
    
    Example 2:
    Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
    Output: 2
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
    
    Example 3:
    Input: n = 3, connections = [[1,0],[2,0]]
    Output: 0

Solution:
    Since the network of cities forms a tree, we don't have to worry about cycle. BFS through the network starting from 0th city and visit all cities.  If we have found a road that go from the current city to a next city, we have found a road that need to be reversed. Return the count of such roads.

Complexity:
    Time: O(V + E)
    Space: O(V + E)
"""

from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        # Build a set to keep track of existing road's directions and an adjacency list
        directions, adj = set(), defaultdict(list)

        for city1, city2 in connections:
            adj[city1].append(city2)
            adj[city2].append(city1)
            directions.add((city1, city2))

        # Intialize the result
        res = 0

        # Initialize the queue that stores cities that is visitable at this step and a set to keep track of visited cities
        queue, visited = deque([0]), set([0])

        # Iterate until the queue is empty
        while queue:

            # Process all cities visitable at the current step
            for _ in range(len(queue)):

                # Pop a city from the queue
                city = queue.popleft()

                # Check neighboring cities
                for nextCity in adj[city]:

                    # If we already visited a neighboring city, skip it
                    if nextCity in visited:
                        continue

                    # Else, increment the result if we have found a road that needed to be reversed
                    res += int((city, nextCity) in directions)

                    # Mark such neighboring city as visited and add it into the queue
                    visited.add(nextCity)
                    queue.append(nextCity)

        return res
