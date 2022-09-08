"""
Problem:
    You are given a 0-indexed binary string s which represents the types of buildings along a street where:

    s[i] = '0' denotes that the ith building is an office and
    s[i] = '1' denotes that the ith building is a restaurant.
    As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

    For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
    Return the number of valid ways to select 3 buildings.

    Example 1:
    Input: s = "001101"
    Output: 6
    Explanation: 
    The following sets of indices selected are valid:
    - [0,2,4] from "001101" forms "010"
    - [0,3,4] from "001101" forms "010"
    - [1,2,4] from "001101" forms "010"
    - [1,3,4] from "001101" forms "010"
    - [2,4,5] from "001101" forms "101"
    - [3,4,5] from "001101" forms "101"
    No other selection is valid. Thus, there are 6 total ways.
    
    Example 2:
    Input: s = "11100"
    Output: 0
    Explanation: It can be shown that there are no valid selections.

Solution:
    There are two ways to solve this problem.
    1. Combination
    For any given digit, the number of combination can formed using such digit as the mid value is the number of opposite digit to the left multiply by the number of digit to opposite to the right. 
    
    IE if there is 4 0s to the left and 10 0s to the right, the number combination resulting in a "010" will be 40. 

    2. Dp
    Keep counts of the occurence of all possible sequence ending with each digit. ie 0s can be used to the following sequences: 0, 10, 010 and 1s can be used to form the following sequence 1, 01, 010. Iterate through all characters and keep track of occurence of all possible sequences.

    If the current digit is 0, update the occurence of 0, 10, 010 using the following formula  
        counts["0"]     +=  1
        counts["10"]    +=  counts["1"]
        counts["010"]   +=  counts["01"]

    If the current digit is 1, update the occurence of 1, 01, 010 using the following formula
        counts["1"]     +=  1
        counts["01"]    +=  counts["0"]
        counts["101"]   +=  counts["10"]

Complexity:
    Time: O(n)
    Space: O(1)
"""

from collections import Counter, defaultdict

# Combination Solution
class Solution:
    def numberOfWays(self, s: str) -> int:

        # Get length of s
        n = len(s)

        # Use two counters to keep track of the numbers of digits to the left and the right of the current number
        left, right = Counter(), Counter(s)

        # A helper to find an opposite
        opp = {"1": "0", "0": "1"}

        # Initialize i and result
        i, res = 0, 0

        # Iterate through all characters in s
        while i < n:
            
            # Count the occurence of the current digit
            count = 1
            while i < n - 1 and s[i] == s[i + 1]:
                count, i = count + 1, i + 1

            # Multiply the occuerence of the opposite digit at the left and right with the count of the current digit
            res += left[opp[s[i]]] * count * right[opp[s[i]]]

            # Update the left and right counters
            left[s[i]], right[s[i]] = left[s[i]] + count, right[s[i]] - count

            # Increment i
            i += 1

        return res

# DP Solution
class Solution:
    def numberOfWays(self, s: str) -> int:

        # Initialize a dict to keep track of counts
        counts = defaultdict(int)

        # Iterate through all characters
        for c in s:

            # If the current digit is 1, update the counts of all sequence that such digit can contribute to
            if c == "1":
                counts["1"], counts["01"], counts["101"] = (
                    counts["1"] + 1,
                    counts["01"] + counts["0"],
                    counts["101"] + counts["10"],
                )

            # Else if the current digit is 0, update the counts of all sequence that such digit can contribute to
            else:
                counts["0"], counts["10"], counts["010"] = (
                    counts["0"] + 1,
                    counts["10"] + counts["1"],
                    counts["010"] + counts["01"],
                )

        # Return the counts of sequence that we are looking for
        return counts["101"] + counts["010"]
