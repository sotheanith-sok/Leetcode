"""
Problem:
    In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

    Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

    Example 1:
    Input: n = 2, trust = [[1,2]]
    Output: 2
    
    Example 2:
    Input: n = 3, trust = [[1,3],[2,3]]
    Output: 3
    
    Example 3:
    Input: n = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

Solution:
    Keep track of people who do not trust anyone and the number of people trusted each person. Iterate through the list of given trusts and update both information. Lastly, iterate through all people that do not trust anyone and if the current person is being trust by all other people, we have found the judge.

Complexity:
    Time: O(n)
    Space: O(n)
"""


from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        # Initialize a set to keep track of people who do not trust anyone and a dict to keep track of the number of people trusted each person
        noTrust, trusted = set(range(1, n + 1)), defaultdict(int)

        # Iterate through the list of given trust and update both datasets
        for p1, p2 in trust:
            noTrust.discard(p1)
            trusted[p2] += 1

        # Iterate through the set of people who do not trust anyone
        for p in noTrust:

            # If the current person is trusted by all other people, we have found the judge
            if trusted[p] == n - 1:
                return p

        # Else, there is no judge
        return -1
