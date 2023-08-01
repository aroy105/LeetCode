class Twitter:
    """Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed."""
    def __init__(self):
        """Initializes your twitter object."""
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId"""
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. 
        Tweets must be ordered from most recent to least recent.
        """
        pass
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """The user with ID followerId started following the user with ID followeeId."""
        pass
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """The user with ID followerId started unfollowing the user with ID followeeId."""
        pass
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)