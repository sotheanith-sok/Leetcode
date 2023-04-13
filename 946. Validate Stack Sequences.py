"""
Problem:
    Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

    Example 1:
    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true
    Explanation: We might do the following sequence:
    push(1), push(2), push(3), push(4),
    pop() -> 4,
    push(5),
    pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
    
    Example 2:
    Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    Output: false
    Explanation: 1 cannot be popped before 2.

Solution:
    Maintain a stack and two pointers pointed to the current value of pushed and popped sequences. Continue to push values from the pushed sequence onto the stack until we encounter a value belonging to the popped sequence. Be greedy and pop such value. We know both sequences are valid if both pointers are able to reach the end of their respective sequence.  

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:

        # Find the length of both sequences
        m, n = len(pushed), len(popped)

        # Initialize both pointers
        i, j = 0, 0

        # Initialize the stack
        stack = []

        # Iterate until both pointers reach the end of their respective sequences
        while i < m or j < n:

            # Both sequences are invalid if we are unable to reach the end of the popped sequence
            if i == m and stack and stack[-1] != popped[j]:
                return False

            # Be greedy and pop a value from the stack if it is equal to the current value of the popped sequence
            if j < n and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                continue

            # Push the current value of the pushed sequence onto the stack
            stack.append(pushed[i])
            i += 1

        return True
