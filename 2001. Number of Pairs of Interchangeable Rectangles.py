"""
Problem:
    You are given n rectangles represented by a 0-indexed 2D integer array rectangles, where rectangles[i] = [widthi, heighti] denotes the width and height of the ith rectangle.

    Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. More formally, two rectangles are interchangeable if widthi/heighti == widthj/heightj (using decimal division, not integer division).

    Return the number of pairs of interchangeable rectangles in rectangles.

    Example 1:
    Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
    Output: 6
    Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
    - Rectangle 0 with rectangle 1: 4/8 == 3/6.
    - Rectangle 0 with rectangle 2: 4/8 == 10/20.
    - Rectangle 0 with rectangle 3: 4/8 == 15/30.
    - Rectangle 1 with rectangle 2: 3/6 == 10/20.
    - Rectangle 1 with rectangle 3: 3/6 == 15/30.
    - Rectangle 2 with rectangle 3: 10/20 == 15/30.
    
    Example 2:
    Input: rectangles = [[4,5],[7,8]]
    Output: 0
    Explanation: There are no interchangeable pairs of rectangles.

Solution:
    Any rectangle can be paired with all previous rectangles with the same ratio. ie if there are 10 rectangles with the same ratio, the result would be 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 or the sum(0,..., count-1) where count = 10 in this case. 

    Thus, start by counting how many rectangles fall into each ratio. Then, calculate the number of possible pairs for each ratio using summation formula: sum(n) = n*(n+1)//2. Lastly, sum all possible pairs up for the final result.

    Since there is always inaccuracy with float division, we will reduce dividend and divisor by their gcd and use the two values as key in the map. 

Complexity:
    Time: O(nlog max(w,h)) because it takes log(max(w,h)) to calculate the gcd
    Space: O(n)
"""

from collections import defaultdict
from math import gcd


class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:

        # Initialize the dict to keep track of counts of rectangles based on their ratio
        counts = defaultdict(int)

        # Count rectangles based on its weight and height reduced by their gcp to avoid float division
        for w, h in rectangles:
            factor = gcd(w, h)
            counts[(w // factor, h // factor)] += 1

        # Calculate the sum from 1 to count - 1
        # sum(count - 1) = (count - 1) * (count - 1 + 1) // 2
        return sum((count - 1) * count // 2 for count in counts.values())

