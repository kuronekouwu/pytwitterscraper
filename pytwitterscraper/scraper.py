#coding = utf-8
import re
import time
import json
import datetime
import requests
import random
import importlib.resources
import os
from requests_html import HTMLSession
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from .scraperresult import TwitterScraperResultProfile, TwitterScraperTrends, TwitterSearchKeywords, TwitterScraperTweets

class TwitterScraper:
	def __init__(self, proxy_enable=False, proxy_http=None, proxy_https=None) :
		# Disable Waring Text
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

		self.url = "https://twitter.com/"
		self.api = "https://api.twitter.com/"

		#Target URL
		self.profile = "1.1/users/lookup.json?{}={}"

		self.user_agent = self.__load_user_agent()

		self.proxy_enable = proxy_enable
		self.proxy_http = "http://" + str(proxy_http)
		self.proxy_https = "https://" + str(proxy_https)

		self.token = self.__get_token()
		self.xguest = self.__getxguesttoken()

	#Public Function
	def get_profile(self, name: str=None, names: list=None, id: str=None, ids: dict=None) -> dict :
		target = None
		if not name is None :
			target = self.profile.format("screen_name",name)
		elif not id is None :
			target = self.profile.format("user_id",id)
		elif not names is None :
			target = [self.__get_twid(names), "screen_name"]
		elif not ids is None :
			target = [self.__get_twid(ids),"user_id"]
		
		if not name is None or not id is None :
			resp = self.__requestsdata(
				url=self.api,
				target=target
			)

			data = resp.json()
		else :
			data = []
			for x in target[0] :
				# print(x)
				resp = self.__requestsdata(
					url=self.api,
					target=self.profile.format(target[1],x)
				)
				
				for y in resp.json() :
					data.append(y)



		if resp.status_code >= 200 :
			if len(data) == 0 or "errors" in data:
				raise Exception("Error! User Not Found!")
			
			if len(data) >= 2 or not names is None or not ids is None  : 
				res = []
				for data_tw in data :
					res.append(
						TwitterScraperResultProfile(
							twitter_id=data_tw["id"],
							twitter_name=data_tw["name"],
							twitter_url=(self.url + data_tw["screen_name"]),
							twitter_screenname=data_tw["screen_name"],
							twitter_location=data_tw["location"],
							twitter_entities=data_tw["entities"],
							twitter_description=data_tw["description"] if "description" in data_tw else None ,
							twitter_verifed=data_tw["verified"] if "verified" in data_tw else None,
							twitter_pinned=True if len(data_tw["pinned_tweet_ids"]) is 0 else False,
							twitter_pinned_id=data_tw["pinned_tweet_ids"][0] if not len(data_tw["pinned_tweet_ids"]) is 0 else None ,
							twitter_follower=data_tw["followers_count"],
							twitter_following=data_tw["friends_count"] ,
							twitter_tweet=data_tw["statuses_count"] if "statuses_count" in data_tw else None ,
							twitter_media=data_tw["media_count"] if "media_count" in data_tw else None ,
							twitter_profileurl=data_tw["profile_image_url_https"].replace("_normal","") if "profile_image_url_https" in data_tw else None,
							twitter_favourites=data_tw["favourites_count"],
							twitter_bannerurl=data_tw["profile_banner_url"] if "profile_banner_url" in data_tw else None,
							twitter_profile_color=data_tw["profile_link_color"] if "profile_link_color" in data_tw else None,
							twitter_extended_url=data_tw["url"] if "url" in data_tw else None ,
							twitter_createat=datetime.datetime.strptime(data_tw["created_at"],"%a %b %d %H:%M:%S %z %Y"),
						)
					)
				
				return res
			else :
				# print(data)
				data_tw = data[0]
				return TwitterScraperResultProfile(
					twitter_id=data_tw["id"],
					twitter_name=data_tw["name"],
					twitter_url=(self.url + data_tw["screen_name"]),
					twitter_screenname=data_tw["screen_name"],
					twitter_location=data_tw["location"],
					twitter_entities=data_tw["entities"],
					twitter_description=data_tw["description"] if "description" in data_tw else None ,
					twitter_verifed=data_tw["verified"] if "verified" in data_tw else None,
					twitter_pinned=True if len(data_tw["pinned_tweet_ids"]) is 0 else False,
					twitter_pinned_id=data_tw["pinned_tweet_ids"][0] if not len(data_tw["pinned_tweet_ids"]) is 0 else None ,
					twitter_follower=data_tw["followers_count"],
					twitter_following=data_tw["friends_count"] ,
					twitter_tweet=data_tw["statuses_count"] if "statuses_count" in data_tw else None ,
					twitter_media=data_tw["media_count"] if "media_count" in data_tw else None ,
					twitter_profileurl=data_tw["profile_image_url_https"].replace("_normal","") if "profile_image_url_https" in data_tw else None,
					twitter_favourites=data_tw["favourites_count"],
					twitter_bannerurl=data_tw["profile_banner_url"] if "profile_banner_url" in data_tw else None,
					twitter_profile_color=data_tw["profile_link_color"] if "profile_link_color" in data_tw else None,
					twitter_extended_url=data_tw["url"] if "url" in data_tw else None ,
					twitter_createat=datetime.datetime.strptime(data_tw["created_at"],"%a %b %d %H:%M:%S %z %Y"),
				)


	def get_tweets(self,id: str=None,count: int=20) :
		i = 0
		tweets = []

		resp = self.__requestsdata(
			url=self.url,
			target=f"i/api/2/timeline/profile/{id}.json?userId={id}&count={count}"
		)

		if resp.status_code >= 400 :
			raise Exception("ID User Not Found!")

		data = resp.json()
		tweetslist = data["globalObjects"]["tweets"]

		for idtweet in tweetslist :
			datatweets = tweetslist[idtweet]
			if int(datatweets["user_id_str"]) == int(id) :
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

	def get_tweetinfo(self, id: str =None, count=20) :
		tweet = {}

		resp = self.__requestsdata(
			url=self.url,
			target=f"i/api/2/timeline/conversation/{id}.json?tweet_mode=extended&count={count}"
		)

		if resp.status_code >= 400 :
			raise Exception("ID Tweet Not Found!")

		data = resp.json()["globalObjects"]["tweets"]["%s" % id]

		tweet.update({
			"id" : int(data["id_str"]),
			"created_at" : datetime.datetime.strptime(data["created_at"],"%a %b %d %H:%M:%S %z %Y"),
			"lang" : "%s" % data["lang"],
			"text" : "%s" % data["full_text"] if "full_text" in data else data["text"],
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

		resp = self.__requestsdata(
			url=self.api,
			target=f"2/guide.json?tcount=20&tab_category=objective_trends"
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

	def get_tweetcomments(self,id: str=None) :
		i = 0
		commants = []

		resp = self.__requestsdata(
			url=self.url,
			target=f"i/api/2/timeline/conversation/{id}.json?tweet_mode=extended&count=10"
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

		resp = self.__requestsdata(
			url=self.url,
			target=f"i/api/1.1/search/typeahead.json?q={query}&src=search_box&result_type=events%2Cusers%2Ctopics"
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

	def __requestsdata(self,url,target) :
		session = HTMLSession()
		while True :
			i = 0
			try :
				proxy = {}
				if self.proxy_enable == True :
					proxy = {
						"http" : self.proxy_http,
						"https" : self.proxy_https
					}

				# Requests Data
				resp = session.get(
					(url + target),
					headers=self.__getdataheaders(),
					proxies=proxy,
					verify=False
				)
			
				headers = resp.headers

				if resp.status_code == 403 :
					self.token = self.__get_token()
					self.xguest = self.__getxguesttoken()

				if "x-rate-limit-limit" in headers :
					if headers["x-rate-limit-limit"] != headers["x-rate-limit-remaining"] :
						if resp.status_code != 429 :
							return resp
				else :
					if resp.status_code != 429 :
						return resp

			except requests.exceptions.SSLError as e :
				i += 1
				print(f"Connect Proxy Failed... Try connect of [ {i} / 10 ]")

				if i >= 10 :
					# print(e)
					raise requests.exceptions.SSLError(e)

				pass
	
	
	# Private Function
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
		proxy = {}

		if self.proxy_enable == True :
			proxy = {
				"http" : self.proxy_http,
				"https" : self.proxy_https
			}

		while True :
			session = HTMLSession()
			resp = session.post((self.api + "1.1/guest/activate.json"), headers=self.__getheaderstoken(), proxies=proxy, verify=False)

			if resp.status_code != 429 or resp.status_code != 403 or resp.status_code != 400 :
				# Get JS Data
				js_data = resp.json()

				if "guest_token" in js_data :
					return js_data["guest_token"]

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
	
	def __load_user_agent(self) :
		with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"user_agent.json"),"r") as data :
			return random.choice(json.loads(data.read()))

	def __get_twid(self, arr) -> dict:
		s = 0
		res = []

		while True :
			all_data = len(arr)
			get_ch = self.__format(arr,start=s)

			if all_data == get_ch[1] :
				res.append(get_ch[0])
				break
			
			res.append(get_ch[0])
			s += get_ch[1]

		return res

	def __format(self, arr: list, start=0) -> dict :
		prams = ""
		i,j  = 0, start

		for x in arr[start:len(arr)] :
			prams = prams + str(x) + ","
			if i == 99:
				return [prams,j]

			i += 1
			j += 1

		return [prams,j]
