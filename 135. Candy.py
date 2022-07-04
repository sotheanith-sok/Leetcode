""" 
Problem:
    There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

    You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    Return the minimum number of candies you need to have to distribute the candies to the children.

    Example 1:
    Input: ratings = [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
    
    Example 2:
    Input: ratings = [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    The third child gets 1 candy because it satisfies the above two conditions.

Solution:
    We will create a cache to store how many candy will be assign to each person. Initially, all people get one candy. For the first pass, we will check from the beginning for people that have higher rating than the previous person. If yes, we give such person a max between his current candy or previous person candy plus 1. For the second pass, we will do the same as the first pass but instead of starting from the beginning, we will start from the end. Lastly, sum up the cache and return the result.   

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def candy(self, ratings: list[int]) -> int:

        # Find the number of people
        N = len(ratings)

        # Cache to store how many candies are given to each person
        cache = [1] * N

        # First pass
        # Iterate through all people from the beginning
        for i in range(1, N):

            # If the current person has a higher rating than previous person
            if ratings[i] > ratings[i - 1]:

                # Update the current person candies count
                cache[i] = max(cache[i], cache[i - 1] + 1)

        # Second pass
        # Iterate through all people from the end
        for j in range(N - 2, -1, -1):

            # If the current person has a higher rating than previous person
            if ratings[j] > ratings[j + 1]:

                # Update the current person candies count
                cache[j] = max(cache[j], cache[j + 1] + 1)

        # Sum up all candies
        return sum(cache)

