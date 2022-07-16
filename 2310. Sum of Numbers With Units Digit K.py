"""
Problem:
    Given two integers num and k, consider a set of positive integers with the following properties:

    The units digit of each integer is k.
    The sum of the integers is num.
    Return the minimum possible size of such a set, or -1 if no such set exists.

    Note:

    The set can contain multiple instances of the same integer, and the sum of an empty set is considered 0.
    The units digit of a number is the rightmost digit of the number.
    

    Example 1:
    Input: num = 58, k = 9
    Output: 2
    Explanation:
    One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
    Another valid set is [19,39].
    It can be shown that 2 is the minimum possible size of a valid set.
    
    Example 2:
    Input: num = 37, k = 2
    Output: -1
    Explanation: It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.
    
    Example 3:
    Input: num = 0, k = 7
    Output: 0
    Explanation: The sum of an empty set is considered 0.

Solution:
    The question asks us for the minimum number of numbers that ended with k needed to be sum to a target. One observation is that we can change the leading digits of all numbers to be whatever we want and thus, this isn't the limiting factor. However, the last digit will always be the multiple of k. So we need to find how many time we have to add k such that the resulting sum has the same last digit as the target's last digit. 
    A few edge case to consider. If num is 0, we have to return 0 because the empty set will be added to 0. If k is 0, we return 1 if the target is a multiple of 10. Else, return -1 because it isn't possible to sum up numbers ending with 0 to be equal to non-zero last digit of the target.   

Complexity:
    Time: O(num/k)
    Space: O(1)
"""


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:

        # If num is 0, return 0 because empty set will add up to 0
        if num == 0:
            return 0

        # If k is 0, return 1 if num is divisible by 10. Else, return -1
        if k == 0:
            return 1 if num % 10 == 0 else -1

        # Find the multiple of k such that the last digit of the resulting sum is the same as the last digit of num.
        res = 1
        total = k

        # Iterate until the sum is larger than num
        while total <= num:

            # Check if the last digits are the same
            if str(total)[-1] == str(num)[-1]:
                return res

            # Update total and result
            total, res = total + k, res + 1

        return -1

