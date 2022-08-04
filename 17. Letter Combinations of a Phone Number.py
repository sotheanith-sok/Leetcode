"""
Problem:
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    Example 2:
    Input: digits = ""
    Output: []
    
    Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

Solution:
    Recursively build all combinations one digit at a time. Once we processed all digits, add combinations into the result.   

Complexity:
    Time: O(3**n)
    Space: O(1)
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        # If there isn't a digit, return empty list
        if not digits:
            return []

        # Mapper of digits to characters
        mappers = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        # Initialize the result
        res = []

        # Recusively go through all digits
        def build(i, partialRes):

            nonlocal res

            # If we reached the length of digits, we have processed all digits
            if i == len(digits):

                # Add the built combination to the result
                res.append("".join(partialRes))

                return

            # Else, add characters mapped to this digit with previous partial result and recursively go on to the next character
            for c in mappers[digits[i]]:
                build(i + 1, partialRes + [c])

        build(0, [])

        return res

