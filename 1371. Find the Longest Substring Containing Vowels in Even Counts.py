""" 
Problem:
    Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

    Example 1:
    Input: s = "eleetminicoworoep"
    Output: 13
    Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
    
    Example 2:
    Input: s = "leetcodeisgreat"
    Output: 5
    Explanation: The longest substring is "leetc" which contains two e's.
    
    Example 3:
    Input: s = "bcbcbc"
    Output: 6
    Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

Solution:
    We don't care about the count of each vowel because if we know that if two indices have the same vowels pattern, we guarantee a valid substring between those two indices. Thus, we will use 5 bits to keep track of each detected vowel. For each character, if it is a vowel, we will xor its corresponding bits map with the pattern so far and check if such pattern exists before. If yes, we calculate the distance and update the result. Noted that if the pattern is not zero, we have to reduce the distance by 1 to exclude the lone vowel. If not, we will memorize the pattern and continue. Xor is important here because it guarantee that if we detect two vowels sequentially, it will result in a 0 bit. 
    
    Ex: Given a string "leetcodeisgreat"
    l: i = 0,   pattern = 00000,    dst = 1
    e: i = 1,   pattern = 00010,    
    e: i = 2,   pattern = 00000,    dst = 3
    t: i = 3,   pattern = 00000,    dst = 4
    c: i = 4,   pattern = 00000,    dst = 5
    o: i = 5,   pattern = 01000,    
    d: i = 6,   pattern = 01000,    dst = 1
    e: i = 7,   pattern = 01010,    
    i: i = 8,   pattern = 01110,    
    s: i = 9,   pattern = 01110,    dst = 1
    g: i = 10,  pattern = 01110,    dst = 2
    r: i = 11,  pattern = 01110,    dst = 3
    e: i = 12,  pattern = 01100,    
    a: i = 13,  pattern = 01101,
    t: i = 14,  pattern = 01101,    dst = 1

    Vowels Mapping:
    char:                               a   e   i   o   u   other
    "aeiou".find(c) + 1:                1   2   3   4   5   0
    (1 << ("aeiou".find(c) + 1)):       2   4   8   16  32  1
    (1 << ("aeiou".find(c) + 1)) >> 1:  1   2   4   8   16  0
  
Complexity:
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        # A hashmap to keep track of previously seen patterns
        seen = {0: 0}

        # Initialize the result and pattern
        res = pattern = 0

        for i, c in enumerate(s):

            # XOR pattern with the bit map of the current character
            pattern ^= (1 << ("aeiou".find(c) + 1)) >> 1

            # If we saw the pattern before
            if pattern in seen:

                # Calculate the distance. Subtract 1 to exclude the lone vowel if the pattern isn't 0.
                res = max(
                    res, i - seen[pattern] + 1 if pattern == 0 else i - seen[pattern]
                )

            # Save the pattern and the current index
            else:
                seen[pattern] = i

        return res

