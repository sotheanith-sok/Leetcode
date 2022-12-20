""" 
Problem:
    There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

    When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

    Example 1:
    Input: rooms = [[1],[2],[3],[]]
    Output: true
    Explanation: 
    We visit room 0 and pick up key 1.
    We then visit room 1 and pick up key 2.
    We then visit room 2 and pick up key 3.
    We then visit room 3.
    Since we were able to visit every room, we return true.
    
    Example 2:
    Input: rooms = [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

Solution:
    DFS from room 0 and try to visit as many rooms as possible. Return True if we visited all rooms. Else, return False.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        # Find the number of rooms
        n = len(rooms)

        # Initialize the stack and a set to keep track of visited room
        stack, visited = [0], set([0])

        # Itearte until the stack is empty
        while stack:

            # Pop a room from the stack to visit
            room = stack.pop()

            # Add next rooms that we haven't visited and add them into the stack
            for nextRoom in rooms[room]:
                if nextRoom in visited:
                    continue

                stack.append(nextRoom)
                visited.add(nextRoom)

        # Return True if we visited all rooms
        return len(visited) == n
