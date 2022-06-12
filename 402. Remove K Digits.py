""" 
Problem:
    Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

    Example 1:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    
    Example 2:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
    
    Example 3:
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Solution:
    If numbers are in a increasing order, we want to remove from the end to create the smallest number. ie. "1,2,3,4,5", k = 2 => "1,2,3". If numbers are in a decreasing order, we want to remove from the start to create the smallest number. ie. "5,4,3,2,1", k = 2 => "3,2,1". Thus, we will use a monotonic increasing stack to solve this problem. We iterate through all number and add them to the stack. If the value at the end of the stack is largest than the current number, we pop it and increment the counter by 1 (ex: given "1,2,4,3" and k = 2, "4,3" will be a problem of decreasing order and thus, we remove 4 before adding 3 onto the stack). After iterate through all numbers, if counter still less than k, we pop numbers from the end of the stack until the counter is equal to k (ie. "1,2,3" is a problem of increasing order and thus, we remove 3). 

Complexity:
    Time: O(n)
    Space: O(n)

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        count = 0
        stack = [num[0]]

        # Remove all numbers from the front for the case of decreasing order.
        for n in num[1:]:
            while stack and stack[-1] > n and count < k:
                stack.pop()
                count += 1
            stack.append(n)

        # Remove all numbers from the end for the case of increasing order
        while count < k and stack:
            stack.pop()
            count += 1

        return str(int("".join(stack))) if stack else "0"
