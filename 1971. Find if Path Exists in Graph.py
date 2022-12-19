""" 
Problem:
    There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

    You want to determine if there is a valid path that exists from vertex source to vertex destination.

    Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

    Example 1:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    Explanation: There are two paths from vertex 0 to vertex 2:
    - 0 → 1 → 2
    - 0 → 2
    
    Example 2:
    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
    Explanation: There is no path from vertex 0 to vertex 5.

Solution:
    Build an adjacency list from all edges. Then, use dfs to traverse the graph from source node and see if we can reach the destination node.

Complexity:
    Time: O(V + E)
    Space: O(V + E)
"""

from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:

        # Build adjacency list from all edges
        # Initialize the adjacency list
        adj = defaultdict(set)

        # Iterate through all edges and add corresponding nodes into the list
        for node1, node2 in edges:
            adj[node1].add(node2)
            adj[node2].add(node1)

        # Convert set to list to faster iterative
        for node in adj:
            adj[node] = list(adj[node])

        # Start DFS to see if there is a path from the source node to the destination node
        # Initialize the stack and visited set
        stack, visited = [source], set([source])

        # Iterate until the stack is empty
        while stack:

            # Pop a node
            node = stack.pop()

            # Check if we have reach the destination node
            if node == destination:
                return True

            # If not, add next unvisited nodes into the stack
            for nextNode in adj[node]:
                if nextNode in visited:
                    continue

                visited.add(nextNode)
                stack.append(nextNode)

        # Return false if we never reach the desitnation node
        return False
