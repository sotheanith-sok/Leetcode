"""
Problem:
    You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

    Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

    The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

    Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

    Example 1:
    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
    Output: 60
    Explanation: 
    We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
    
    Example 2:
    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
    Output: 68
    Explanation:
    This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
    
    Example 3:
    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
    Output: 72

Solution:
    To find the max performance for some arbitrary efficiency, we need to find k people with fastest speed given that they have at least such efficiency. Thus, start by sorting people based on their efficiency and speed in an decreasing order. Iterate through all people. For each person, add their speed to a heap. If the heap exceeds k size, pop a person with the least speed. Then, calculate performance of all people in the heap. Return the largest performance.   

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: list[int], efficiency: list[int], k: int
    ) -> int:

        # Intialize a heap to keep track of people speed and a variable to keep track of their combined speed
        heap, speedSum = [], 0

        # Intialize the result
        res = 0

        # Iterate through all people from the most efficient with the higest speed 
        for efficiency, speed in sorted(zip(efficiency, speed), reverse=True):

            # Add a person to the heap and add his speed to the accumulator
            heapq.heappush(heap, speed)
            speedSum += speed

            # If there is more than k people in the heap, pop the slowest person
            if len(heap) == k + 1:
                speedSum -= heapq.heappop(heap)

            # Calculate the performance given all people in the heap
            res = max(res, speedSum * efficiency)

        return res % (10 ** 9 + 7)

