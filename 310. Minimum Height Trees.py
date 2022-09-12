"""
Problem:
    A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

    Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

    Return a list of all MHTs' root labels. You can return the answer in any order.

    The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

    Example 1:
    Input: n = 4, edges = [[1,0],[1,2],[1,3]]
    Output: [1]
    Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
    
    Example 2:
    Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    Output: [3,4]

Solution:
    A root node to a minimum height tree is a middle node between longest path of all nodes in a tree. If the longest path has even number nodes, there should be 2 possible root nodes and if the longest path has odd number nodes, there should only be 1 possible root node. Thus, we have to find such node.

    To find a center of the graph, we simply have to remove nodes one layer at a time. Start by creating an adjacency list and in-degree for all nodes. The outer most nodes will have an in-degree of 1 since we are working with undirected graph. Start from those nodes and use bfs to traverse the tree. For every node that we process, we will reduce the in-degree that such node contribute to its neighboring nodes by 1. Once a neighboring node has an in-degree of 1, we can add such node to the queue because it will be the outer most nodes for the next layer. All nodes processed at the last layer will be the center.

Complexity:
    Time: O(E + V)
    Space: O(V)

"""


from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        # If there is no edges, just return 0 node since len(edges) == n-1
        if not edges:
            return [0]

        # Intialize a dict to store adjacency list and in-degree for each node
        adj = defaultdict(list)
        inDegree = defaultdict(int)

        # Add all nodes into the two dicts
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

            inDegree[node1] += 1
            inDegree[node2] += 1

        # Intialize the queue and the visited set
        queue = deque(node for node in adj if inDegree[node] == 1)
        visited = set(queue)

        # Intialize the result
        res = []

        # Iterate until the queue is empty
        while queue:

            # Find the number of nodes at this layer
            n = len(queue)

            # Clear all nodes from the last layer since we haven't reach the center yet
            res.clear()

            # Iterate through all nodes at this layer
            for _ in range(n):

                # Pop a node and add it to the result
                node = queue.popleft()
                res.append(node)

                # Iterate through neighboring nodes
                for neiNode in adj[node]:

                    # If we already visit such node, skip it
                    if neiNode in visited:
                        continue

                    # Else, reduce such node indgree by
                    inDegree[neiNode] -= 1

                    # If such node has in-degree of 1, it will be the most outer node for the next layer
                    if inDegree[neiNode] == 1:

                        # Thus, add such node to the queue and mark it as visited
                        queue.append(neiNode)
                        visited.add(neiNode)

        return res

