import urllib2
import json
import sys
import oauth2 as oauth
import constants

fb_consumer = oauth.Consumer(key=constants.FB_APP_ID, secret=constants.FB_SECRET)
fb_client = oauth.Client(fb_consumer)

#twitter oauth
t_consumer = oauth.Consumer(key=constants.TWITTER_CONSUMER_KEY, secret=constants.TWITTER_CONSUMER_SECRET)
access_token = oauth.Token(key=constants.TWITTER_ACCESS_KEY, secret=constants.TWITTER_ACCESS_SECRET)
t_client = oauth.Client(t_consumer, access_token)


token = constants.FB_ACCESS
endpoint = "https://graph.facebook.com/v2.5/285479221497876/posts?fields=picture,message,story,created_time,link,id&access_token="+token
resp, content = fb_client.request(endpoint)
content_dict = json.loads(content, strict=False)

f = open('static/json/fb.json', 'w')
f.truncate()
json.dump(content_dict, f)
f.close()


endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?count=25&include_rts=false&exclude_replies=true&user_id=525993877"
response, data = t_client.request(endpoint)
content = json.loads(data, strict=False)

f = open('static/json/twitter.json', 'w')
f.truncate()
json.dump(content, f)
f.close()


