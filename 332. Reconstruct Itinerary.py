""" 
Problem:
    You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

    All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

    
    Example 1:
    Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]
    
    Example 2:
    Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Solution:
    Sort the tickets by departure and arrival. This will ensure that the resulting path will be the smallest lexical order. To start with, we will build our adjacency list where each departure is mapped to multiple arrivals. Then, we will perform DFS on the adjacency list. We will use "JFK" as the starting departure and at each iterative call, we will pick a arrival from the adjacency list and append the arrival to the result. Update the adjacency list to reflect the change. Then, we call the DFS on the arrival. Repeat the process until we used up all the tickets or reach a deadend. If we reach a deadend, we will reverse the update on the adjacency list and result and move on the next arrival.       

Complexity:
    Time: O(E**2)
    Space: O(E)
"""


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        # Sort the ticket such that the result will be the smallest lexical order.
        tickets.sort()

        # Build the adjucency list
        adj = {s: [] for s, e in tickets}
        for s, e in tickets:
            adj[s].append(e)

        # Initialize the res varaible.
        res = ["JFK"]

        # Perform the dfs
        def dfs(src):

            # The first basecase: if we found the result aka the length of res is length of tickets + 1, return True
            if len(res) == len(tickets) + 1:
                return True

            # If we reach the deadend and haven't found a result, return False.
            if src not in adj:
                return False

            # Make a copy of possible arrivals
            arrivals = list(adj[src])

            # For each arrival,
            for i, arrival in enumerate(arrivals):

                # Pop it from the adjacency list.
                adj[src].pop(i)

                # Append it to the result.
                res.append(arrival)

                # Call DFS on the arrival. If it returns true, we found our result and thus, we can return true to end the program here.
                if dfs(arrival):
                    return True

                # Else, we reverse the change to the adjacency list and the result and move to the next arrival.
                adj[src].insert(i, arrival)
                res.pop()

        dfs("JFK")

        return res

