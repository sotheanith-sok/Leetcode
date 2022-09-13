"""
Problem:
    There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

    You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

    Example 1:
    Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
    Output: 700
    Explanation:
    The graph is shown above.
    The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
    Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
    
    Example 2:
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
    Output: 200
    Explanation:
    The graph is shown above.
    The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
    
    Example 3:
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
    Output: 500
    Explanation:
    The graph is shown above.
    The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

Solution:
    Use dynamic programming to solve this problem. A cost to reach a node is the minmum cost among costs to reach such node from a previous node + the minimum cost to such previous node. The cost to reach the source node is always 0 and costs to reach other nodes are intialize to infinity. Since we can make at most k stops, we can at most make k+1 moves. 

    Start by converting all edges to an adjacency list (child -> parents) and calculate the minimum cost for all nodes for each move starting from 1st to kth move. 

    Ex: Given n = 11, flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]], src = 0, dst = 2, k = 4

    Thus, we can make k+1 moves

    minCosts for all nodes and moves
            0       1       2       3       4       5
    0       0       0       0       0       0       0
    1       inf     inf     101     9       4       4
    2       inf     inf     inf     201     103     11     
    3       inf     3       3       3       3       3
    4       inf     inf     6       6       6       6
    5       inf     1       1       1       1       1
    6       inf     2       2       2       2       2
    7       inf     1       1       1       1       1
    8       inf     inf     2       2       2       2
    9       inf     inf     inf     3       3       3
    10      inf     inf     inf     102     10      5

    res = min(minCosts[2]) = 11 


Complexity:
    Time: O(kn**2)
    Space: O(kn)
"""


from collections import defaultdict
from functools import lru_cache
from math import inf


# Top-down dp
class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:

        # We can make k+1 moves with k stops
        k += 1

        # Build an adjacency list mapped a child to its parents and a dict stored costs from all edges
        adj = defaultdict(list)
        costs = defaultdict(lambda: inf)
        for source, destination, cost in flights:
            adj[destination].append(source)
            costs[(source, destination)] = cost

        # Recursive function to calculate the minimum cost to reach a node at kth move
        @lru_cache(None)
        def minCost(k, node):

            # If a node is the source, return 0
            if node == src:
                return 0

            # If we reach the last move, return infinity for all nodes execpt the source node
            if k == 0:
                return inf

            # Take the minimum cost to reach such node from its parents
            return min(
                (costs[(pNode, node)] + minCost(k - 1, pNode) for pNode in adj[node]),
                default=inf,
            )

        # If there is a route between source and destination nodes, return cost. Else, return -1
        return minCost(k, dst) if minCost(k, dst) != inf else -1


# Bottom-up dp
class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:

        # Add extra move to account for 0th move
        k += 2

        # Build an adjacency list mapped a child to its parents and a dict stored costs from all edges
        adj = defaultdict(list)
        costs = defaultdict(lambda: inf)
        for source, destination, cost in flights:
            adj[destination].append(source)
            costs[(source, destination)] = cost

        # Intialize the cache to store min cost to reach all nodes for all moves
        minCosts = [[inf] * k for _ in range(n)]

        # It always cost 0 to reach the source node for every moves
        minCosts[src] = [0] * k

        # Intialize a result to keep track of minimum cost to reach the destination node
        res = inf

        # Fill in the cache starting from 1st move to k+1 move
        for k in range(1, k):

            # Iterate through all nodes
            for node in range(n):

                # Skip the source node
                if node == src:
                    continue

                # Calculate the minimum cost to reach the current node at k move with respect to its parent nodes at k-1 move
                minCosts[node][k] = min(
                    (
                        costs[(pNode, node)] + minCosts[pNode][k - 1]
                        for pNode in adj[node]
                    ),
                    default=inf,
                )

                # If we found a new minimum cost to reach the destination node, save it the result
                if node == dst:
                    res = min(res, minCosts[node][k])

        # If there is a route between source and destination nodes, return cost. Else, return -1
        return res if res != inf else -1

