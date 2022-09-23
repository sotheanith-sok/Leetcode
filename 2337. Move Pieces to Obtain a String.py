"""
Problem:
    You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

    The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
    The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
    Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

    Example 1:
    Input: start = "_L__R__R_", target = "L______RR"
    Output: true
    Explanation: We can obtain the string target from start by doing the following moves:
    - Move the first piece one step to the left, start becomes equal to "L___R__R_".
    - Move the last piece one step to the right, start becomes equal to "L___R___R".
    - Move the second piece three steps to the right, start becomes equal to "L______RR".
    Since it is possible to get the string target from start, we return true.
    
    Example 2:
    Input: start = "R_L_", target = "__LR"
    Output: false
    Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
    After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
    
    Example 3:
    Input: start = "_R", target = "R_"
    Output: false
    Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.

Solution:
    Use two pointers to solve this problem. Let i and j be pointers for start and target respectively. While i and j are pointing to a blank space, increment them. Then, return False if 
    
        1. i and j point to different character or 
        2. If i pointer points to a left character that come before j pointer or 
        3. If i pointer points to a right character that come after j pointer

    Else, increment both pointers. Lastly, if one pointer reach the end, return True if both pointers reach the end. Else, return False. 

Complexity:
    Time: O(m + n) where m and n are lengths of start and target
    Space: O(1)
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:

        # Find lengths of start and target
        m, n = len(start), len(target)

        # Initialize i and j pointers
        i, j = 0, 0

        # While both pointers haven't reach the end
        while True:

            # Increment the i pointer until we see a character
            while i < m and start[i] == "_":
                i += 1

            # Increment the j pointer until we see a character
            while j < n and target[j] == "_":
                j += 1

            # If one pointer reaches the end
            if i == m or j == n:

                # Check if both pointers reach the end
                return i == m and j == n

            # Return False if
            # 1. i and j point to different character or
            # 2. If i pointer points to a left character that come before j pointer or
            # 3. If i pointer points to a right character that come after j pointer
            if (
                start[i] != target[j]
                or (start[i] == "L" and i < j)
                or (start[i] == "R" and i > j)
            ):
                return False

            # Else, increment both pointers
            i, j = i + 1, j + 1

