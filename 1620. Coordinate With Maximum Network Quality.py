"""
Problem:
    You are given an array of network towers towers, where towers[i] = [xi, yi, qi] denotes the ith network tower with location (xi, yi) and quality factor qi. All the coordinates are integral coordinates on the X-Y plane, and the distance between the two coordinates is the Euclidean distance.

    You are also given an integer radius where a tower is reachable if the distance is less than or equal to radius. Outside that distance, the signal becomes garbled, and the tower is not reachable.

    The signal quality of the ith tower at a coordinate (x, y) is calculated with the formula ⌊qi / (1 + d)⌋, where d is the distance between the tower and the coordinate. The network quality at a coordinate is the sum of the signal qualities from all the reachable towers.

    Return the array [cx, cy] representing the integral coordinate (cx, cy) where the network quality is maximum. If there are multiple coordinates with the same network quality, return the lexicographically minimum non-negative coordinate.

    Note:

    A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either:
    x1 < x2, or
    x1 == x2 and y1 < y2.
    ⌊val⌋ is the greatest integer less than or equal to val (the floor function).
    
    Example 1:
    Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
    Output: [2,1]
    Explanation: At coordinate (2, 1) the total quality is 13.
    - Quality of 7 from (2, 1) results in ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
    - Quality of 5 from (1, 2) results in ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
    - Quality of 9 from (3, 1) results in ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
    No other coordinate has a higher network quality.
    
    Example 2:
    Input: towers = [[23,11,21]], radius = 9
    Output: [23,11]
    Explanation: Since there is only one tower, the network quality is highest right at the tower's location.
    
    Example 3:
    Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
    Output: [1,2]
    Explanation: Coordinate (1, 2) has the highest network quality.

Solution:
    Since x and y are ranged from 0 to 50, a bruteforce approaches would to calculate quality for all locations and find the lowest lexicographically (x, y) with the highest quality. This approach would take O(2500m) where m is the number of towers. However, we can be smarter with our search by taking advantage of the gradient of the quality. 
    
    Given some arbitrary location, we will check the quality of its surronding neighbors and only continue to neighbors that have quality larger than or equal to the current quality aka only search in the directions of positive or neutral gradient.

    Use bfs to traverse the grid starting from all towers.   

Complexity:
    Time: O(mn**2) where m is the number of towers and n is the possible values of x and y
    Space: O(n**2)
"""

from collections import deque
from math import floor, sqrt


class Solution:
    def bestCoordinate(self, towers: list[list[int]], radius: int) -> list[int]:
        
        # Calculate quality at a location
        def quality(x, y):

            # Intialize the overall quality to 0
            q = 0

            # Iterate through all towers
            for xT, yT, qT in towers:

                # Calculate the distance between a tower and the location
                dist = sqrt((xT - x) ** 2 + (yT - y) ** 2)

                # Add the quality of such tower to the overall quality
                q += floor(qT / (1 + dist)) if dist <= radius else 0
            
            return q

        # Use BFS to traverse the 2-d plane and find location with the higest quality

        # Initalize the queue
        queue = deque([(x, y, quality(x, y)) for x, y, _ in towers])
        
        # Initliaze the set
        visited = set([(x, y) for x, y, _ in towers])
        
        # A helper for 8-directional movement
        directions = [
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
        ]

        # Initialize the result
        resX, resY, resQ = 0, 0, -1

        # Iterate until the queue is empty
        while queue:

            # Find how many locations at this iteration
            n = len(queue)

            # Go through all locations
            for _ in range(n):

                # Pop a location
                x, y, q = queue.popleft()

                # Update the result if the current location has higher quality or lower lexicographically order
                if (q > resQ) or (q == resQ and (x < resX or (x == resX and y < resY))):
                    resX, resY, resQ = x, y, q

                # Iterate through all neighboring locations
                for dx, dy in directions:

                    # Calculate the coordinate of a neighboring location
                    neiX, neiY = x + dx, y + dy

                    # If a such location isn't out of bound and we haven't visit such location yet
                    if (
                        0 <= neiX <= 50
                        and 0 <= neiY <= 50
                        and (neiX, neiY) not in visited
                    ):
                        # Mark it as visited
                        visited.add((neiX, neiY))

                        # Calculate the quality of such location
                        neiQ = quality(neiX, neiY)

                        # If the quality of such location does not decrease compare to the current location, visit such location
                        if neiQ >= q:
                            queue.append((neiX, neiY, neiQ))

        return [resX, resY]

