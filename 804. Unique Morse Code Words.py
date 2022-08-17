"""
    Problem:
    International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

    'a' maps to ".-",
    'b' maps to "-...",
    'c' maps to "-.-.", and so on.
    For convenience, the full table for the 26 letters of the English alphabet is given below:

    [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

    For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
    Return the number of different transformations among all words we have.

    Example 1:
    Input: words = ["gin","zen","gig","msg"]
    Output: 2
    Explanation: The transformation of each word is:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."
    There are 2 different transformations: "--...-." and "--...--.".
    
    Example 2:
    Input: words = ["a"]
    Output: 1

Solution:
    Convert each word to morse code and add them to a set. Return the length of such set

Complexity:
    Time: O(mn) where m is length of words and n is the length of each word
    Space: O(m)
"""


class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:

        # Morse codes 0-25 mapped to a-z
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]


        # Initialize the set
        res = set()

        # Iterate through each word
        for word in words:

            # Create a list to store morses code of the current word 
            code = []

            # Iterate through each character
            for c in word:

                # Convert such character to a morse code and append it to the list
                code.append(morse[ord(c) - 97])

            # Convert the list to string and add it to the set
            res.add("".join(code))

        return len(res)
