""" 
Problem:
    You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
    The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
    Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

    Example 1:
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
    Explanation: 
    We can connect the points as shown above to get the minimum cost of 20.
    Notice that there is a unique path between every pair of points.
    
    Example 2:
    Input: points = [[3,12],[-2,5],[-4,1]]
    Output: 18

Solution (Minimum Spanning Tree):
    We start by generating all edges and their associated cost. Then, we can apply Prim's or Kruskal's algorithm to generate a minimum spanning tree.
        1. Prim's algorithm - Start at any given node. Mark the node as visted. For any neighboring nodes that hasn't been visited, add their edges and weights to a min heap. Pop the closest edge from the heap and repeat the process until all nodes are visted.
        2. Kruskal's algorithm - sort all edges by weights. For each edges, use a dijoint-set (A node has a pointer to its parent) to keep track of connections. If two subsets are disjointed aka their parents are different, we will union those two sets by turning the smaller set into a child of the larger set.     

Complexity:
    Time: 
        1. O(n**2 log(n))  - cost of popping for all edges
        2. O(n**2 log(n**2)) - cost of sorting edges
    Space: O(n**2) 
"""

import heapq

# Prim's Algorithm
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)

        # Generate edges.
        edges = {i: [j for j in range(n)] for i in range(n)}

        # Performs Prim's algorithm
        cost = 0
        min_heap = [[0, 0]]  # Cost, Node
        visited = set()

        while len(visited) != n:
            # Pop a minimum edge from the min heap
            dst, node = heapq.heappop(min_heap)

            # If the edge connects to unvisited node, visit it
            if not node in visited:

                # Add distance to the cost
                cost += dst

                # Add the node to the visited list
                visited.add(node)

                # Add all edges that connect to unvisited neighbors to the min heap
                for neighbor in edges[node]:
                    if not neighbor in visited:

                        # Push edges to the min heap [distance, node]
                        heapq.heappush(
                            min_heap,
                            [
                                abs(points[node][0] - points[neighbor][0])
                                + abs(points[node][1] - points[neighbor][1]),
                                neighbor,
                            ],
                        )
        return cost


# Kruskal's Algorithm
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Generate all edges
        edges = []  # [distance, start, end]

        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dst = abs(points[i][0] - points[j][0]) + abs(
                        points[i][1] - points[j][1]
                    )
                    edges.append([dst, i, j])

        # Sort edges based on distance and reserve it
        edges.sort(key=lambda e: e[0], reverse=True)

        # Perform Kruskal's algorithm
        disjoint = [i for i in range(len(points))]

        def find(node):
            global disjoint

            if disjoint[node] == node:
                return node

            find(disjoint[node])

        while edges:
            dst, start, end = edges.pop()

            
            


print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))

