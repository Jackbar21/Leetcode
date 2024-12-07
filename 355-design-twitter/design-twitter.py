class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # userId: set of userIds
        self.user_to_tweet_data = defaultdict(set) # user: set of tweet data (time, userId, tweetId)
        self.cur_time = 0

        # self.max_heap = [] # (time, userId, tweetId), where time is always unique!
        # Instead of using a global max heap as before, store a similar max heap,
        # but PER user!! This means UPDATING the news feed of OTHER users whenever a
        # tweet gets posted! To do this, we should also keep track of a 'followed_by'
        # hash-map, on top of the 'following' hash-map :)
        self.followed_by = defaultdict(set)
        self.news_feed = defaultdict(list) # userId: max-heap of posts by time similar to before :)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.tweet_to_user[tweetId] = userId
        data = (-self.cur_time, userId, tweetId)
        self.user_to_tweet_data[userId].add(data)
        self.cur_time += 1

        # Update the news feed for every user (including userId itself!)
        # that is currently following userId :)
        for user_id in self.followed_by[userId]:
            heapq.heappush(self.news_feed[user_id], data)

        # Of course, this should also belong to userId's OWN newsfeed!
        heapq.heappush(self.news_feed[userId], data)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        juicy_tweets = []
        popped_tweets = []

        max_heap = self.news_feed[userId]
        while len(max_heap) > 0:
            data = heapq.heappop(max_heap)
            _, user_id, tweetId = data

            # If no longer following, this news_feed data is irrelevant!
            if user_id != userId and user_id not in self.following[userId]:
                continue

            popped_tweets.append(data)
            juicy_tweets.append(tweetId)
            if len(juicy_tweets) == 10:
                break
        
        # Append popped data back into the heap!
        for data in popped_tweets:
            heapq.heappush(max_heap, data)

        return juicy_tweets
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # If already following, do nothing!
        if followeeId in self.following[followerId]:
            return

        # Update following status
        self.following[followerId].add(followeeId)
        self.followed_by[followeeId].add(followerId)

        # Update news feed -- follwerId is now interested in followeeId's content!
        for tweet_data in self.user_to_tweet_data[followeeId]:
            heapq.heappush(self.news_feed[followerId], tweet_data)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # If already not following, do nothing!
        if followeeId not in self.following[followerId]:
            return

        # Update following status
        self.following[followerId].discard(followeeId)
        self.followed_by[followeeId].discard(followerId)

        # Update news feed -- follwerId is NO LONGER interested in followeeId's content!
        # for tweet_data in self.user_to_tweet_data[followeeId]:
        #     heapq.heappush(self.news_feed[followerId], tweet_data)
        # EDIT: Too slow to edit heap here, so instead ignore popped items that don't belong
        # in news feed later on :)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)