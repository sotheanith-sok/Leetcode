""" 
Problem:
    There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

    A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

    Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

    Example 1:
    Illustration of graph
    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    Output: [2,4,5,6]
    Explanation: The given graph is shown above.
    Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
    Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
    
    Example 2:
    Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    Output: [4]
    Explanation:
    Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

Solution:
    Use dfs to traverse the graph. A node is considered safe if and only if it is a terminal node or all of its neighbors are a safe node. Use hashmap to keep track of visited nodes and whether they are a safe node or not. 

Complexity:
    Time: O(E+V)
    Space: O(V)
"""


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # A hashmap used to keep track of visited nodes and if they are safe.
        n = len(graph)
        safe = {}

        # Perform Depth First Search
        def dfs(i):

            # If we visited the node before, return the previous result.
            if i in safe:
                return safe[i]

            # Since we haven't visit this node, assume it is not safe.
            safe[i] = False

            # Check all of its neighbors.
            for nei in graph[i]:
                # If at least one of the node isn't safe, return the node as unsafe.
                if not dfs(nei):
                    return False

            # Else, we know that the node is safe because it either doesn't have any neighbor or all of its neighbors are safe nodes.
            safe[i] = True
            return True

        res = []

        # For every nodes, check if it is a safe node/
        for i in range(n):

            # If it is a safe node, append the result.
            if dfs(i):
                res.append(i)

        return res


