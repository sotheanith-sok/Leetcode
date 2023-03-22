"""
Problem:
    You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

    The score of a path between two cities is defined as the minimum distance of a road in this path.

    Return the minimum possible score of a path between cities 1 and n.

    Note:

    A path is a sequence of roads between two cities.
    It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
    The test cases are generated such that there is at least one path between 1 and n.
    

    Example 1:
    Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    Output: 5
    Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
    It can be shown that no other path has less score.
    
    Example 2:
    Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
    Output: 2
    Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

Solution:
    Since we can visit a city multiple times, the minimum possible score is the shortest road between two arbitrary cities in the graph that contains 1 and n.

    Thus, we can bfs through such graph to explore all roads and return the shortest road. 

Complexity:
    Time: O(E + V)
    Space: O(E + V)
"""

from collections import defaultdict, deque
from math import inf


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:

        # Build an adjacency list from the list of roads
        adj = defaultdict(list)
        for city1, city2, distance in roads:
            adj[city1].append((city2, distance))
            adj[city2].append((city1, distance))

        # Initialize the result
        res = inf

        # Initialize the queue and a set to keep track of visited cities
        # We will start from the 1st city
        queue, visited = deque([1]), set([1])

        # Iterate until the queue is empty
        while queue:

            # Find the number of cities visitable at this step
            k = len(queue)

            # Process all cities
            for _ in range(k):

                # Pop a city from the queue
                city = queue.popleft()

                # Check neighboring cities
                for nextCity, distance in adj[city]:

                    # Update the result if we found a shorter road
                    res = min(res, distance)

                    # If the next city is already visited, skip it
                    if nextCity in visited:
                        continue

                    # Else, mark it as visited and add it into the queue
                    visited.add(nextCity)
                    queue.append(nextCity)

        return res
