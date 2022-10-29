""" 
Problem:
    You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. You are given two 0-indexed integer arrays plantTime and growTime, of length n each:

    plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting exactly one seed. You do not have to work on planting the same seed on consecutive days, but the planting of a seed is not complete until you have worked plantTime[i] days on planting it in total.
    growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last day of its growth, the flower blooms and stays bloomed forever.
    From the beginning of day 0, you can plant the seeds in any order.

    Return the earliest possible day where all seeds are blooming.

    Example 1:
    Input: plantTime = [1,4,3], growTime = [2,3,1]
    Output: 9
    Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
    One optimal way is:
    On day 0, plant the 0th seed. The seed grows for 2 full days and blooms on day 3.
    On days 1, 2, 3, and 4, plant the 1st seed. The seed grows for 3 full days and blooms on day 8.
    On days 5, 6, and 7, plant the 2nd seed. The seed grows for 1 full day and blooms on day 9.
    Thus, on day 9, all the seeds are blooming.
    
    Example 2:
    Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]
    Output: 9
    Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
    One optimal way is:
    On day 1, plant the 0th seed. The seed grows for 2 full days and blooms on day 4.
    On days 0 and 3, plant the 1st seed. The seed grows for 1 full day and blooms on day 5.
    On days 2, 4, and 5, plant the 2nd seed. The seed grows for 2 full days and blooms on day 8.
    On days 6 and 7, plant the 3rd seed. The seed grows for 1 full day and blooms on day 9.
    Thus, on day 9, all the seeds are blooming.
    
    Example 3:
    Input: plantTime = [1], growTime = [1]
    Output: 2
    Explanation: On day 0, plant the 0th seed. The seed grows for 1 full day and blooms on day 2.
    Thus, on day 2, all the seeds are blooming.

Solution:
    We can only work on one plant at a time, but multiple plants can grow at the same time. Thus, we can be greedy and work with plant that take the longest to grow first. 

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:

        # Pair both information and sort all plants by grow time
        info = sorted(zip(plantTime, growTime), key=lambda e: -e[1])

        # Keep track of max time to plant and grow all plants
        maxPlant, maxGrow = 0, 0

        # Itereate through all plants
        for plant, grow in info:

            # Update the max time to plant all plants
            maxPlant += plant

            # Update the max time to grow all plants
            # Add 1 because a plant only blossum on the next day
            maxGrow = max(maxGrow, maxPlant + grow + 1)

        # Subtract 1 to accond for base 0th day
        return maxGrow - 1
