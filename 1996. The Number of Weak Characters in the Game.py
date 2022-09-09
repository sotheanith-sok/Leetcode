"""
Problem:
    You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

    A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

    Return the number of weak characters.

    Example 1:
    Input: properties = [[5,5],[6,3],[3,6]]
    Output: 0
    Explanation: No character has strictly greater attack and defense than the other.
    
    Example 2:
    Input: properties = [[2,2],[3,3]]
    Output: 1
    Explanation: The first character is weak because the second character has a strictly greater attack and defense.
    
    Example 3:
    Input: properties = [[1,5],[10,4],[4,3]]
    Output: 1
    Explanation: The third character is weak because the second character has a strictly greater attack and defense.

Solution:
    Intuition:
    A bruteforce approach would require an O(n**2) running time because we have check if there exists another character who his two properties are greater than the current character. However, we can do better.

    It is hard to find a way to store all previous characters such that we can efficiently find characters that have their properties greater than some arbitrary threshold. Thus, let reduce the complexity by sorting all characters. 

    With sorted characters by attack properties, we know that every character will have his attack property greater than or equal to all previous character. So, what determine if a character is stronger than any previous character is now their defense properties. If we have 10 characters with the same attack properties, we would want to see a character with the highest defense property first because such character is going to eliminate the most out of all previous characters that have lower properties. Thus, we should also sort character based on the defense property as the second criteria. 

    Algorithm: 
    We will solve this problem using a monotonically decreasing stack. Start by sorting characters based on their attack properties in an ascending order and their defense properties in an descending order. Iterate through all characters. If there is a character on top of the stack with both properties lesser than the current character, pop it and increment the result. Then, append the character onto the stack. Lastly, return the result.

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""


class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:

        # Sort characters based on their attack properties in an ascending order and their defense properties in a descending order
        properties.sort(key=lambda x: (x[0], -x[1]))

        # Initialize the stack and result
        stack, res = [], 0

        # Iterate through all characters
        for property in properties:

            # While there is a character on top of the stack with lesser properties than the current character, pop such character and increment the result
            while stack and stack[-1][0] < property[0] and stack[-1][1] < property[1]:
                res += 1
                stack.pop()

            # Append the current character onto the stack
            stack.append(property)

        return res
