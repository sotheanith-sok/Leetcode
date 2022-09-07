"""
Problem:
    In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

    The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

    The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

    Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

    Example 1:
    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]
    
    Example 2:
    Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
    Output: [4,1]

Solution:
    To solve this problem, we need to be able to determine if by removing a edge, remaining edges will create a valid tree. There are two approaches to solve this problem.

    1.  Bruteforce:
        Start by skip each edge one at at time starting from the last edge. For each skip, check if the remanining edges make a tree by building adjacency list and make sure all nodes have no more than 1 parent. Then, run dfs on the adjacency list to check if we can visit all nodes. Since there is only one extra edge added to the tree, there will always be a node without an incoming edge when we remove an edge.

    2.  Union-find:
        Usually union-find won't be able to find a cycle in a directed graph because if two parent nodes point to a child node, union-find will indicate a cricle if we try to union the two parent nodes. 
        
        However, since we are working with a tree (all nodes have at most 1 parent), union-find will be able to find any cycle as long as there is no nodes with two incoming edges. Since, we are adding a single edge to the tree, there will either be a node with 2 incoming edges or all nodes have a single incoming edge. 

        For the first case, we remove one incoming edge and check if the tree has a cycle. If yes, return another edge.

        For the second case, we add all edges to the union-find and return the last edge that cause a cycle.
        

Complexity:
    Time: O(VE**2) for bruteforce and O(VE) for union-find
    Space: O(V + E)
"""

# Bruteforce
from collections import defaultdict

class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:

        # Find numbers of vertices and edges
        V, E = max(max(edge) for edge in edges), len(edges)

        # Check if remaining edges can make a tree
        def isTree(skip):

            # Initialize the adjacency list
            adj = defaultdict(list)

            # Initialize a set to keep track of nodes that have no parent
            noParent = set(range(1, V + 1))

            # Iterate through all edges
            for i in range(E):

                # Skip an edge
                if i == skip:
                    continue

                # Find the src and dst vertices
                src, dst = edges[i]

                # If there are more than 1 incoming edges to a vertex, return False
                if dst not in noParent:
                    return False

                # Add edge to the adjacency list
                adj[src].append(dst)

                # Mark the current dst vertex as has parent
                noParent.remove(dst)

            # Use dfs to check if there is a cycle
            # Initlaize the stack and visited set
            stack = list(noParent)
            visited = set(stack)

            # Iterate until stack is empty
            while stack:

                # Pop a vertex
                vertex = stack.pop()

                # Iterate through neighboring vertices
                for nextVertex in adj[vertex]:

                    # If we visited a neighboring vertex already, there is a cycle
                    if nextVertex in visited:
                        return False

                    # Add the neighboring vertex to the stack
                    visited.add(nextVertex)

                    # Mark such vertex as visited
                    stack.append(nextVertex)

            # Check if we were able to visit all vertices
            return len(visited) == V

        # Skip all edges one a time and check if we can make a tree with reamining edges
        for i in range(E - 1, -1, -1):
            if isTree(i):
                return edges[i]


# Union-Find
from collections import defaultdict

class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:

        # Implementation of union-find
        class UnionFind:
            def __init__(self):

                # A dict to keep track of roots of each node
                self.roots = {}

            # Recursively find the root node of a node
            def find(self, x):
                if self.roots.get(x, x) == x:
                    return x

                return self.find(self.roots[x])

            # Union two nodes
            def union(self, x, y):

                # Find roots of both nodes
                rootX, rootY = self.find(x), self.find(y)

                # If roots are different, union them
                if rootX != rootY:
                    self.roots[y] = rootX
                    return True

                # Else, return False
                return False

        # Find vertice that have two in-edges
        # Get the number of edges
        E = len(edges)

        # Initialize a dict to keep track of incoming edges to each vertex
        inEdges = defaultdict(list)

        # Initialize to keep track of a vertex that has two incoming edges
        twoIncomingEdges = None

        # Iterate through all edges
        for i in range(E):

            _, dst = edges[i]

            # Add the index of an edge to the dict based on the destination vertex
            inEdges[dst].append(i)

            # If a vertex has more than 1 incoming edges, save it and end the search
            if len(inEdges[dst]) == 2:
                twoIncomingEdges = inEdges[dst]
                break

        # Use union find to detect a cycle
        # Initialize the union-find
        uf = UnionFind()

        # Iterate through all edges
        for i in range(E):

            # Get the source and desitnation vertices
            src, dst = edges[i]

            # If there is a vertex with two incoming edges and the current edge is the second incoming edge of such vertex, skip it
            if twoIncomingEdges and i == twoIncomingEdges[1]:
                continue

            # Union the two vertices
            if not uf.union(src, dst):

                # If there was a vertex with two incoming edges, return the first incoming edge as skipping the second incoming edge does not remove the cycle.
                # Else, return the current edge that cause the cycle 
                return edges[i] if not twoIncomingEdges else edges[twoIncomingEdges[0]]

        # If there is no cycle, return the second incoming edge
        return edges[twoIncomingEdges[1]]
