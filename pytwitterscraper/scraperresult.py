from datetime import datetime

class TwitterScraperResultProfile :
	def __init__(self,
		twitter_id: int, twitter_name: str, twitter_description: str, twitter_url: str, twitter_entities: str, twitter_follower: int, twitter_following: int, twitter_location: str, 
		twitter_createat: datetime, twitter_extended_url: str ,twitter_tweet: int, twitter_media: int, twitter_profileurl : str, twitter_bannerurl: str, twitter_profile_color: str,
		twitter_screenname: str, twitter_favourites:str, twitter_verifed: bool, twitter_pinned: bool, twitter_pinned_id: str) :
			self.id = twitter_id
			self.name = twitter_name
			self.screen_name = twitter_screenname
			self.url = twitter_url
			self.description = twitter_description
			self.location= twitter_location
			self.entities = twitter_entities
			self.verifed = twitter_verifed
			self.follower = twitter_follower
			self.following = twitter_following
			self.extended_url = twitter_extended_url
			self.tweet = twitter_tweet
			self.media = twitter_media
			self.profileurl = twitter_profileurl
			self.bannerurl = twitter_bannerurl
			self.favourites = twitter_favourites
			self.pinned = twitter_pinned
			self.pinned_id = twitter_pinned_id
			self.profile_color = twitter_profile_color
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

