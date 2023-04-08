"""
Problem:
    Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.

    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

    class Node {
        public int val;
        public List<Node> neighbors;
    }
    

    Test case format:

    For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

    An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

    The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

    Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    
    Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
    
    Example 3:
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.

Solution:
    Maintain a dict mapping nodes' values to initialized nodes. BFS through the graph starting from the root node and copy all nodes one level at a time. Use the dict to keep track of initialized/visited nodes and two queue for processing nodes at each level for original and copied graph.

Complexity:
    Time: O(n)
    Space: O(n)
"""


from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":

        # If there is no given root node, return None
        if not node:
            return None

        # Initialize the root node of the copied graph
        root = Node(node.val)

        # Save such root node into the dict
        nodes = {node.val: root}

        # Initialize two queue: one for the original graph and one for the copied graph
        queue1, queue2 = deque([node]), deque([root])

        # Iterate until both queues are empty
        while queue1:

            # Find the number of nodes at this level
            k = len(queue1)

            # Process a pair of nodes from both queues
            for _ in range(k):

                # Pop a node from each queue
                node1, node2 = queue1.popleft(), queue2.popleft()

                # Iterate through all neighboring nodes of a parent node belonging to the orignal graph
                for nextNode in node1.neighbors:

                    # Check if we have visited such neighboring node before
                    visited = nextNode.val in nodes

                    # If not, initialize such node and save it into the dict
                    if not visited:
                        nodes[nextNode.val] = Node(nextNode.val)

                    # Copy the connection between the newly created node to the parent node of the copied graph
                    node2.neighbors.append(nodes[nextNode.val])

                    # If we have visited a neighboring node before, continue to the next node
                    if visited:
                        continue

                    # Else, add the neighboring node and its copy into both queues
                    queue1.append(nextNode)
                    queue2.append(nodes[nextNode.val])

        return root
