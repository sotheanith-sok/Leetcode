"""
Problem:
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);
    
    Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    
    Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    
    Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

Solution:
    Divide characters into multiple buckets based on the number of rows and merge all buckets back into the result.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Initialize the buckets
        buckets = [[] for _ in range(numRows)]

        # Initialize the steps
        steps = list(range(0, numRows)) + list(range(numRows - 2, 0, -1))

        # Start at step index 0
        i = 0

        # Iterate through all characters
        for c in s:

            # Add characters to its corresponding bucket
            buckets[steps[i]].append(c)

            # Increment i
            i = i + 1 if i < len(steps) - 1 else 0

        # Merge buckets
        # Intialize the result
        res = []

        # Add all buckets to the result
        for bucket in buckets:
            res.extend(bucket)

        return "".join(res)

