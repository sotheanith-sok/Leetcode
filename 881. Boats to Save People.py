""" 
Problem:
    You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.

    Example 1:
    Input: people = [1,2], limit = 3
    Output: 1
    Explanation: 1 boat (1, 2)
    
    Example 2:
    Input: people = [3,2,2,1], limit = 3
    Output: 3
    Explanation: 3 boats (1, 2), (2) and (3)
    
    Example 3:
    Input: people = [3,5,3,4], limit = 5
    Output: 4
    Explanation: 4 boats (3), (3), (4), (5)

Solution:
    Since only two people can fit in a single boat, we want to be greedy and fit the largest person with the smallest person. Thus, we sort people by weights and use two pointers. Then, if the total weight of the person in the left pointer and the right pointer is less than or equal to the limit, we can add them to the boat and move on to the next pair by increment the left pointer  and decrement the right pointer. If their weights surpass the limit, we only add the person at the right pointer to the boat aka only decrement the right pointer. We repeat the process until everyone is on a boat.  

Complexity:
    Time: O(nlogn)
    Space: O(1)
"""


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:

            l = l+1 if people[l]+people[r]<=limit else l
            r -= 1
            boats += 1
        return boats

