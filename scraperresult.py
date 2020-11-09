from datetime import datetime

class TwitterScraperResultProfile :
	def __init__(self,
		twitter_id: int, twitter_name: str, twitter_description: str, twitter_url: str, twitter_follower: int, twitter_following: int, 
		twitter_createat: datetime, twitter_extended_url: str ,twitter_tweet: int, twitter_media: int, twitter_profileurl : str, twitter_bannerurl: str,
		twitter_screenname: str, twitter_verifed: bool) :
			self.id = twitter_id
			self.name = twitter_name
			self.screenname = twitter_screenname
			self.url = twitter_url
			self.description = twitter_description
			self.verifed = twitter_verifed
			self.follower = twitter_follower
			self.following = twitter_following
			self.extended_url = twitter_extended_url
			self.tweet = twitter_tweet
			self.media = twitter_media
			self.profileurl = twitter_profileurl
			self.bannerurl = twitter_bannerurl
			self.createat = twitter_createat

class TwitterScraperTrends :
	def __init__(self,
		twitter_data: dict) :
			self.contents = twitter_data

class TwitterScraperTweets :
	def __init__(self,
		twitter_data: list) :
			self.contents = twitter_data

class TwitterSearchKeywords :
	def __init__(self,
		twitter_userdata: dict, twitter_topicsdata: dict ) :
			self.users = twitter_userdata
			self.topics = twitter_topicsdata

