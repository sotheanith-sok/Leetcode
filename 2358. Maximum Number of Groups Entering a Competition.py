""" 
Problem:
    You are given a positive integer array grades which represents the grades of students in a university. You would like to enter all these students into a competition in ordered non-empty groups, such that the ordering meets the following conditions:

    The sum of the grades of students in the ith group is less than the sum of the grades of students in the (i + 1)th group, for all groups (except the last).
    The total number of students in the ith group is less than the total number of students in the (i + 1)th group, for all groups (except the last).
    Return the maximum number of groups that can be formed.

    Example 1:
    Input: grades = [10,6,12,7,3,5]
    Output: 3
    Explanation: The following is a possible way to form 3 groups of students:
    - 1st group has the students with grades = [12]. Sum of grades: 12. Student count: 1
    - 2nd group has the students with grades = [6,7]. Sum of grades: 6 + 7 = 13. Student count: 2
    - 3rd group has the students with grades = [10,3,5]. Sum of grades: 10 + 3 + 5 = 18. Student count: 3
    It can be shown that it is not possible to form more than 3 groups.
    
    Example 2:
    Input: grades = [8,8]
    Output: 1
    Explanation: We can only form 1 group, since forming 2 groups would lead to an equal number of students in both groups.

Solution:
    We can be greedy and group small numbers together. Start by sorting grades and continue to add each grade until the sum of current group and the length of current group are greater than previous group. Then, we increment the number of group by 1 and start forming the next group. 

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


class Solution:
    def maximumGroups(self, grades: list[int]) -> int:

        # Sort grades
        grades = sorted(grades)

        # Initialize the result
        res = 0

        # Initialize the sum and length of the last group
        lTotal, lLen = 0, 0

        # Initialzie the sum and length of the current group
        cTotal, cLen = 0, 0

        # Iterate through all grades
        for grade in grades:

            # Add the current grade to the sum of the current group and increment the legnth by 1
            cTotal, cLen = cTotal + grade, cLen + 1

            # If the sum and length of the current groups are greater than previous groups,
            if cTotal > lTotal and cLen > lLen:

                # Increment the number of group
                res += 1

                # Update the sum and length of the last group
                lTotal, lLen = cTotal, cLen

                # Reset the sum and length of the current group
                cTotal, cLen = 0, 0

        return res
