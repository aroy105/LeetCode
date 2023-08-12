from collections import defaultdict
import heapq
class Twitter:
    """Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed."""
    def __init__(self):
        """Initializes your twitter object."""
        self.count = 0 # The number of tweets, will store more recent tweets as smaller numbers
        # The count value is negative since we'll want more recent tweets, and python has a minHeap
        # Remember, this stores what number tweet that tweet is on the ENTIRE site.
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    # For this function, we can use a HashMap. Key: userId, Value: List of tweetIds
    def postTweet(self, userId: int, tweetId: int) -> None:
        """Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId"""
        # Add a new tweet for the user under the tweetMap, and store the count + tweetId
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrement the count for the next tweet
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. 
        Tweets must be ordered from most recent to least recent.
        """
        res = []
        minHeap = []
        # Add yourself as a follower, to include your own tweets for consideration,
        self.followMap[userId].add(userId)
        # Go through all the people you follow
        for followeeId in self.followMap[userId]:
            # If the person has tweeted...
            if followeeId in self.tweetMap:
                # Get the index of the most recent tweet for the person
                index = len(self.tweetMap[followeeId]) - 1
                # Store what number tweet on Twitter it is and the actual tweetId
                count, tweetId = self.tweetMap[followeeId][index]
                # For the tweet, push the following details into a single entry onto the minHeap
                # - What number tweet it is on all of twitter (where 0 is the first tweet, -1 is the second, etc)
                # - Store the tweet ID
                # - Store the person's id
                # - Store index of person's next most recent tweet, so you don't accidentally display this one again
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        # While there are tweets that exist amongst you and your followers (minHeap) and while lt ten tweets are shown
        while minHeap and len(res) < 10:
            # Get all four data points from the top of the minHeap i.e. the most recent tweet details
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # add the tweet's id to the result
            res.append(tweetId)
            # If the person has any more tweets, we want to add that as an eligible tweet for consideration
            if index >= 0:
                # For the person's next most recent tweet, grab what number tweet it was and the tweet's id
                # Remember, index stored the index of the next most recent tweet i.e. the one we're adding for consideration
                count, tweetId = self.tweetMap[followeeId][index]
                # Add all the same details we did above back into the minHeap
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
        

    # To take care of these next two functions, we can create a HashMap
    # The Key contains the user, and the Value will be the HashSet, which contains all the people they follow
    # We use a hashset since we can add and reduce from it in O(1) time
    def follow(self, followerId: int, followeeId: int) -> None:
        """The user with ID followerId started following the user with ID followeeId."""
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """The user with ID followerId started unfollowing the user with ID followeeId."""
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)