""" 
Problem:
    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

    Example 1:
    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    
    Example 2:
    Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
    Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Solution:
    DFS through the graph and find paths starting from 0 node and ending at n-1 node. Save all valid paths into a list of result.

Complexity:
    Time: O(V!)
    Space: O(V)
"""


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:

        # Find the number of nodes and initialize the result
        n, res = len(graph), []

        # DFS through the graph and find all paths from 0 node to n-1 node
        def dfs(pRes, visited):

            # If we found the n-1 node, copy the path into the result
            if pRes[-1] == n - 1:
                res.append(list(pRes))
                return

            # Else, iterate through next nodes
            for nextNode in graph[pRes[-1]]:

                # If the next node is visited, skip it
                if nextNode in visited:
                    continue

                # Else, add such node into the path and mark it as visited
                pRes.append(nextNode)
                visited.add(nextNode)

                # DFS on the subpath
                dfs(pRes, visited)

                # Remove such node from the path and unmark it as visited
                pRes.pop()
                visited.remove(nextNode)

        # Call dfs starting at the 0 node
        dfs([0], set([0]))

        return res
