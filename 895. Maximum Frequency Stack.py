""" 
Problem:
    Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

    Implement the FreqStack class:

    FreqStack() constructs an empty frequency stack.
    void push(int val) pushes an integer val onto the top of the stack.
    int pop() removes and returns the most frequent element in the stack.
    If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
    
    Example 1:
    Input
    ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
    [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    Output
    [null, null, null, null, null, null, null, 5, 7, 5, 4]
    Explanation
    FreqStack freqStack = new FreqStack();
    freqStack.push(5); // The stack is [5]
    freqStack.push(7); // The stack is [5,7]
    freqStack.push(5); // The stack is [5,7,5]
    freqStack.push(7); // The stack is [5,7,5,7]
    freqStack.push(4); // The stack is [5,7,5,7,4]
    freqStack.push(5); // The stack is [5,7,5,7,4,5]
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

Solution:
    The question asks us to create a stack sorted by frequency and then the order by which each value is added to the stack. Thus, we will use a tier stack where each tier represents the frequency of a value. When add a value to the stack, we check the frequency of such value and add it to a corresponding tier. Then, when we pop a value from the stack, we start from the last value in the highest tier first until it is empty before we go down to the next tier.  

Complexity:
    Time: O(1)
    Space: O(n)

"""


class FreqStack:
    def __init__(self):

        # Hashmap to keep track of frequency.
        self.freq = {}

        # Hashmap to keep track of tier.
        self.tiers = {}

        # A variable to keep track of the max for quicker pop.
        self.max = 0

    def push(self, val: int) -> None:

        # Increment the frequency of a given val.
        self.freq[val] = self.freq[val] + 1 if val in self.freq else 1

        # If the updated frequency excceed the max frequency, increment the max frequency.
        self.max = self.max + 1 if self.freq[val] > self.max else self.max

        # Add the val to its corresponding frequency tier.
        self.tiers[self.freq[val]] = (
            self.tiers[self.freq[val]] + [val]
            if self.freq[val] in self.tiers
            else [val]
        )

    def pop(self) -> int:

        # Pop the result from the last value in the max frequency tier.
        res = self.tiers[self.max].pop()

        # Reduce the max frequency if there is not more value at such tier.
        self.max = self.max - 1 if not self.tiers[self.max] else self.max

        # Decrement the frequency of the result.
        self.freq[res] -= 1

        return res

