""" 
Problem:
    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

    Implement the Twitter class:

    Twitter() Initializes your twitter object.
    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
    void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
    void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
    

    Example 1:

    Input
    ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    Output
    [null, null, [5], null, null, [6, 5], null, [5]]

    Explanation
    Twitter twitter = new Twitter();
    twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2);    // User 1 follows user 2.
    twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2);  // User 1 unfollows user 2.
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

Solution:
    Use a hashmap to store followers and followees (map[followerId] -> set(followeeIds)). This ensure O(1) running time for postTweet, follow, and unfollow functions. For getNewsFeed opeartion, we will use a heap to store the most recent tweets from each followees. Once we pop the most recent tweet from top of the heap, we will add the next recent tweet from that followee onto the heap. Repeat until the heap is empty or we have 10 tweets. This approach ensure the running time will be O(n) where n is the number of users and every person is follow everyone else.  

Complexity:
    Time: O(n) where n is the number of users.
    Space: O(m+n) where n is the number of users and m is the number of tweets.
"""


import heapq


class Twitter:
    def __init__(self):
        self.users = {}  # Map followerId to a set of followeeIds
        self.tweets = {}  # Map folllowerId to a list of tweets
        self.count = 0  # Keep track of the latest tweet.

    def postTweet(self, userId: int, tweetId: int) -> None:
        # If a user tweeted before, append the new tweet to the list.
        if userId in self.tweets:
            self.tweets[userId].append([self.count, tweetId])

        # Else, initilize the tweet for a given user.
        else:
            self.tweets[userId] = [[self.count, tweetId]]
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:

        # Initialize a heap to store recent tweets
        heap = []

        # Get a list of all followees including the user themselves.
        followees = self.users[userId] | {userId} if userId in self.users else {userId}

        # Add the most recent tweet from each user to the heap
        for uid in followees:
            if uid in self.tweets:
                count, tid = self.tweets[uid][-1]

                # Also, keep track of uid and the index of next tweet for future retrival.
                heapq.heappush(heap, [count, tid, uid, len(self.tweets[uid]) - 2])

        res = []

        # while the heap isn't happen and we don't have 10 tweets
        while heap and len(res) < 10:

            # Pop the most recent tweet.
            count, tid, uid, index = heapq.heappop(heap)

            # Append the tid to the res.
            res.append(tid)

            # If there still a tweet from this user.
            if index >= 0:

                # Retrieve his next tweet and add it to the heap.
                count, tid = self.tweets[uid][index]
                heapq.heappush(heap, [count, tid, uid, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:

        # If a user follows someone before, add a followee to the set.
        if followerId in self.users:
            self.users[followerId].add(followeeId)

        # Else, initialize a set for the user.
        else:
            self.users[followerId] = set({followeeId})

    def unfollow(self, followerId: int, followeeId: int) -> None:

        # If a user follows a followee before, remove the followee.
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
