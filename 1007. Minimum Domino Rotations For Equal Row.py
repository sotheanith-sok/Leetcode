""" 
Problem:
    In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

    We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

    Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

    If it cannot be done, return -1.

    Example 1:
    Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
    Output: 2
    Explanation: 
    The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
    If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

    Example 2:
    Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
    Output: -1
    Explanation: 
    In this case, it is not possible to rotate the dominoes to make one row of values equal.

Solution:
    We will performe exhaustive search through all dominoes for all possible target numbers. However, since a value has to be in all dominoes to generate a valid answer, we reduce our possible target numbers from 1-6 to the numbers in the first dominoe. Then, for each number, we will check if there is a value at the top or the bottom of a dominoe that is equal to it and if yes, we increment its respective counters. Else, we end the search early and move on to the next target. Once, we are able to iterate through all dominoes, we will return the minimum numbers of swap which is equal to the minimum of the difference between the numbers of dominoes and each count (top and bottom) of the target.    

Complexity:
    Time: O(2n) == O(n)
    Space: O(1)

"""


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        N = len(tops)

        # Add the values in the first domino to the possible targets
        targets = [tops[0], bottoms[0]]

        # Iterate through all targets
        for t in targets:

            # Initialize counters for top and bottom
            tc, bc = 0, 0

            # Iterate through all dominoes
            for i in range(N):

                # If non of the number is equal to the target, solution isn't possible. Thus, we end the search early.
                if tops[i] !=t and bottoms[i] != t:
                    break

                # Else, update its respective counter.
                tc = tc + 1 if tops[i] == t else tc
                bc = bc + 1 if bottoms[i] == t else bc

                # Return the result at the last iteration.
                if i == N-1:
                    return min(N-tc, N-bc)
            
        # If we can't find a solution, return -1.
        return -1


