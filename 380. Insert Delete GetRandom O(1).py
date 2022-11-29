""" 
Problem:
    Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
    You must implement the functions of the class such that each function works in average O(1) time complexity.

    Example 1:
    Input
    ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    [[], [1], [2], [2], [], [1], [2], []]
    Output
    [null, true, false, true, 2, true, false, 2]

    Explanation
    RandomizedSet randomizedSet = new RandomizedSet();
    randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
    randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
    randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
    randomizedSet.insert(2); // 2 was already in the set, so return false.
    randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Solution:
    Since we want to the add and remove operation to be of O(1), we have to use either hashset or hashmap. However, since we can't slice or index hashset or hashmap without coverting to a list (cost O(n)) when we call the random operation, we have to maintain another list. Thus, we have to use a hashmap since we need to tie values in the hash data structure to the index in the list.

    Add: If it doesn't exist in the hashmap, we append the value to the end of the list and map the val to that index in the list.

    Remove: If it does exist in the hashmap, we find the index of such value and replace it with the value at the end of the list (cost O(1) to pop from the end of the list). Then, we update the val at the end of the list to point to the index of the current value in the hashmap. Finally, we pop the current val from the hashmap and the last value the list. 

    Random: Pick an index from the list and return a value at that index.

Complexity:
    Time: O(1)
    Space: O(n)
"""

from random import randint


class RandomizedSet:
    def __init__(self):

        # Map of [val: index in the list]
        self.map = {}

        # A list to help with random
        self.list = []

    def insert(self, val: int) -> bool:

        # If it already exists, return False.
        if val in self.map:
            return False

        # Append the val to the end of the list
        self.list.append(val)

        # Add [val:index] to the map
        self.map[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:

        # If it doesn't exist, return False.
        if val not in self.map:
            return False

        # Basic Idea: Override the element that we want to remove with the last element.
        # Update the hashmap such that the last value in the list points index of the current value.
        self.map[self.list[-1]] = self.map[val]

        # Remove val from the map and pop the last value from the list.
        index = self.map.pop(val)

        # Update the list such that the value at the end of the list override the value at the index of the current value.
        self.list[index] = self.list[-1]

        self.list.pop()

        return True

    def getRandom(self) -> int:

        # Pick a random index
        index = randint(0, len(self.list) - 1)

        return self.list[index]
