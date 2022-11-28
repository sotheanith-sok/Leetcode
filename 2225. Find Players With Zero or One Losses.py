""" 
Problem:
    You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

    Return a list answer of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.
    The values in the two lists should be returned in increasing order.

    Note:

    You should only consider the players that have played at least one match.
    The testcases will be generated such that no two matches will have the same outcome.
    

    Example 1:
    Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    Output: [[1,2,10],[4,5,7,8]]
    Explanation:
    Players 1, 2, and 10 have not lost any matches.
    Players 4, 5, 7, and 8 each have lost one match.
    Players 3, 6, and 9 each have lost two matches.
    Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
    
    Example 2:
    Input: matches = [[2,3],[1,3],[5,4],[6,4]]
    Output: [[1,2,5,6],[]]
    Explanation:
    Players 1, 2, 5, and 6 have not lost any matches.
    Players 3 and 4 each have lost two matches.
    Thus, answer[0] = [1,2,5,6] and answer[1] = [].

Solution:
    Iterate through all matches and count how many time each player loses. Then, iterate through the counts and find players that never lose and players who lose at most one matches. Return both lists sorted alphabetically (We sort here to reduce sorting space by eliminating players with more than one lost). 

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""

from collections import defaultdict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:

        # Initialize a dict to store each player's lost count
        scores = defaultdict(int)

        # Iterate through all matches and save players scores into the dict
        for winner, loser in matches:
            if winner not in scores:
                scores[winner] = 0
            scores[loser] += 1

        # Intialize two lists to store players that never lose and players that lose at most one match
        winners, lostOne = [], []

        # Iterate through players and their counts and save them into both lists
        for player, score in scores.items():
            if score == 0:
                winners.append(player)
            
            if score == 1:
                lostOne.append(player)

        # Return both lists sorted alphabetically 
        return [sorted(winners), sorted(lostOne)]
