""" 
Problem:
    Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

    The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

    For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
    Implement the StockSpanner class:

    StockSpanner() Initializes the object of the class.
    int next(int price) Returns the span of the stock's price given that today's price is price.
    
    Example 1:
    Input
    ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    [[], [100], [80], [60], [70], [60], [75], [85]]
    Output
    [null, 1, 1, 1, 2, 1, 4, 6]
    Explanation
    StockSpanner stockSpanner = new StockSpanner();
    stockSpanner.next(100); // return 1
    stockSpanner.next(80);  // return 1
    stockSpanner.next(60);  // return 1
    stockSpanner.next(70);  // return 2
    stockSpanner.next(60);  // return 1
    stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
    stockSpanner.next(85);  // return 6

Solution:
    Since we are looking for consecutive days where each previous day is less than the current day, we don't have to search all the previous days. Instead, we only have to search until find a previous day that is larger than the current day. Thus, we can use a monotonic decreasing stack to optimize this problem. A monotonic stack will store (price, span). While the last price is larger than the last value in the stack, we pop the last value and add its span to the last price's span. Then, we add the last price and its span onto the stack and return the span.  

Complexity:
    Time: O(n)
    Space: O(n)

"""


class StockSpanner:
    def __init__(self):
        # Monotonic decreasing stack of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # All prices have a span of 1
        span = 1

        # Pop the last value in the stack if it is less than the current price and add its span to the current price's span.
        while self.stack and self.stack[-1][0] <= price:
            _, s = self.stack.pop()
            span += s

        # Add price and its span to the stack.
        self.stack.append((price, span))

        # Return the span
        return span
