"""
Problem:
    You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

    We repeatedly make k duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

    Example 1:
    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.
    
    Example 2:
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation: 
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"
   
    Example 3:
    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"

Solution:
    A bruteforce approach would be to rescan the string for k duplicate after every removal. But we can do better. If we scan every character in the string one at a time, we only have to check for k duplicate pattern at the end of the generated partial string. For example, given a string "aabbcc" and k = 3, the k duplicate pattern is only possible if a "c" is the next character and thus, we don't have to worry about other characters. We can use a stack to store the previous char and its count. If its count is above k, we pop it from the stack and whatever left on top of the stack will be the new end character.  

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # A stack to store previous characters and its count [char, count]
        stack = []

        # Scan through all characters
        for char in s:

            # If current character and the previous character is the same, update the count
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            
            # Else, append the current character to the stack
            else:
                stack.append([char, 1])

            # Remove the latest character if its count is bigger than or equal to k
            while stack and stack[-1][1] >= k:
                stack.pop()

        # Generate strings from the stack
        result = ""
        for char, count in stack:
            result += char * count

        return result
