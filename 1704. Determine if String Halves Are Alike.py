""" 
    You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

    Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

    Return true if a and b are alike. Otherwise, return false.

    Example 1:
    Input: s = "book"
    Output: true
    Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
    
    Example 2:
    Input: s = "textbook"
    Output: false
    Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
    Notice that the vowel o is counted twice.

Solution:
    Use two pointers to solve this problem. The left pointer start at 0 and the right pointer start at length of the string - 1. Iterate until the two pointers meet. At each iteration, if a pointer points to a vowel, update its respective vowels count. Finally, return true with both vowel counters are the same. Else, false. 

Complexity:
    Time: O(n)
    Space: O(n)

"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # All possible vowels
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        # Initialize vowel counters
        leftVowelCounter = rightVowelCounter = 0

        # Initialize the left and right pointers
        l, r = 0, len(s) - 1

        # Iterate until the left and right pointers meet
        while l < r:

            # Increment the left vowel counter if the character at the left pointer is a vowel
            if s[l] in vowels:
                leftVowelCounter += 1

            # Increment the right vowel counter if the character at the right pointer is a vowel
            if s[r] in vowels:
                rightVowelCounter += 1

            # Update pointers
            l, r = l + 1, r - 1

        return leftVowelCounter == rightVowelCounter

