"""
Problem:
    You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

    You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

    Return a list of all the recipes that you can create. You may return the answer in any order.

    Note that two recipes may contain each other in their ingredients.

    Example 1:
    Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
    Output: ["bread"]
    Explanation:
    We can create "bread" since we have the ingredients "yeast" and "flour".
    
    Example 2:
    Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
    Output: ["bread","sandwich"]
    Explanation:
    We can create "bread" since we have the ingredients "yeast" and "flour".
    We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
    
    Example 3:
    Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
    Output: ["bread","sandwich","burger"]
    Explanation:
    We can create "bread" since we have the ingredients "yeast" and "flour".
    We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
    We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

Solution:
    Use topological sort with Kahn's algorithm to solve this problem. We start by generating adjacency list of items that can be use to make other items and a count which keep track of how many items needed to make an item. Then, add all items that have 0 items leading into it into a queue. Iterate until a queue is empty. Pop an item and find all items that such item lead to. Then, reduce all those items count by 1 and add any 0 count item into the queue. Any item that was popped and is in a recipes is part of a solution. 

Complexity:
    Time: O(V+E)
    Space: O(V+E)
"""

from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:

        # Intialize the adjacency list and counts
        adj = defaultdict(list)
        counts = defaultdict(int)

        # Add ingredients and recipes into the adjacency list and counts
        for ingredient, recipe in zip(ingredients, recipes):
            counts[recipe] = len(ingredient)
            for item in ingredient:
                adj[item].append(recipe)

        # Convert recipes from list to set for faster checking
        recipes = set(recipes)

        # Initialize the queue and add all supplies into it. We know that supplies do not have any item leading into it
        queue = deque(supplies)

        # Initialize the result
        res = []

        # Iterate until the queue is empty
        while queue:

            # Pop an item
            i = queue.popleft()

            # If such item is a recipe, add it to the result
            if i in recipes:
                res.append(i)

            # Reduce counts of all items that the current item lead to
            for j in adj[i]:
                counts[j] -= 1

                # If any item has its count reduced to 0, add such item to the queue
                if counts[j] == 0:
                    queue.append(j)

        return res

