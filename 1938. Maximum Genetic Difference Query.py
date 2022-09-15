"""
Problem:
    There is a rooted tree consisting of n nodes numbered 0 to n - 1. Each node's number denotes its unique genetic value (i.e. the genetic value of node x is x). The genetic difference between two genetic values is defined as the bitwise-XOR of their values. You are given the integer array parents, where parents[i] is the parent for node i. If node x is the root of the tree, then parents[x] == -1.

    You are also given the array queries where queries[i] = [nodei, vali]. For each query i, find the maximum genetic difference between vali and pi, where pi is the genetic value of any node that is on the path between nodei and the root (including nodei and the root). More formally, you want to maximize vali XOR pi.

    Return an array ans where ans[i] is the answer to the ith query.

    Example 1:
    Input: parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]
    Output: [2,3,7]
    Explanation: The queries are processed as follows:
    - [0,2]: The node with the maximum genetic difference is 0, with a difference of 2 XOR 0 = 2.
    - [3,2]: The node with the maximum genetic difference is 1, with a difference of 2 XOR 1 = 3.
    - [2,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.
    
    Example 2:
    Input: parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]
    Output: [6,14,7]
    Explanation: The queries are processed as follows:
    - [4,6]: The node with the maximum genetic difference is 0, with a difference of 6 XOR 0 = 6.
    - [1,15]: The node with the maximum genetic difference is 1, with a difference of 15 XOR 1 = 14.
    - [0,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.

Solution:
    Use trie tree and dfs to solve this problem. Start by building an adjacency list mapped all nodes to their child and a queries dict mapped nodes to their values. Preserve the orignal position of each query so that we return the correct order of results. In order to avoid sorting results, we will use an ordered dict mapped queries position to their results.

    Start dfs through all nodes starting from the root. For each node, add it into a trie tree and calculate results of queries correspond to such node. Then, dfs through its child before removing such node from the trie tree and backtracking. 

    Finally, pray that leetcode will accept your code.

    Optimization Performed:
    1. Dynamic depth for Trie tree
    2. Use OrderedDict to avoid sorting results
    3. Iterative DFS

Complexity:
    Time: O(m n) where is m is the number of node and n is the number of queries
    Space: O (m + n)
"""

from collections import OrderedDict, defaultdict


class TrieNode:

    # Instantiate a trie node of a fix bits length
    def __init__(self, bits=0) -> None:

        # A dict mapped this trie node to its child trie nodes
        self.children = defaultdict(TrieNode)

        # A variable to keep track of the bits length starting from this node
        self.bits = bits

        # A variable to store the value correspond to bits starting from the root to this node
        self.val = None

    # Add a value into the trie node
    def add(self, val):

        # Intialize the current node
        node = self

        # Iterate through all bits of the value starting from the most significant bit
        for offset in range(self.bits - 1, -1, -1):

            # Find the current bit
            bit = (val & 1 << offset) >> offset

            # Continue to the next node based on the current bit
            node = node.children[bit]

        # Save the value at the last node
        node.val = val

    # Given a value, find an existing value in the trie node such that both values xor to the largest possible value
    def find(self, val):

        # Initialize the current node
        node = self

        # Iterate through all bits of the value starting from the most significant bit
        for offset in range(self.bits - 1, -1, -1):

            # Find the current bit
            bit = (val & 1 << offset) >> offset

            # If there exists a trie node correspond to the opposite of the current bit, go there
            # Else, go to the trie node correspond to the current bit
            node = (
                node.children[1 - bit]
                if 1 - bit in node.children
                else node.children[bit]
            )

        # Return the value of the last node
        return node.val

    # Remove a value from the trie node
    def remove(self, val):

        # DFS through the trie node
        def dfs(offset, node):

            # Stop the search once we reach -1 bit
            if offset == -1:
                return

            # Find the current bit
            bit = (val & 1 << offset) >> offset

            # Go to the child trie node base on the current bit
            dfs(offset - 1, node.children[bit])

            # If the child trie node has no children, remove the such node from the current node
            if len(node.children[bit].children) == 0:
                node.children.pop(bit)

        # Call dfs starting on the root
        dfs(self.bits - 1, self)


class Solution:
    def maxGeneticDifference(
        self, parents: list[int], queries: list[list[int]]
    ) -> list[int]:

        # Find the number of nodes and queries
        m, n = len(parents), len(queries)

        # Build an adjacency list
        root, adj = None, defaultdict(list)
        for dst, src in enumerate(parents):
            if src == -1:
                root = dst
                continue
            adj[src].append(dst)

        # Create a dict mapped nodes to their queries positions and values
        query = defaultdict(list)
        for i, (node, val) in enumerate(queries):
            query[node].append((i, val))

        # Intialize an OrderedDict to store the result
        res = OrderedDict({i: -1 for i in range(n)})

        # Intialize the trie node
        trie = TrieNode(m.bit_length())

        # Iterative DFS
        # Initalize a stack and a list of keep track of previous nodes
        stack, previous = [(-1, root)], []

        # Iterate until the stack is empty
        while stack:

            # Pop a node from the stack
            parent, node = stack.pop()

            # If the parent of the current node is not the last node in the list of previous nodes
            while previous and previous[-1] != parent:

                # Pop it from the list and remove such node from the trie node
                trie.remove(previous.pop())

            # Add the current node to the trie node
            trie.add(node)

            # Append the current node to the list of previous nodes
            previous.append(node)

            # Calculate queries correspond to the current node
            for i, val in query[node]:
                res[i] = trie.find(val) ^ val

            # Add the child of the current node onto the stack
            for nextNode in adj[node]:
                stack.append((node, nextNode))

        # Return results as a list
        return list(res.values())

