"""
Problem:
    You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

    Choose 2 distinct names from ideas, call them ideaA and ideaB.
    Swap the first letters of ideaA and ideaB with each other.
    If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
    Otherwise, it is not a valid name.
    Return the number of distinct valid names for the company.

    Example 1:
    Input: ideas = ["coffee","donuts","time","toffee"]
    Output: 6
    Explanation: The following selections are valid:
    - ("coffee", "donuts"): The company name created is "doffee conuts".
    - ("donuts", "coffee"): The company name created is "conuts doffee".
    - ("donuts", "time"): The company name created is "tonuts dime".
    - ("donuts", "toffee"): The company name created is "tonuts doffee".
    - ("time", "donuts"): The company name created is "dime tonuts".
    - ("toffee", "donuts"): The company name created is "doffee tonuts".
    Therefore, there are a total of 6 distinct company names.

    The following are some examples of invalid selections:
    - ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
    - ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
    - ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
    
    Example 2:
    Input: ideas = ["lack","back"]
    Output: 0
    Explanation: There are no valid selections. Therefore, 0 is returned.

Solution:
    For each idea, divide it into a leading character and suffix characters and group all ideas based on their leading character. 
    
    Then, pick two arbitrary groups and compare them. Two ideas will generate an invalid name if their suffix existed in both groups. ie: ["coffee"] and ["time", "toffee"]. Thus, exclude such idea and find the number of possible valid names generated from such groups. Repeat the process for all pair of groups.
   
Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict
from itertools import product


class Solution:
    def distinctNames(self, ideas: list[str]) -> int:

        # Initialize a hashmap mapped leading characters to their suffix characters
        groups = defaultdict(set)

        # Iterate through all ideas and group them based on their leading characters
        for idea in ideas:
            groups[idea[0]].add(idea[1:])

        # Initialize the result
        res = 0

        # Compare every possible pairs of groups
        for c1, c2 in product(groups, repeat=2):

            # Only compare groups where the first group leading character is less than the second group leading character to avoid repeated work
            if c1 >= c2:
                continue

            # Find the number of suffix characters exisited in both groups
            invalid = len(groups[c1] & groups[c2])

            # Calculate the number of valid names possible from both groups and increment the result
            res += (len(groups[c1]) - invalid) * (len(groups[c2]) - invalid)

        # Double the result to account for reversed names
        return res * 2
