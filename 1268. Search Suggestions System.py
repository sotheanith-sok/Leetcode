""" 
Problem:
    You are given an array of strings products and a string searchWord.

    Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

    Return a list of lists of the suggested products after each character of searchWord is typed.

    Example 1:
    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
    ]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
    
    Example 2:
    Input: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    
    Example 3:
    Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
    Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Solution:
    We will use a sliding window to solve this problem. Start by sorting the products. As we input more characters, the possible solution will keep reducing. Thus, we will use two pointers to keep track of the window of possible solution. Initially, the window size will be the entire products. Then, for each input character, we will increment the left pointer and decrement the right pointer until we found a word that contain the same prefix as the input characters and we append a solution to the result. Noted that the left pointer should not pass the right pointer. Repeat until we interate through all characters in a given word.   

Complexity:
    Time: O(nlog + m + n) where n is the size of products and m is the size of a given word.
    Space: O(1)
"""


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str):

        # Sort the products
        products.sort()

        # Intialize the left and the right pointer and the result.
        l, r, res = 0, len(products) - 1, []

        # Iterate through all characters in searchWord
        for i in range(len(searchWord)):

            # Prefix from the beginning until the current character of searchWord. 
            prefix = searchWord[: i + 1]

            # Increment the left pointer until we found a word with the same prefix.
            while l <= r and products[l][: i + 1] != prefix:
                l += 1

            # Decrement the right pointer until we found a word with the same prefix.
            while l <= r and products[r][: i + 1] != prefix:
                r -= 1

            # Append the subarray to the result. Min is used since we only want at most 3 words.
            res.append(products[l : min(r + 1, l + 3)])

        return res

