"""
Problem:
    Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

    Example 1:
    Input: nums = ["01","10"]
    Output: "11"
    Explanation: "11" does not appear in nums. "00" would also be correct.
    
    Example 2:
    Input: nums = ["00","01"]
    Output: "11"
    Explanation: "11" does not appear in nums. "10" would also be correct.
    
    Example 3:
    Input: nums = ["111","011","001"]
    Output: "101"
    Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Solution:
    Convert all numbers from binary to integer and store them in a set. Then iterate through all possible numbers for a given bits length and return the first number that doesn't exist in the set.

Complexity:
    Time: O(2**m) where m is the bits length of all numbers
    Space:O(n) where n is the length of numbers
"""


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        # Save the bits length of all numbers
        bits = len(nums[0])

        # Convert all numbers into an integer and store them in a set
        exists = set(int(num, 2) for num in nums)

        # Iterate through all possible numbers for a given bits length
        for num in range(2 ** bits):

            # If the current number doesn't exist in the set, return it as a binary string
            if num not in exists:
                return f"{{:0{bits}b}}".format(num)

