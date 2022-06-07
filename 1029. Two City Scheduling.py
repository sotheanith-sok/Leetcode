""" 
Problem:
    A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

    Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

    Example 1:
    Input: costs = [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation: 
    The first person goes to city A for a cost of 10.
    The second person goes to city A for a cost of 30.
    The third person goes to city B for a cost of 50.
    The fourth person goes to city B for a cost of 20.

    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
    
    Example 2:
    Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    Output: 1859
    Example 3:

    Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    Output: 3086

Solution:
    We can't just iterate through the costs and pick the minimum. It won't return the true minimum cost. 
    Ex: [[10,100],[10,1000]] => output cost == 1010

    Thus, we need a better way of showing how important it is to add a person to a city. We can use the difference of the cost of going A and B to do so (A - B). If the difference is positive, it  means it is more costly for a person to go to city A than city B. If the difference is negative, it means that it is more costly for a person to go to city B than city A. Thus, we sort persons by differences and pick the lower half to be going to city A and the upper half to be going to city B.   

Complexity:
    Time: O(nlogn)
    Space: O(n)

"""


class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        # Find the number of people
        n = len(costs)

        # Keep track of the cost
        cost = 0

        # Create a list of [i, diff[i]] for ith  person
        diff = [[i, value[0] - value[1]] for i, value in enumerate(costs)]

        # Sort the list by differences. 
        diff.sort(key=lambda a: a[1])

        # Pick the lower half of the list to go to city A and the upper half to go to city B
        for i in range(n):
            cost += costs[diff[i][0]][0] if i < n / 2 else costs[diff[i][0]][1]
        
        return cost


print(
    Solution().twoCitySchedCost(
        [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    )
)

