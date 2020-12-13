# Twitter Scraper Python
Get data from twitter using REST API from Twitter :3

# Prerequisites
Before you begin, ensure you have met the following requirements:
* Python 3.6
* Internet Connnetion

# Installation
To install pytwitterscraper :

    pip install pytwitterscraper


# Usage 
First you have import libray pytwitterscraper :
    
    from pytwitterscraper import TwitterScraper
    

and call class object TwitterScraper :

    tw = TwitterScraper()

or you can able to use proxy :

    tw = TwitterScraper(proxy_enable=True, proxy_http="xxx.xxx.xxx.xxx:xxxx",proxy_https="xxx.xxx.xxx.xxx:xxxx")

If you have step by step You can able to use pytwitterscraper

# Class Object Data

| Class Object Classes | Description |
| ------ | ------ |
| get_profile(name=None,id=None,ids=[None],names=[None]) | Get Profile from Twitter **With select Name or ID or Names or IDS** |
| get_tweets(id,count=20) | Get List Tweet from Profille Twitter By ID |
| get_tweetinfo(id,count=20) | Get Tweet Information By ID |
| get_tweetcomments(id) | Get Tweet Comments By ID **Top 10 Comment** | 
| get_trends() | Get Trend Hashtags **Detect with IP Location** |
| searchkeywords(query) | Search Keyworld With Users and Topics |

# Example Code
1. Get Profile **Example : I want get profile from Shirakami Fubuki** :
    ```py 
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> profile = tw.get_profile(name="shirakamifubuki")
    >>> profile.__dict__
    >>> {'id': '997786053124616192', 'name': '白上フブキ@ShirakamiFubuki', 'screen_name': 'shirakamifubuki', 'url': 'https://twitter.com/shirakamifubuki', 'description': 'Vtuber事務所ホロライブプロダクション/1期生白上フブキ🦊❖担当絵師:凪白みと@lemon_mito 【ツイ担当】🦊は黒上🌽はユニコン 【絵】＃絵フブキ 【生放送】#フブキch 【切り抜き】#フブ切り【スケジュール】#白上式手抜きスケジュール', 'location': '誕生日\u3000１０月５日/ツイステ沼🐙アークナイツ沼/FGO沼', 'verifed': False, 'follower': 589583, 'following': 668, 'extended_url': 'https://t.co/R9TNhC7sPO', 'tweet': 75702, 'media': 9120, 'profileurl': 'https://pbs.twimg.com/profile_images/1322559849872334850/G2vq3G01.jpg', 'bannerurl': 'https://pbs.twimg.com/profile_banners/997786053124616192/1594284737', 'createat': datetime.datetime(2018, 5, 19, 10, 28, 27, tzinfo=datetime.timezone.utc)}
    ```

2. Get Profile **Example : I want get profile from ID 880317891249188864** :
    ```py 
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> profile = tw.get_profile(id="880317891249188864")
    >>> profile.__dict__
    >>> {'id': '880317891249188864', 'name': 'ときのそら🐻11/29.2ndLIVEパラレルタイム！', 'screen_name': 'tokino_sora', 'url': 'https://twitter.com/tokino_sora', 'description': '🎊 2ndアルバム『ON STAGE!』ビクターエンタテインメントより好評発売中！🎉11/29ときのそら2ndLIVE『パラレルタイム』開催決定！！🐻バーチャルアイドルときのそら(๑╹ᆺ╹)横アリ目指してがんばります୧(๑•̀ㅁ•́๑)૭✧❣️#ときのそら,#ときのそら生放送,#soraArt', 'location': '日本 東京', 'verifed': None, 'follower': 318548, 'following': 7123, 'extended_url': 'https://t.co/YVd92xsmZA', 'tweet': 19794, 'media': 1887, 'profileurl': 'https://pbs.twimg.com/profile_images/1296434665016844288/2RqmlpoD.jpg', 'bannerurl': 'https://pbs.twimg.com/profile_banners/880317891249188864/1602301415', 'createat': datetime.datetime(2017, 6, 29, 6, 51, 55, tzinfo=datetime.timezone.utc)}
    ```

3. Get Tweet **Example : I want get tweets from Shirakami Fubuki** :
    ```py 
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> tweets = tw.get_tweets(997786053124616192, count=3)
    >>> tweets.contents
    >>> [{'id': 1313103613204467712, 'created_at': datetime.datetime(2020, 10, 5, 13, 7, 52, tzinfo=datetime.timezone.utc), 'lang': 'ja', 'text': '✨白上フブキお誕生日記念ボイス＆グッズ✨おるやんけのぬいぐるみの夢が叶いましたそして湯呑もいつか作りたいと言ってた夢が叶いました夢が沢山詰まったグッズ達ですよろしくおねがいします🌽🔽購入はコチラ🔽… https://t.co/ZksPkhYQI2', 'hashtags': [], 'media': [], 'urls': [{'url': 'https://t.co/ZksPkhYQI2'}], 'likes': 8656, 'relay': 0, 'retweet': 2329}, {'id': 1325440832795635713, 'created_at': datetime.datetime(2020, 11, 8, 14, 11, 34, tzinfo=datetime.timezone.utc), 'lang': 'ja', 'text': '⏰２５時から\u3000ポルポルと一緒に幽霊調 査いくことになったよーー！！！！✨今ソロで頑張ってるみたいぞ(^・ω・^§)ﾉ【Phasmophobia】 本\u3000物\u3000の\u3000狂\u3000気 【尾丸ポルカ/ホロライブ】 https://t.co/MO7Xug3chb @YouTubeより', 'hashtags': [], 'media': [], 'urls': [{'url': 'https://t.co/MO7Xug3chb'}], 'likes': 1448, 'relay': 0, 'retweet': 254}, {'id': 1325458019069538304, 'created_at': datetime.datetime(2020, 11, 8, 15, 19, 52, tzinfo=datetime.timezone.utc), 'lang': 'ja', 'text': '⏰２５時から！！！！突発！キツネ属による🎪🌽✨✨Phasmophobia✨✨先輩調査員として引っ張っていくぞぉおおっ！ポルポルも上手くなってるので！２人でプロ調査しにいくぞぉぉおいっ！！！🔽待機しておるか🔽… https://t.co/2vUfw2RyY6', 'hashtags': [], 'media': [], 'urls': [{'url': 'https://t.co/2vUfw2RyY6'}], 'likes': 1707, 'relay': 0, 'retweet': 350}]
    ```

4. Get Tweet Info **Example : I want to get info ID Tweet 1324993735248109568** :
    ```py
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> twinfo = tw.get_tweetinfo(1324993735248109568)
    >>> twinfo.contents
    >>> {'id': 1324993735248109568, 'created_at': datetime.datetime(2020, 11, 7, 8, 34, 58, tzinfo=datetime.timezone.utc), 'lang': 'ja', 'text': '⏰２０時からです今日のお祝いは２０時からです！✨２１時は５期生コラボみたいから皆でみよーっ🌽100万人をみんなでお祝いするやーつ🔽いつもありがとっ🔽 https://t.co/JV5IW889AE #フブキch https://t.co/KSGTLDdnt3', 'hashtags': ['フブキch'], 'media': [], 'urls': [], 'likes': 4204, 'relay': 0, 'retweet': 771}
    ```

5. Get Tweet Comments **Example : I want to get comments from ID Tweet 1324993735248109568** :
    ```py
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> twcomments = tw.get_tweetcomments(1324993735248109568)
    >>> twcomments.contents
    >>> [{'id': 1324993789363056641, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 11, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki 了解です！！', 'hashtags': [], 'media': [], 'urls': [], 'likes': 0, 'relay': 0, 'retweet': 0}, {'id': 1324993879691599876, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 32, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki 了解です！', 'hashtags': [], 'media': [], 'urls': [], 'likes': 0, 'relay': 0, 'retweet': 0}, {'id': 1324993879611904000, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 32, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki 🥰🥰🥰🥰🥰🥰', 'hashtags': [], 'media': [], 'urls': [], 'likes': 0, 'relay': 0, 'retweet': 0}, {'id': 1324993804059897857, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 14, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki りょぴ！', 'hashtags': [], 'media': [], 'urls': [], 'likes': 0, 'relay': 0, 'retweet': 0}, {'id': 1324993901317529600, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 37, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki りょぴ！', 'hashtags': [], 'media': [], 'urls': [], 'likes': 0, 'relay': 0, 'retweet': 0}, {'id': 1324993889401413632, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 35, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki りょぴ！', 'hashtags': [], 'media': [], 'urls': [], 'likes': 0, 'relay': 0, 'retweet': 0}, {'id': 1324993901900386304, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 38, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki 塾で見れねー', 'hashtags': [], 'media': [], 'urls': [], 'likes': 1, 'relay': 0, 'retweet': 0}, {'id': 1324993880912064512, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 33, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki りょぴ！！', 'hashtags': [], 'media': [], 'urls': [], 'likes': 0, 'relay': 0, 'retweet': 0}, {'id': 1324993849077297155, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 25, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki 了解です〜！', 'hashtags': [], 'media': [], 'urls': [], 'likes': 0, 'relay': 0, 'retweet': 0}, {'id': 1324993855440052225, 'created_at': datetime.datetime(2020, 11, 7, 8, 35, 26, tzinfo=datetime.timezone.utc), 'comment': '@shirakamifubuki I love you fubuki', 'hashtags': [], 'media': [], 'urls': [], 'likes': 1, 'relay': 0, 'retweet': 0}]
    ```

6. Get Lasest Trends Twitter : 
    ```py
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> trends = tw.get_trends()
    >>> trends.content
    >>> [{'name': '#earthquake', 'description': None}, {'name': '#SundayMorning', 'description': 'Greeting a new day with grumpiness, enthusiasm, motivation and coffee'}, {'name': 'GOT7', 'description': None}, {'name': 'Newt', 'description': None}, {'name': '#SundayThoughts', 'description': 'Wisdom, inspiration and curiosity for your Sunday'}, {'name': '#sundayvibes', 'description': None}, {'name': '#AskFFT', 'description': None}, {'name': 'New Bedford', 'description': None}, {'name': 'Four Seasons Total Landscaping', 'description': "People express confusion after President Trump Tweets that a press conference will be held 'at Four Seasons Total Landscaping’"}, {'name': 'Britain', 'description': None}, {'name': 'Antonio Brown', 'description': None}, {'name': 'Bliss Corner', 'description': None}, {'name': 'Good Sunday', 'description': None}, {'name': 'Cape Cod', 'description': None}, {'name': 'Parler', 'description': None}, {'name': 'Rudy', 'description': None}, {'name': 'Football Sunday', 'description': None}, {'name': 'Romney', 'description': None}, {'name': 'Deejay Dallas', 'description': None}, {'name': 'NFL Sunday', 'description': None}, {'name': 'USGS', 'description': None}, {'name': 'Written', 'description': None}, {'name': 'Mike Williams', 'description': None}, {'name': 'Turtwig', 'description': None}, {'name': 'Marvin Jones', 'description': None}, {'name': 'Chark', 'description': None}, {'name': 'Jeudy', 'description': None}, {'name': 'Doherty', 'description': None}, {'name': 'Seahawks -3', 'description': None}, {'name': 'Kushner', 'description': None}]
    ```

7. Search Keyword :
    ```py
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> search = tw.searchkeywords("tokino_sora")
    >>> trends.users
    >>> [{'name': 'ときのそら🐻11/29.2ndLIVEパラレルタイム！', 'url': 'https://twitter.com/tokino_sora', 'profileurl': 'http://pbs.twimg.com/profile_images/1296434665016844288/2RqmlpoD_normal.jpg', 'bannerurl': 'https://pbs.twimg.com/profile_images/1296434665016844288/2RqmlpoD_normal.jpg', 'screen_name': 'tokino_sora', 'tags': ['tokino_sora', '@tokino_sora', 'tokino', 'sora', 'ときのそら🐻11/29.2ndliveパラレルタイム!']}, {'name': '時野空人', 'url': 'https://twitter.com/TokinoSorahito', 'profileurl': 'http://pbs.twimg.com/profile_images/480667036410863616/yeHCL21U_normal.png', 'bannerurl': 'https://pbs.twimg.com/profile_images/480667036410863616/yeHCL21U_normal.png', 'screen_name': 'TokinoSorahito', 'tags': ['tokinosorahito', '@tokinosorahito', '時野空人']}, {'name': 'Tokino Sora', 'url': 'https://twitter.com/TokinoSora25', 'profileurl': 'http://pbs.twimg.com/profile_images/1320705788218765313/xDbzLV47_normal.jpg', 'bannerurl': 'https://pbs.twimg.com/profile_images/1320705788218765313/xDbzLV47_normal.jpg', 'screen_name': 'TokinoSora25', 'tags': ['tokinosora25', '@tokinosora25', 'tokino', 'sora']}, {'name': 'Neil Qu', 'url': 'https://twitter.com/TokinoSoraFan', 'profileurl': 'http://pbs.twimg.com/profile_images/1222368653758255104/cmvSX51v_normal.jpg', 'bannerurl': 'https://pbs.twimg.com/profile_images/1222368653758255104/cmvSX51v_normal.jpg', 'screen_name': 'TokinoSoraFan', 'tags': ['tokinosorafan', '@tokinosorafan', 'neil', 'qu']}, {'name': "tokino sora's camera stand", 'url': 'https://twitter.com/randomrubeee', 'profileurl': 'http://pbs.twimg.com/profile_images/1325110251356643331/S6ctgUp0_normal.jpg', 'bannerurl': 'https://pbs.twimg.com/profile_images/1325110251356643331/S6ctgUp0_normal.jpg', 'screen_name': 'randomrubeee', 'tags': ['randomrubeee', '@randomrubeee', 'tokino', "sora's", 'camera', 'stand']}, {'name': 'Simp 4 Tokino Sora', 'url': 'https://twitter.com/kalatnieufene', 'profileurl': 'http://pbs.twimg.com/profile_images/1281801965815517185/DDaYI5yo_normal.jpg', 'bannerurl': 'https://pbs.twimg.com/profile_images/1281801965815517185/DDaYI5yo_normal.jpg', 'screen_name': 'kalatnieufene', 'tags': ['kalatnieufene', '@kalatnieufene', 'simp', '4', 'tokino', 'sora']}, {'name': 'sora tokino', 'url': 'https://twitter.com/sora_tokino', 'profileurl': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'bannerurl': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'screen_name': 'sora_tokino', 'tags': ['sora_tokino', '@sora_tokino', 'sora', 'tokino']}]
    >>> trends.topics
    >>> []
    ```
8. Get Profile **Example: I want get profile Tokino Sora by ID but i want use proxy not to rate limit** (HTTPS Required!) :
    ```py
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper(proxy_enable=True, proxy_http="xxx.xxx.xxx.xxx:xxxx",proxy_https="xxx.xxx.xxx.xxx:xxxx")
    >>> tw.get_profile(id=880317891249188864).__dict__
    >>> {'id': 880317891249188864, 'name': 'ときのそら�🐻ONSTAG！！', 'screen_name': 'tokino_sora', 'url': 'https://t.co/YVd92xsmZA', 'description': '🎊🎊 nアルバムム『『ON STAE』ビクターエンタテインrトより好評発売中！�🎉11/2ときのそらら2ndLIV『パラレルタイム』開催決定！！��バーチャルアイドルときのそそらら(๑╹╹横アリ目指してがんばりまますす୧(•̀ㅁㅁ•́๑)૭✧️ときのそそら,ときのそら生放放送送,#soraArttion': '日本 東京', 'entities': {'url': {'urls': [{'url': 'https://t.co/YVd92xsmZA', 'expanded_url': 'https://youtube.com/channel/UCp6993wxpyDPHUpavwDFqgg?sub_confirmation=1', 'display_urlocation': '日本 東京', 'entities': {'url': {'urls': [{'url': 'https://t.co/YVd92xsmZA', 'expanded_url': 'https://youtube.com/channel/UCp6993wxpyDPHUpavwDFqgg?sub_confirmation=1', 'display_url': 'youtube.com/channel/UCp699…', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'verifed': False, 'follower': 347116, 'following': 7125, 'extended_url': 'https://t.co/YVd92xsmZA', 'tweet': 20483, 'media': 1950, 'profileurl': 'https://pbs.twimg.com/profile_images/1333357590911152132/WNtw6XJI.jpg', 'bannerurl': 'https://pbs.twimg.com/profile_banners/880317891249188864/1606732197', 'favourites': 110200, 'pinned': False, 'pinned_id': 1335930331111669761, 'profile_color': '1DA1F2', 'createat': datetime.datetime(2017, 6, 29, 6, 51, 55, tzinfo=datetime.timezone.utc)}
    ```
9. Get many Profile By ID **Example: I want get profile screen_name Tokino Sora and Shirakami Fubuki By ID**
    ```py
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> data = tw.get_profile(ids=[880317891249188864,997786053124616192])
    >>> for data_mem in data :
    >>>     print(data_mem.screen_name)
    >>> tokino_sora
    >>> shirakamifubuki
    ```

10. Get many Profile By Name **Example: I want get profile ID Tokino Sora and Shirakami Fubuki By Name**
    ```py
    >>> from pytwitterscraper import TwitterScraper
    >>> tw = TwitterScraper()
    >>> data = tw.get_profile(names=["tokino_sora","shirakamifubuki"])
    >>> for data_mem in data :
    >>>     print(data_mem.id)
    >>> 880317891249188864
    >>> 997786053124616192
    ```

# Lastest 
I have to thanks for source code from 
- dgnsrekt 

 I have make some awsome project :3

สุดท้ายนี้... ขอไปด้วยภาพ เมนตัวเองล่ะกัน ปล. มีอีกเมนหนึ่ง

![Fubuki F R I E N D](https://media1.tenor.com/images/0d99bbdd3327e45bb49262bc25a34997/tenor.gif)


# License

MIT
