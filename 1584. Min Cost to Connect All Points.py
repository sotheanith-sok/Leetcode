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
from math import dist

# Prim's Algorithm
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        num_points = len(points)

        # Generate a list of nodes that any given node can visit.
        edges = {i: [j for j in range(num_points)] for i in range(num_points)}

        # Performs Prim's algorithm
        cost = 0
        min_heap = [[0, 0]]  # Cost, Node
        visited = set()

        while len(visited) != num_points:
            # Pop a node with minimum distance from visited node
            dst, node = heapq.heappop(min_heap)

            # If such node hasn't been visited
            if not node in visited:

                # Add distance to the cost
                cost += dst

                # Add the node to the visited list
                visited.add(node)

                # Add all unvisted neighboring nodes and their distance to the min heap.
                for neighbor in edges[node]:
                    if not neighbor in visited:
                        dst = abs(points[node][0] - points[neighbor][0]) + abs(
                            points[node][1] - points[neighbor][1]
                        )
                        # Push edges to the min heap [distance, node]
                        heapq.heappush(
                            min_heap, [dst, neighbor],
                        )

        return cost


# Kruskal's Algorithm - too slow for leetcode but it does work
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        # Implement Disjoint-Set data structure
        class disjoint:
            def __init__(self, n):
                # Keep track of each node's parent
                self.parents = [i for i in range(n)]

                # Keep track of the rank. A node rank increases if we use it as a parent for another node
                self.ranks = [1] * n

            def find(self, node):
                # Recursively find the parent node of a given node
                if self.parents[node] == node:
                    return node
                return self.find(self.parents[node])

            def union(self, node_1, node_2):
                # Check if you can union two nodes. Union is only possible if each node belongs to a seperate subtree
                parent_1 = self.find(node_1)
                parent_2 = self.find(node_2)

                # Union the two trees
                if parent_1 != parent_2:
                    if self.ranks[parent_1] <= self.ranks[parent_2]:
                        self.parents[parent_1] = parent_2
                        self.ranks[parent_2] += 1
                    else:
                        self.parents[parent_2] = parent_1
                        self.ranks[parent_1] += 1
                    return True
                return False

        # Generate all edges
        edges = []  # [distance, start, end]

        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dst = abs(points[i][0] - points[j][0]) + abs(
                        points[i][1] - points[j][1]
                    )
                    heapq.heappush(edges, [dst, i, j])

        # Perform Kruskal's algorithm
        dis = disjoint(len(points))
        cost = 0

        while edges:
            dst, start, end = heapq.heappop(edges)
            if dis.union(start, end):
                cost += dst

        return cost


print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))

