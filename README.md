![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)
# Twitter-crawler  
Twitter-crawler is a crawler for collecting recent tweets of any Twitter user written in *Python 3.6*. The scraped data is stored in a *JSON* file named *twitter_data.json*. 

## Getting Started  


### Cloning the repository
```sh
git clone https://github.com/kaavehh/twitter-crawler
cd twitter-crawler
```
### Requirements   
- tweepy  

Install all requirements at once:
```powershell
pip install -r requirements.txt
```
Or install them one by one via *pip*:  
```sh
pip install tweetpy  
```  

### Setup Twitter authorization  
Make changes to [*twitter_oath_settings.py*](https://github.com/kaavehh/twitter-crawler/blob/c8a0ab8a8a821c354bc057a3484381de15761eb8/twitter_oath_settings.py) and replace your access tokens:  
```python  
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = "" 
```     
  
## Running the scripts  
```
python twitter_crawler.py  
```
*twitter_data.json* will be created in the current working directory. 

The default user whose tweets will be scraped is __Donald Trump__! It can be changed through the *screen_name* argument in [*twitter_crawler.py*](https://github.com/kaavehh/twitter-crawler/blob/c8a0ab8a8a821c354bc057a3484381de15761eb8/twitter_crawler.py#L22).  
The default number of scraped tweets is __25__. It can be changed through the *count* argument in [*twitter_crawler.py*](https://github.com/kaavehh/twitter-crawler/blob/c8a0ab8a8a821c354bc057a3484381de15761eb8/twitter_crawler.py#L22)

An example of an extracted tweet:  
```json
{"created_at": "Sun Mar 03 20:18:23 +0000 2019", "id": 1102302218903003141, "id_str": "1102302218903003141", "full_text": "The reason I do not want military drills with South Korea is to save hundreds of millions of dollars for the U.S. for which we are not reimbursed. That was my position long before I became President. Also, reducing tensions with North Korea at this time is a good thing!", "truncated": false, "display_text_range": [0, 270], "entities": {"hashtags": [], "symbols": [], "user_mentions": [], "urls": []}, "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", "in_reply_to_status_id": null, "in_reply_to_status_id_str": null, "in_reply_to_user_id": null, "in_reply_to_user_id_str": null, "in_reply_to_screen_name": null, "user": {"id": 25073877, "id_str": "25073877", "name": "Donald J. Trump", "screen_name": "realDonaldTrump", "location": "Washington, DC", "description": "45th President of the United States of America\ud83c\uddfa\ud83c\uddf8", "url": "https://t.co/OMxB0x7xC5", "entities": {"url": {"urls": [{"url": "https://t.co/OMxB0x7xC5", "expanded_url": "http://www.Instagram.com/realDonaldTrump", "display_url": "Instagram.com/realDonaldTrump", "indices": [0, 23]}]}, "description": {"urls": []}}, "protected": false, "followers_count": 58795574, "friends_count": 45, "listed_count": 100891, "created_at": "Wed Mar 18 13:46:38 +0000 2009", "favourites_count": 9, "utc_offset": null, "time_zone": null, "geo_enabled": true, "verified": true, "statuses_count": 40722, "lang": "en", "contributors_enabled": false, "is_translator": false, "is_translation_enabled": true, "profile_background_color": "6D5C18", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", "profile_background_tile": true, "profile_image_url": "http://pbs.twimg.com/profile_images/874276197357596672/kUuht00m_normal.jpg", "profile_image_url_https": "https://pbs.twimg.com/profile_images/874276197357596672/kUuht00m_normal.jpg", "profile_banner_url": "https://pbs.twimg.com/profile_banners/25073877/1550087458", "profile_link_color": "1B95E0", "profile_sidebar_border_color": "BDDCAD", "profile_sidebar_fill_color": "C5CEC0", "profile_text_color": "333333", "profile_use_background_image": true, "has_extended_profile": false, "default_profile": false, "default_profile_image": false, "following": false, "follow_request_sent": false, "notifications": false, "translator_type": "regular"}, "geo": null, "coordinates": null, "place": null, "contributors": null, "is_quote_status": false, "retweet_count": 12064, "favorite_count": 56042, "favorited": false, "retweeted": false, "lang": "en"}
```
  
## To-do list  
- Tweets analysis

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/kaavehh/trump-crawler/blob/master/LICENSE.md) file for details

## Links
- [Tweepy](http://www.tweepy.org)
