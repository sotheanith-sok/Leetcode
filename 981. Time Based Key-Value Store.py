"""
Problem:
    Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

    Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
    

    Example 1:

    Input
    ["TimeMap", "set", "get", "get", "set", "get", "get"]
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Output
    [null, null, "bar", "bar", null, "bar2", "bar2"]

    Explanation
    TimeMap timeMap = new TimeMap();
    timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
    timeMap.get("foo", 1);         // return "bar"
    timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.get("foo", 4);         // return "bar2"
    timeMap.get("foo", 5);         // return "bar2"

Solution:
    Use dict to store (key, timestamp) -> value for O(1) lookup. Create another dict to store key -> list(timestamp). Then, use binary search to find timestamp less than or equal a given timestamp and return the corresponding value. 

Complexity:
    Time: O(nlogn)
    Space: O(n)
"""

from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    def __init__(self):

        # Initialize a dict map key -> list of timestamps
        self.times = defaultdict(list)

        # Initialize a dict to map (key, timestamp) -> value
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        # Store key, timestamp, and value into the two dicts
        self.times[key].append(timestamp)
        self.values[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:

        # Find the list of timestamps belong to this key
        prevTimes = self.times[key]

        # Find the index of previous timestamp that less than or equal to the given timestamp
        idx = bisect_right(prevTimes, timestamp)

        # If there isn't one, return ""
        if idx == 0:
            return ""

        # Else, return the value
        return self.values[(key, prevTimes[idx - 1])]
