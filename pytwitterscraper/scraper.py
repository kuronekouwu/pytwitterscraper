#coding = utf-8
import re
import time
import json
import datetime
from pprint import pprint
from requests_html import HTMLSession
from urllib.parse import urlparse
from fake_useragent import UserAgent
from .scraperresult import TwitterScraperResultProfile, TwitterScraperTrends, TwitterSearchKeywords, TwitterScraperTweets

class TwitterScraper:
	def __init__(self) :
		self.url = "https://twitter.com/"
		self.api = "https://api.twitter.com/"

		self.user_agent = UserAgent().firefox

		self.token = self.__get_token()
		self.xguest = self.__getxguesttoken()

	#Public Function
	def get_profile(self, name) -> dict :
		session = HTMLSession()
		resp = session.get(
			(self.api + f"graphql/4S2ihIKfF3xhp-ENxvUAfQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22{name}%22%2C%22withHighlightedLabel%22%3Atrue%7D"),
			headers=self.__getdataheaders()
		)
		data = resp.json()

		if resp.status_code >= 200 :
			if len(data["data"]) == 0 :
				raise Exception("Error! User Not Found!")
				return False

			dataall = data["data"]["user"]
			dataprofile = resp.json()["data"]["user"]["legacy"]

			return TwitterScraperResultProfile(
				twitter_id=dataall["rest_id"],
				twitter_name=dataprofile["name"],
				twitter_url=self.url + dataprofile["screen_name"],
				twitter_screenname=dataprofile["screen_name"],
				twitter_description=dataprofile["description"] if "description" in dataprofile else None ,
				twitter_verifed=dataprofile["verified"],
				twitter_follower=dataprofile["followers_count"],
				twitter_following=dataprofile["friends_count"] ,
				twitter_tweet=dataprofile["statuses_count"] if "statuses_count" in dataprofile else None ,
				twitter_media=dataprofile["media_count"] if "media_count" in dataprofile else None ,
				twitter_profileurl=dataprofile["profile_image_url_https"].replace("_normal","") if "profile_image_url_https" in dataprofile else None ,
				twitter_bannerurl=dataprofile["profile_banner_url"] if "profile_banner_url" in dataprofile else None,
				twitter_extended_url=dataprofile["url"] if "url" in dataprofile else None ,
				twitter_createat=datetime.datetime.strptime(dataprofile["created_at"],"%a %b %d %H:%M:%S %z %Y"),
			)

	def get_tweets(self,id: int=None,count: int=20) :
		i = 0
		tweets = []

		session = HTMLSession()
		resp = session.get(
			(self.url + f"i/api/2/timeline/profile/{id}.json?userId={id}&count={count}"),
			headers=self.__getdataheaders()
		)

		if resp.status_code >= 400 :
			raise Exception("ID User Not Found!")

		data = resp.json()
		tweetslist = data["globalObjects"]["tweets"]

		for idtweet in tweetslist :
			datatweets = tweetslist[idtweet]
			if int(datatweets["user_id_str"]) == id :
				tweets.append({
					"id" : int(datatweets["id_str"]),
					"created_at" : datetime.datetime.strptime(datatweets["created_at"],"%a %b %d %H:%M:%S %z %Y"),
					"lang" : "%s" % datatweets["lang"],
					"text" : "%s" % datatweets["full_text"] if "full_text" in datatweets else datatweets["text"],
					"hashtags" : [],
					"media" : [],
					"urls" : [],
					"likes" : int(datatweets["favorite_count"]) if "favorite_count" in datatweets else 0 ,
					"relay" : int(datatweets["reply_count"]) if "reply_count" in datatweets else 0,
					"retweet" : int(datatweets["retweet_count"]) if "retweet_count" in datatweets else 0
				})

				#Remove Enter
				tweets[i]["text"] = tweets[i]["text"].strip().replace("\n", "")

				for dataentities in datatweets["entities"] :
					if dataentities == "hashtags" :
						for datahashtags in datatweets["entities"][dataentities] :
							tweets[i]["hashtags"].append(datahashtags["text"])

					if dataentities == "media" :
						for datamedias in datatweets["entities"][dataentities] :
							tweets[i]["media"].append({
								"url" : "%s" % datamedias["url"],
								"type" : "%s" % datamedias["type"],
								"image_url" : "%s" % datamedias["media_url_https"],
								"twitter_url" : "%s" % datamedias["expanded_url"]
							})

					if dataentities == "urls" :
						for dataurls in datatweets["entities"][dataentities] :
							tweets[i]["urls"].append({
								"url" : "%s" % dataurls["url"]
							})

				i += 1

		return TwitterScraperTweets(
			twitter_data=tweets
		)

	def get_tweetinfo(self, id=None, count=20) :
		tweet = {}

		session = HTMLSession()
		resp = session.get(
			(self.url + f"i/api/2/timeline/conversation/{id}.json?tweet_mode=extended&count={count}"),
			headers=self.__getdataheaders()
		)

		if resp.status_code >= 400 :
			raise Exception("ID Tweet Not Found!")

		data = resp.json()["globalObjects"]["tweets"]["%s" % id]

		tweet.update({
			"id" : int(data["id_str"]),
			"created_at" : datetime.datetime.strptime(data["created_at"],"%a %b %d %H:%M:%S %z %Y"),
			"lang" : "%s" % data["lang"],
			"text" : "%s" % data["full_text"] if "full_text" in data else data["text"].strip("\n"),
			"hashtags" : [],
			"media" : [],
			"urls" : [],
			"likes" : int(data["favorite_count"]) if "favorite_count" in data else 0 ,
			"relay" : int(data["reply_count"]) if "reply_count" in data else 0,
			"retweet" : int(data["retweet_count"]) if "retweet_count" in data else 0
		})

		#Remove Enter
		tweet["text"] = tweet["text"].strip().replace("\n", "")

		for dataentities in data["entities"] :
			if dataentities == "hashtags" :
				for datahashtags in data["entities"][dataentities] :
					tweet["hashtags"].append(datahashtags["text"])

			if dataentities == "media" :
				for datamedias in data["entities"][dataentities] :
					tweet["media"].append({
						"url" : "%s" % datamedias["url"],
						"type" : "%s" % datamedias["type"],
						"image_url" : "%s" % datamedias["media_url_https"],
						"twitter_url" : "%s" % datamedias["expanded_url"]
					})

			if dataentities == "urls" :
				for dataurls in data["entities"][dataentities] :
					tweet["urls"].append({
						"url" : "%s" % dataurls["url"]
					})

		return TwitterScraperTweets(
			twitter_data=tweet
		)

	def get_trends(self) :
		name_trend = []

		session = HTMLSession()
		resp = session.get(
			(self.api + "2/guide.json?tcount=20&tab_category=objective_trends"),
			headers=self.__getdataheaders()
		)

		data = resp.json()

		for entryid in data["timeline"]["instructions"][1]["addEntries"]["entries"] :
			if entryid["entryId"] == "trends" :
				for items in entryid["content"]["timelineModule"]["items"] :
					name_trend.append({
						"name" : "%s" % items["item"]["content"]["trend"]["name"], 
						"description" : "%s" % items["item"]["content"]["trend"]["description"] if "description" in items["item"]["content"]["trend"] else None
					})

				break

		return TwitterScraperTrends(
			twitter_data=name_trend
		)

	def get_tweetcomments(self,id: int=None) :
		i = 0
		commants = []

		session = HTMLSession()
		resp = session.get(
			(self.url + f"i/api/2/timeline/conversation/{id}.json?tweet_mode=extended&count=20"),
			headers=self.__getdataheaders()
		)

		if resp.status_code >= 400 :
			raise Exception("ID Tweet Not Found!")
			
		data = resp.json()["globalObjects"]["tweets"]

		del data["%s" % id]

		for idtweet in data :
			datatweets = data[idtweet]
			commants.append({
				"id" : int(datatweets["id_str"]),
				"created_at" : datetime.datetime.strptime(datatweets["created_at"],"%a %b %d %H:%M:%S %z %Y"),
				"comment" : "%s" % datatweets["full_text"] if "full_text" in datatweets else datatweets["text"],
				"hashtags" : [],
				"media" : [],
				"urls" : [],
				"likes" : int(datatweets["favorite_count"]) if "favorite_count" in datatweets else 0 ,
				"relay" : int(datatweets["reply_count"]) if "reply_count" in datatweets else 0,
				"retweet" : int(datatweets["retweet_count"]) if "retweet_count" in datatweets else 0
			})

			#Remove Enter
			commants[i]["comment"] = commants[i]["comment"].strip().replace("\n", "")

			for dataentities in datatweets["entities"] :
				if dataentities == "hashtags" :
					for datahashtags in datatweets["entities"][dataentities] :
						commants[i]["hashtags"].append(datahashtags["text"])

				if dataentities == "media" :
					for datamedias in datatweets["entities"][dataentities] :
						commants[i]["media"].append({
							"url" : "%s" % datamedias["url"],
							"type" : "%s" % datamedias["type"],
							"image_url" : "%s" % datamedias["media_url_https"],
							"twitter_url" : "%s" % datamedias["expanded_url"]
						})

				if dataentities == "urls" :
					for dataurls in datatweets["entities"][dataentities] :
						commants[i]["urls"].append({
							"url" : "%s" % dataurls["url"]
						})

			i += 1
		
		return TwitterScraperTweets(
			twitter_data=commants
		)


	def searchkeywords(self, query=None) :
		i,j = 0, 0 

		users = []
		topics = []

		session = HTMLSession()
		resp = session.get(
			(self.url+ f"i/api/1.1/search/typeahead.json?q={query}&src=search_box&result_type=events%2Cusers%2Ctopics"),
			headers=self.__getdataheaders()
		)

		data = resp.json()

		for datausers in data["users"] :
			users.append({
				"name" : "%s" % datausers["name"],
				"url" : "%s" % self.url + datausers["screen_name"],
				"profileurl" : "%s" % datausers["profile_image_url"] if "profile_image_url" in datausers else None,
				"bannerurl" : "%s" % datausers["profile_image_url_https"] if "profile_image_url_https" in datausers else None,
				"screen_name" : "%s" % datausers["screen_name"],
				"tags" : []
			})

			for tags in datausers["tokens"] :
				users[i]["tags"].append(tags["token"])

			i += 1

		for datatopics in data["topics"] :
			topics.append({
				"name" : "%s" % datatopics["topic"],
				"tags" : []
			})

			for tags in datausers["tokens"] :
				topics[j]["tags"].append(tags["token"])

			j += 1

		return TwitterSearchKeywords(
			twitter_userdata=users,
			twitter_topicsdata=topics
		)

	#Private Fuction
	def __get_token(self) -> str :
		session = HTMLSession()
		resp = session.get(self.url)
		links = resp.html.find("link")

		scripts = []
		for link in links:
			if link.attrs.get("as") != "script":
				continue
			scripts.append(link.attrs.get("href"))

		#Delay Becasue Twitter Set Rate Limit :v
		time.sleep(0.5)
		main_script = list(filter(lambda u: "/main." in u, scripts))

		new = main_script[0]
		resp = session.get(new)
		token_regex = re.compile(r"A{20}.{84}")

		return token_regex.findall(resp.text)[0]

	def __getxguesttoken(self) -> str :
		session = HTMLSession()
		resp = session.post((self.api + "1.1/guest/activate.json"), headers=self.__getheaderstoken())

		return resp.json()["guest_token"]

	def __getheaderstoken(self) :
		res = {
			"Authorization" : "Bearer %s" % self.token
		}

		return res 

	def __getdataheaders(self) -> dict :
		res = {}
		res["Authorization"] = "Bearer %s" % self.token
		res["x-guest-token"] = self.xguest
		res["User-Agent"] = self.user_agent

		return res
