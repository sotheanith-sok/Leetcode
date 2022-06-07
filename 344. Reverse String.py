""" 
Problem:
    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    
    Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Solution:
    Use a left and a right pointers to iterate through the list. Iterate until the left is equal to the right pointer. At each iteration, swap value at the two pointers and update the pointers. 
Complexity
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Initialize pointers.
        l, r = 0, len(s) - 1

        # Iterate until the two pointers meet.
        while l < r:

            # Swap values.
            s[l], s[r] = s[r], s[l]

            # Update pointers.
            l, r = l + 1, r - 1

