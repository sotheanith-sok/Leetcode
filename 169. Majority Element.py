""" 
Problem:
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Solution:
    In order to solve this problem using O(1) space, we will have to use Boyer-Moore algorithm. 
    We will initialize two varaibles to keep track of the candidate and its count. Iterate through all elements in nums. At each interation, if the count reach 0, we know that the candidate cannot be the majority element since there are other elements that make up at least half of the partial array and thus, we will set the candidate to the current num and its count to 1. Else, if the candidate is the same as the current element, we increment the count. Lastly, if the candidate is not the same as the current element, we decrement the count. 
    
Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Intialize varaibles to keep track of the candidate and its count.
        candidate, count = 0, 0

        # Iterate through all numbers
        for n in nums:

            # If the count reach 0, we know that the candidate is invalid and thus, we update the candidate to the current number and its count to 1
            if count == 0:
                candidate, count = n, 1

            # If the candidate is the same the current number, incrment its count by 1.
            elif candidate == n:
                count += 1

            # If the candidate is not equal to the current number, decrement its count by 1.
            elif candidate != n:
                count -= 1

        return candidate

