""" 
Problem:
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

    
    Example 1:
    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3
    Explanation:
    Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 4. Your tank = 4 - 1 + 5 = 8
    Travel to station 0. Your tank = 8 - 2 + 1 = 7
    Travel to station 1. Your tank = 7 - 3 + 2 = 6
    Travel to station 2. Your tank = 6 - 4 + 3 = 5
    Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
    Therefore, return 3 as the starting index.
    
    Example 2:
    Input: gas = [2,3,4], cost = [3,4,3]
    Output: -1
    Explanation:
    You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
    Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 0. Your tank = 4 - 3 + 2 = 3
    Travel to station 1. Your tank = 3 - 3 + 3 = 3
    You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
    Therefore, you can't travel around the circuit once no matter where you start.

Solution:
    Solve this problem using a two pointers technique. We will contiue to expanding the window as long the total sum is not negative and reduce the window when the total sum is negative. Return the index of the left pointer if the window length reaches the length of the route. Else, return -1.

    This approach works because the window length only expanding if the total sum continue to be non zero and it will reduce until the total sum is not negative.  

Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        # Find the length of the route
        n = len(gas)

        # Initialize the left and right pointers and the total sum
        l, r, total = 0, 0, 0

        # Continue to expanding the right pointer until 2n to account for a circular route
        while r < 2 * n:

            # Reduce the window length until the total sum is not negative
            while total < 0:
                total -= gas[l % n] - cost[l % n]
                l += 1

            # If the window length is same as the length of the route and the total sum is non negative, we have found a solution
            if r - l == n and total >= 0:
                return l

            # Else, expand the window
            total += gas[r % n] - cost[r % n]
            r += 1

        return -1
