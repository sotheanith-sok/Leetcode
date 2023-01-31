"""
Problem:
    You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

    However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

    Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

    
    Example 1:

    Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
    Output: 34
    Explanation: You can choose all the players.
    
    Example 2:
    Input: scores = [4,5,6,5], ages = [2,1,2,1]
    Output: 16
    Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
    
    Example 3:
    Input: scores = [1,2,3,5], ages = [8,9,10,1]
    Output: 6
    Explanation: It is best to choose the first 3 players. 

Solution:
    Solve this problem using dynamic programming. Before we pick any given player, we should consider picking all players of younger ages. Thus, start by sorting all players based on their ages. 
    
    Let dp be a cache containing the maximum total score if we were to pick a sequence of players ended at an arbitrary player. Iterate through all players. At each iteration, find a sequence of picked players ended at some arbitrary previous player that allow us to pick the current player and achieve the maximum total score. Finally, return the largest maximum total score.  

Complexity:
    Time: O(n**2)
    Space: O(n)
"""


class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:

        # Sort all players based on their ages
        players = sorted(zip(ages, scores))

        # Initialize the dp cache and result
        dp, res = [(0, 0, 0)], 0

        # Iterate through all players
        for age, score in players:

            # Find a sequence of picked players ended at some arbitrary previous player that allow us to pick the current player and achieve the largest total score
            totalScore, maxAge, maxScore = max(
                (totalScore, maxAge, maxScore)
                for (totalScore, maxAge, maxScore) in dp
                if age == maxAge or score >= maxScore
            )

            # Add the maximum total score achievable if we were to pick the current player
            dp.append((totalScore + score, max(maxAge, age), max(maxScore, score)))

            # Update the result
            res = max(res, totalScore + score)

        # Return the largest total score
        return res
